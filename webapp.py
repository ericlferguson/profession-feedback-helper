import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from performance_review_generator import PerformanceReviewGenerator, DEFAULT_LEVEL_MAP
from resume_session_utils import get_latest_session_file, load_session_data

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure server-side session (filesystem-based by default)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = os.path.join(os.path.dirname(__file__), 'flask_session')
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
Session(app)

# Resume last session route
@app.route('/resume', methods=['POST'])
def resume():
    session_file = get_latest_session_file()
    if not session_file:
        return redirect(url_for('index'))
    data = load_session_data(session_file)
    # Restore all keys from the loaded session into the current session
    for k, v in data.items():
        session[k] = v
    return redirect(url_for('chatgpt_results'))

# Utility to get available roles from YAML files
def get_available_roles():
    role_dir = os.path.join(os.path.dirname(__file__), 'role_definitions')
    roles = []
    for fname in os.listdir(role_dir):
        if fname.endswith('.yaml'):
            roles.append(fname.replace('.yaml', '').replace('_', ' ').title())
    return sorted(roles)

@app.route('/', methods=['GET', 'POST'])
def index():
    roles = get_available_roles()
    levels = list(DEFAULT_LEVEL_MAP.keys())
    # Check if there is a resumable session file
    resume_available = get_latest_session_file() is not None
    if request.method == 'POST':
        name = request.form['name']
        pronouns = [request.form['pronoun_subject'], request.form['pronoun_possessive']]
        role = request.form['role']
        level = request.form['level']
        session['user_info'] = dict(name=name, pronouns=pronouns, role=role, level=level)
        return redirect(url_for('feedback'))
    return render_template('index.html', roles=roles, levels=levels, resume_available=resume_available)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    user_info = session.get('user_info')
    if not user_info:
        return redirect(url_for('index'))
    # Generate responsibilities from YAML
    generator = PerformanceReviewGenerator(
        name=user_info['name'],
        pronouns=user_info['pronouns'],
        role=user_info['role'],
        level=user_info['level'],
        get_chatgpt_feedback=False,
    )
    # Flatten for form rendering
    items = []
    section_order = []
    for section, subs in generator.responsibilities.items():
        for subsection, behaviors in subs.items():
            for behavior in behaviors:
                items.append((section, subsection, behavior))
        section_order.append(section)
    # Ensure 'overview' is first, then rest sorted
    if 'overview' in section_order:
        sections = ['overview'] + sorted([s for s in set(section_order) if s != 'overview'])
    else:
        sections = sorted(set(section_order))
    if request.method == 'POST':
        ratings = {}
        comments = {}
        for i, (section, subsection, behavior) in enumerate(items):
            key = f'rating_{i}'
            ratings[(section, subsection, behavior)] = int(request.form[key])
        for section in sections:
            comments[section] = request.form.get(f'comment_{section}', '').strip()
        # Fill feedback lists based on ratings
        generator.exceeds_list = {}
        generator.meets_list = {}
        generator.does_not_meet_list = {}
        for (section, subsection, behavior), rating in ratings.items():
            if rating == 0:
                generator.does_not_meet_list.setdefault(section, []).append(behavior)
            elif rating == 1:
                generator.meets_list.setdefault(section, []).append(behavior)
            elif rating == 2:
                generator.exceeds_list.setdefault(section, []).append(behavior)
        # Set section comments
        generator.section_comments = comments
        generator.give_feedback()
        # Prepare detailed summary for results
        summary = {
            'exceeds': generator.exceeds_list,
            'meets': generator.meets_list,
            'does_not_meet': generator.does_not_meet_list,
            'comments': comments,
            'user': user_info,
        }
        session['feedback'] = generator.feedback
        session['summary'] = summary
        # Store generator state for ChatGPT feedback
        session['chatgpt_input'] = dict(
            name=user_info['name'],
            pronouns=user_info['pronouns'],
            role=user_info['role'],
            level=user_info['level'],
            exceeds=generator.exceeds_list,
            meets=generator.meets_list,
            does_not_meet=generator.does_not_meet_list,
            comments=comments,
        )
        return redirect(url_for('chatgpt_results'))
    return render_template('feedback.html', items=items, user=user_info, sections=sections)


@app.route('/chatgpt_results')
def chatgpt_results():
    import time
    chatgpt_result = session.get('chatgpt_result')
    chatgpt_input = session.get('chatgpt_input')
    summary = session.get('summary')
    # Compute all unique section names for summary
    all_sections = []
    if summary:
        all_sections = set(summary['meets'].keys()) | set(summary['exceeds'].keys()) | set(summary['does_not_meet'].keys())
        all_sections = sorted(all_sections)
    if chatgpt_result:
        return render_template('chatgpt_results.html', chatgpt_result=chatgpt_result, summary=summary, all_sections=all_sections)
    if not chatgpt_input:
        return redirect(url_for('index'))
    # Show loading page while waiting
    if request.args.get('waited') != '1':
        # Start feedback generation and redirect after a short wait
        return render_template('loading.html')
    # Actually generate feedback
    generator = PerformanceReviewGenerator(
        name=chatgpt_input['name'],
        pronouns=chatgpt_input['pronouns'],
        role=chatgpt_input['role'],
        level=chatgpt_input['level'],
        get_chatgpt_feedback=True,
    )
    # Restore feedback lists
    generator.exceeds_list = chatgpt_input['exceeds']
    generator.meets_list = chatgpt_input['meets']
    generator.does_not_meet_list = chatgpt_input['does_not_meet']
    generator.section_comments = chatgpt_input['comments']  # Fix: use section_comments instead of comments
    generator.give_feedback()
    generator.get_chatgpt_feedback()
    session['chatgpt_result'] = generator.chatgpt_feedback
    # LOGGING: Save user input/output to JSONL
    import json, datetime
    log_entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'user_info': chatgpt_input,
        'summary': summary,
        'chatgpt_result': generator.chatgpt_feedback,
    }
    try:
        os.makedirs('logs', exist_ok=True)
        # Build a safe filename
        def safe(s):
            return ''.join(c if c.isalnum() else '_' for c in s.lower())
        username = safe(chatgpt_input.get('name', 'anon'))
        role = safe(chatgpt_input.get('role', 'role'))
        level = safe(chatgpt_input.get('level', 'level'))
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        fname = f'logs/{username}_{role}_{level}_{timestamp}.json'
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(log_entry, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f'Could not write log: {e}')
    return render_template('chatgpt_results.html', chatgpt_result=generator.chatgpt_feedback, summary=summary, all_sections=all_sections)

if __name__ == '__main__':
    app.run(debug=True)

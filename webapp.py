import os
from flask import Flask, render_template, request, redirect, url_for, session
from performance_review_generator import PerformanceReviewGenerator, LEVEL_MAP

app = Flask(__name__)
app.secret_key = os.urandom(24)

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
    levels = list(LEVEL_MAP.keys())
    if request.method == 'POST':
        name = request.form['name']
        pronouns = [request.form['pronoun_subject'], request.form['pronoun_possessive']]
        role = request.form['role']
        level = request.form['level']
        session['user_info'] = dict(name=name, pronouns=pronouns, role=role, level=level)
        return redirect(url_for('feedback'))
    return render_template('index.html', roles=roles, levels=levels)

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
    sections = set()
    for section, subs in generator.responsibilities.items():
        for subsection, behaviors in subs.items():
            for behavior in behaviors:
                items.append((section, subsection, behavior))
                sections.add(section)
    sections = sorted(sections)
    if request.method == 'POST':
        ratings = {}
        comments = {}
        for i, (section, subsection, behavior) in enumerate(items):
            key = f'rating_{i}'
            ratings[(section, subsection, behavior)] = int(request.form[key])
        for section in sections:
            comments[section] = request.form.get(f'comment_{section}', '').strip()
        # Fill feedback lists based on ratings
        generator.okay_list = {}
        generator.going_well_list = {}
        generator.feedback_list = {}
        for (section, subsection, behavior), rating in ratings.items():
            if rating == 0:
                generator.feedback_list.setdefault(section, []).append(behavior)
            elif rating == 1:
                generator.okay_list.setdefault(section, []).append(behavior)
            elif rating == 2:
                generator.going_well_list.setdefault(section, []).append(behavior)
        generator.give_feedback()
        # Prepare detailed summary for results
        summary = {
            'going_well': generator.going_well_list,
            'meets': generator.okay_list,
            'needs_improvement': generator.feedback_list,
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
            going_well=generator.going_well_list,
            meets=generator.okay_list,
            needs_improvement=generator.feedback_list,
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
        all_sections = set(summary['meets'].keys()) | set(summary['going_well'].keys()) | set(summary['needs_improvement'].keys())
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
    generator.going_well_list = chatgpt_input['going_well']
    generator.okay_list = chatgpt_input['meets']
    generator.feedback_list = chatgpt_input['needs_improvement']
    generator.comments = chatgpt_input['comments']
    generator.give_feedback()
    generator.get_chatgpt_feedback()
    session['chatgpt_result'] = generator.chatgpt_feedback
    return render_template('chatgpt_results.html', chatgpt_result=generator.chatgpt_feedback, summary=summary, all_sections=all_sections)

if __name__ == '__main__':
    app.run(debug=True)

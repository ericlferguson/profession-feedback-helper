import os
import tempfile
import pytest
from flask import session
from webapp import app

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    client = app.test_client()
    yield client
    os.close(db_fd)
    os.unlink(db_path)

def test_index_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Performance Review Generator" in rv.data
    assert b"Start Review" in rv.data or b"Submit" in rv.data

def test_feedback_flow(client):
    # Simulate filling out the index form
    response = client.post('/', data={
        'name': 'Test User',
        'pronoun_subject': 'they',
        'pronoun_possessive': 'their',
        'role': 'Software Engineer',
        'level': 'junior',
    }, follow_redirects=True)
    assert b"Provide Feedback" in response.data
    # Extract feedback items from the rendered form
    # For simplicity, select 'meets' (1) for all behaviors
    from webapp import PerformanceReviewGenerator
    gen = PerformanceReviewGenerator(
        name='Test User',
        pronouns=['they', 'their'],
        role='Software Engineer',
        level='junior',
    )
    items = []
    for section, subs in gen.responsibilities.items():
        for subsection, behaviors in subs.items():
            for behavior in behaviors:
                items.append((section, subsection, behavior))
    feedback_data = {f'rating_{i}': '1' for i in range(len(items))}
    for section in set(s for s, _, _ in items):
        feedback_data[f'comment_{section}'] = f"Comment for {section}"
    rv = client.post('/feedback', data=feedback_data, follow_redirects=True)
    # Should redirect to loading or results page
    assert rv.status_code == 200
    assert b"Generating summary" in rv.data or b"Feedback Summary" in rv.data

def test_chatgpt_results_route(client, monkeypatch):
    # Simulate session state for /chatgpt_results
    with client.session_transaction() as sess:
        sess['chatgpt_result'] = 'LLM summary here.'
        sess['summary'] = {'meets': {}, 'going_well': {}, 'needs_improvement': {}, 'comments': {}, 'user': {}}
        sess['chatgpt_input'] = {
            'name': 'Test User',
            'pronouns': ['they', 'their'],
            'role': 'Software Engineer',
            'level': 'junior',
            'going_well': {}, 'meets': {}, 'needs_improvement': {}, 'comments': {}
        }
    rv = client.get('/chatgpt_results')
    assert rv.status_code == 200
    assert b"LLM summary here." in rv.data
    assert b"Feedback Summary" in rv.data

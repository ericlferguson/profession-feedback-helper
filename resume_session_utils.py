import os
import pickle

SESSION_DIR = os.path.join(os.path.dirname(__file__), 'flask_session')


def get_latest_session_file():
    files = [
        os.path.join(SESSION_DIR, f)
        for f in os.listdir(SESSION_DIR)
        if os.path.isfile(os.path.join(SESSION_DIR, f))
    ]
    if not files:
        return None
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return files[0]


def load_session_data(session_file):
    with open(session_file, 'rb') as f:
        data = f.read()
    # Scan for the start of a pickle stream (0x80 or 0x81)
    for i in range(len(data)):
        if data[i] in (0x80, 0x81):
            try:
                return pickle.loads(data[i:])
            except Exception:
                continue
    raise ValueError(f'No valid pickle found in {session_file}')

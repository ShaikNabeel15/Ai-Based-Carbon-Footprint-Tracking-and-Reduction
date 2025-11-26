import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
FACTORIES_FILE = os.path.join(DATA_DIR, 'factories.json')
TRANSACTIONS_FILE = os.path.join(DATA_DIR, 'transactions.json')

def _ensure_file_exists(filepath, default_content=[]):
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump(default_content, f, indent=4)

def load_data(filename):
    filepath = os.path.join(DATA_DIR, filename)
    _ensure_file_exists(filepath)
    with open(filepath, 'r') as f:
        return json.load(f)

def save_data(filename, data):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def get_factories():
    return load_data('factories.json')

def save_factories(factories):
    save_data('factories.json', factories)

def get_transactions():
    return load_data('transactions.json')

def save_transactions(transactions):
    save_data('transactions.json', transactions)

import json
from .entropy_checker import calculate_entropy, evaluate_strength

def scan_password_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    results = []
    for account, pwd in data.items():
        entropy = calculate_entropy(pwd)
        strength = evaluate_strength(entropy)
        results.append({
            "account": account,
            "password": pwd,
            "entropy": entropy,
            "strength": strength
        })
    return results

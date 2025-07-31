import argparse
from analyzer.entropy_checker import calculate_entropy, evaluate_strength
from analyzer.password_suggester import suggest_password, suggest_passphrase
from analyzer.password_scanner import scan_password_file

parser = argparse.ArgumentParser(description="Password Analyzer Tool")
parser.add_argument("-p", "--password", help="Check strength of a password")
parser.add_argument("-s", "--suggest", help="Suggest strong password", action="store_true")
parser.add_argument("-f", "--file", help="Scan JSON file of saved passwords")

args = parser.parse_args()

if args.password:
    entropy = calculate_entropy(args.password)
    strength = evaluate_strength(entropy)
    print(f"Entropy: {entropy} bits\nStrength: {strength}")

if args.suggest:
    print("Random Strong Password:", suggest_password())
    print("Passphrase Suggestion:", suggest_passphrase())

if args.file:
    results = scan_password_file(args.file)
    for entry in results:
        print(f"{entry['account']}: {entry['strength']} ({entry['entropy']} bits)")

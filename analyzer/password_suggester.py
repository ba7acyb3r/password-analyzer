import secrets
import string

def suggest_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def suggest_passphrase():
    words = ["correct", "horse", "battery", "staple", "moon", "light", "river", "stone", "cloud"]
    return ' '.join(secrets.choice(words) for _ in range(4))

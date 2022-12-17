import random
import string

def generate_password(length, blacklist):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    available_chars = [c for c in all_chars if c not in blacklist]
    password = "".join(random.choices(available_chars, k=length))
    return password

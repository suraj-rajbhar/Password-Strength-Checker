import re

def password_strength(password):
    # Checking for the minimum length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."

    # Checking for uppercase letters
    if not re.search(r"[A-Z]", password):
        return "Password should contain at least one uppercase letter."

    # Checking for lowercase letters
    if not re.search(r"[a-z]", password):
        return "Password should contain at least one lowercase letter."

    # Checking for numbers
    if not re.search(r"[0-9]", password):
        return "Password should contain at least one number."

    # Checking for special characters
    if not re.search(r"[!@#$%^&*()_+=-{};:'<>,.?/`~]", password):
        return "Password should contain at least one special character."

    return "Your password is strong."

# Test the function
print(password_strength("prodigy123"))

#password strength checker

def check_password_strength(password):
    strength = 0

    if len(password) >= 0 :
        strength += 1
    if any(char.islower() for char in password ):
        strength += 1
    if any(char.isupper() for char in password ):
        strength += 1
    if any(char.isupper() for char in password ):
        strength += 1
    if any(char in for char in password ):
        strength += 1
import string

from constants import PWD_STRENGTH


def password_strength(password):
    strength = 0
    if len(password) >= 6:
        strength += 1

    if len(password) >= 8:
        strength += 1

    for letter in password:
        if letter in string.ascii_lowercase:
            strength += 1
        if letter.isupper():
            strength += 1
        if letter.isalpha():
            strength += 1
        if letter.isdigit():
            strength += 1
        if letter in string.punctuation:
            strength += 1

    return PWD_STRENGTH["STRONG"] if strength == 6 else \
        PWD_STRENGTH["MEDIUM"] if strength >= 4 else \
        PWD_STRENGTH["WEAK"]

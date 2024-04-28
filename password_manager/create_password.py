import getpass

from constants import PWD_STRENGTH
from password_strength import password_strength


def create_password(prompt=str('Enter a password: ')):
    password = getpass.getpass(prompt=prompt).strip()
    print("Password is " + password_strength(password))

    while password_strength(password) == PWD_STRENGTH["WEAK"]:
        vault_password = getpass.getpass(prompt=prompt).strip()
        print("Password is " + password_strength(vault_password))

    return password

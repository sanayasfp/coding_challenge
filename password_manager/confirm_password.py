import getpass


def confirm_password(password: str = None, attempts=5, prompt=str('Confirm a password: ')):
    if password is None:
        raise ValueError("Password is empty")

    confirmation = getpass.getpass(prompt=prompt).strip()
    attempts -= 1

    while password != confirmation and attempts > 0:
        confirmation = getpass.getpass(prompt=prompt).strip()
        attempts -= 1

    if attempts == 0:
        print("Too many attempts")
        exit(1)

    return password

import json
import os
import re
import time

import constants
import records
from encrypt import encrypt
from hash import h


def vault_path(v_file_name=str("")):
    return os.path.join(os.getcwd(), "./.vaults", v_file_name)


def vault_file_name(*name: str):
    return h(*name) + constants.VAULT_EXTENSION


def record_file_name(*name: str):
    return h(*name) + constants.RECORD_EXTENSION


def check_inactive_time():
    signed_at_str = os.getenv(constants.SIGNED_AT)
    signed_at = float(signed_at_str) if signed_at_str else 0

    if (time.time() - signed_at) > 180:
        os.environ[constants.SIGNED_VAULT_NAME] = ""
        os.environ[constants.SIGNED_VAULT_PASSWORD] = ""
        return False
    else:
        return True


def check_signed():
    if not check_inactive_time():
        return False

    if os.getenv(constants.SIGNED_VAULT_PASSWORD) and os.getenv(constants.SIGNED_VAULT_NAME):
        os.environ[constants.SIGNED_AT] = str(int(time.time()))
        return True
    else:
        return False


def get_signed_vars():
    if check_signed():
        return {
            "name": os.getenv(constants.SIGNED_VAULT_NAME),
            "password": os.getenv(constants.SIGNED_VAULT_PASSWORD),
        }

    return None


def get_record_files(record_id: str):
    file_name = record_file_name(record_id, get_signed_vars()["password"])
    salt_file_name = record_file_name("salt", record_id, get_signed_vars()["password"])
    file_path = vault_path(file_name)
    salt_file_path = vault_path(salt_file_name)

    return file_path, salt_file_path


def no_empty_input(prompt="", max_attempts=10):
    value = input(prompt).strip()

    while not value:
        value = input(prompt).strip()
        max_attempts -= 1

        if max_attempts <= 0:
            return None

    return value


def update_record_username_and_password(record_id: str, record: dict, message="Record"):
    record_file_path, record_salt_file_path = get_record_files(record_id)

    with open(record_salt_file_path, 'rb') as salt_file:
        salt = salt_file.read()
        salt_file.close()

    new_encrypted_record = encrypt(password=get_signed_vars()["password"], message=json.dumps(record),
                                   salt=salt)

    while True:
        try:
            records.update(None, record_id, new_salt=salt, new_record=new_encrypted_record)

            print(f"{message} updated successfully")
            return
        except FileExistsError:
            confirm = input("Confirm update? (y/n) ").strip().lower()
            if confirm == "y":
                os.remove(record_file_path)
                os.remove(record_salt_file_path)
            else:
                print(f"{message} not updated!")
                return


def is_valid_file_name(file_name):
    pattern = r"^[a-zA-Z0-9_\-\.]{1,26}$"
    return re.match(pattern, file_name) is not None

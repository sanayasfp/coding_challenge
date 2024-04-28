import json
import os

from Crypto.Random import get_random_bytes

import constants
import records
import utils
from confirm_password import confirm_password
from create_password import create_password
from encrypt import encrypt


def add_password_to_vault():
    record_id = utils.no_empty_input('Enter record name: ')

    if not record_id:
        return

    username = utils.no_empty_input('Enter username: ')

    if not username:
        return

    password = create_password()

    confirm_password(password, attempts=5, prompt="Please confirm password: ")

    record_file_path, record_salt_file_path = utils.get_record_files(record_id)
    record_salt = get_random_bytes(32)
    record_data = {
        "record_id": record_id,
        "username": username,
        "password": password,
    }

    encrypted_record = encrypt(password=utils.get_signed_vars()["password"], message=json.dumps(record_data),
                               salt=record_salt)

    while True:
        try:
            records.create(record_id, salt=record_salt, record=encrypted_record)

            print(f"Record added to vault {utils.get_signed_vars()['name']} successfully.")
            return
        except FileExistsError:
            confirm = input("Record already exists. Do you want to overwrite it? (y/n) ").strip().lower()
            if confirm == "y":
                os.remove(record_file_path)
                os.remove(record_salt_file_path)
            else:
                print("Record not added to vault!")
                return


if __name__ == '__main__':
    add_password_to_vault()

import json
import os

import utils
from decrypt import decrypt
from encrypt import encrypt


def create(record_id: str, salt: bytes, record: bytes | dict):
    record_file_path, record_salt_file_path = utils.get_record_files(record_id)

    if isinstance(record, bytes):
        encrypted_record = record
    else:
        encrypted_record = encrypt(password=utils.get_signed_vars()["password"],
                                   message=json.dumps(record),
                                   salt=salt)

    with open(record_salt_file_path, "xb") as file:
        file.write(salt)
        file.close()

    with open(record_file_path, "xb") as file:
        file.write(encrypted_record)
        file.close()


def read(record_id: str, password: str) -> dict | None:
    try:
        record_file_path, record_salt_file_path = utils.get_record_files(record_id)

        with open(record_salt_file_path, 'rb') as salt_file:
            salt = salt_file.read()
            salt_file.close()

        with open(record_file_path, 'rb') as record_file:
            record_data = record_file.read()
            record_file.close()

        decrypted_record = decrypt(password, record_data, salt)

        return json.loads(decrypted_record)
    except FileNotFoundError:
        return None


def update(record_id: str | None, new_record_id: str, new_salt: bytes, new_record: bytes | dict):
    create(new_record_id, new_salt, new_record)

    if record_id is not None:
        record_file_path, record_salt_file_path = utils.get_record_files(record_id)
        os.remove(record_file_path)
        os.remove(record_salt_file_path)


def delete():
    pass

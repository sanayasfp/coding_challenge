import json
import os

from Crypto.Random import get_random_bytes

import records
import utils
from encrypt import encrypt

global TRANSFERRED_PARAMS


def update_record_name():
    record_id = TRANSFERRED_PARAMS['record_id']
    record = records.read(record_id, password=utils.get_signed_vars()["password"])

    if record:
        new_record_id = utils.no_empty_input('Enter new record name: ')

        if not new_record_id:
            return

        record["record_id"] = new_record_id
        new_record_salt = get_random_bytes(32)
        new_encrypted_record = encrypt(password=utils.get_signed_vars()["password"], message=json.dumps(record),
                                       salt=new_record_salt)
        new_record_file_path, new_record_salt_file_path = utils.get_record_files(new_record_id)

        while True:
            try:
                records.update(record_id, new_record_id, new_salt=new_record_salt, new_record=new_encrypted_record)
                TRANSFERRED_PARAMS['record_id'] = new_record_id

                print("Record updated successfully")
                return
            except FileExistsError:
                confirm = input("Record already exists. Do you want to overwrite it? (y/n) ").strip().lower()
                if confirm == "y":
                    os.remove(new_record_file_path)
                    os.remove(new_record_salt_file_path)
                else:
                    print("Record not updated!")
                    return


if __name__ == '__main__':
    update_record_name()

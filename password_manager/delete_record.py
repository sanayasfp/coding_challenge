import os

import records
import utils

global TRANSFERRED_PARAMS
global DISPLAY_MENU


def delete_record():
    record_id = TRANSFERRED_PARAMS['record_id']
    record = records.read(record_id, password=utils.get_signed_vars()["password"])

    if record:
        print("Are you sure you want to delete the record?")
        confirm = input("Type the record name to confirm deletion: ").strip()

        if confirm == record_id:
            record_file_path, record_salt_file_path = utils.get_record_files(record_id)

            os.remove(record_file_path)
            os.remove(record_salt_file_path)

            print(f"Record {record_id} deleted from {utils.get_signed_vars()['name']} vault.")

            global DISPLAY_MENU
            DISPLAY_MENU = False
        else:
            print(f"Record not deleted!")
            return


if __name__ == '__main__':
    delete_record()

import pyperclip

import records
import utils


def fetch_password_from_vault():
    record_id = input("Please enter the record name: ")
    record = records.read(record_id, password=utils.get_signed_vars()["password"])

    if not record:
        print("Record not found!")
        return

    copy_to_clipboard = input("Would you like to copy the record to clipboard? (y/n): ").strip().lower()

    if copy_to_clipboard == 'y':
        pyperclip.copy(record["username"])
        input("Username copied to clipboard. Press Enter to copy password")
        pyperclip.copy(record["password"])
        print("Password copied!")
        return

    print(f"For {record['record_id']} record")
    print("The username is", record["username"])
    print("The password is:", record["password"])


if __name__ == '__main__':
    fetch_password_from_vault()

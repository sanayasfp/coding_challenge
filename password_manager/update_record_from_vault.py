import records
import utils
from display_menu import display_menu

global TRANSFERRED_PARAMS

menu = {
    "title": "",
    "subtitle": "",
    "description": "What do you want to modify?",
    "items": [
        {
            "auth": True,
            "label": "Record name",
            "action": "update_record_name",
            "keys": ["1"]
        },
        {
            "auth": True,
            "label": "Username",
            "action": "update_record_username",
            "keys": ["2"]
        },
        {
            "auth": True,
            "label": "Password",
            "action": "update_record_password",
            "keys": ["3"]
        },
        {
            "auth": True,
            "label": "Delete record",
            "action": "delete_record",
            "keys": ["4"]
        },
        {
            "label": "Cancel (enter c to cancel)",
            "action": "quit",
            "keys": ["5", "c", "q", "quit"]
        }
    ]
}


def update_record_from_vault():
    record_id = input("Please enter the record name: ")

    if not utils.get_signed_vars():
        return

    record = records.read(record_id, password=utils.get_signed_vars()["password"])

    if not record:
        print("Record not found!")
        return

    TRANSFERRED_PARAMS["record_id"] = record_id

    display_menu(menu, TRANSFERRED_PARAMS)

    del TRANSFERRED_PARAMS["record_id"]


if __name__ == '__main__':
    update_record_from_vault()

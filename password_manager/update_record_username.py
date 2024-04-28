import records
import utils

global TRANSFERRED_PARAMS


def update_record_username():
    record_id = TRANSFERRED_PARAMS['record_id']
    record = records.read(record_id, password=utils.get_signed_vars()["password"])

    if record:
        new_username = utils.no_empty_input('Enter new username: ')

        if not new_username:
            return

        record["username"] = new_username

        utils.update_record_username_and_password(record_id, record, "Username")


if __name__ == '__main__':
    update_record_username()

import records
import utils
from confirm_password import confirm_password
from create_password import create_password

global TRANSFERRED_PARAMS


def update_record_username():
    record_id = TRANSFERRED_PARAMS['record_id']
    record = records.read(record_id, password=utils.get_signed_vars()["password"])

    if record:
        password = create_password()

        confirm_password(password, attempts=5, prompt="Please confirm password: ")

        record["password"] = password

        utils.update_record_username_and_password(record_id, record, "Password")


if __name__ == '__main__':
    update_record_username()

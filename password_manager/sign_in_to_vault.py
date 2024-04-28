import getpass
import os
from time import time

import constants
import utils
from hash import compare


def sign_in_to_vault():
    v_name = input("Enter vault name: ").strip()
    v_password = getpass.getpass(f"Enter password for the {v_name} vault:").strip()
    v_file_path = utils.vault_path(utils.vault_file_name(v_name, v_password))

    try:
        with open(v_file_path, "r") as v_file:
            v_data = v_file.read().strip().split("\n")
            v_data = [line.strip() for line in v_data]

            if len(v_data) != 4:
                print("Vault compromised. Please try again.")
                return

            _, read_v_name, read_v_hash, _ = v_data

            if not all([
                compare(read_v_hash, read_v_name),
                read_v_name == v_name
            ]):
                print("Vault compromised. Please try again.")
                return

            os.environ[constants.SIGNED_VAULT_NAME] = v_name
            os.environ[constants.SIGNED_VAULT_PASSWORD] = v_password
            os.environ[constants.SIGNED_AT] = str(time())

            print("Thank you, you are now signed in.")
    except FileNotFoundError:
        print("Verify vault name and password")


if __name__ == "__main__":
    sign_in_to_vault()

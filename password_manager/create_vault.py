import utils
from confirm_password import confirm_password
from constants import VAULT_EXTENSION
from create_password import create_password
from hash import h


def create_vault():
    vault_name = input("Please provide a name for the vault: ").strip()

    while not utils.is_valid_file_name(vault_name):
        vault_name = input("Please provide a name for the vault: ").strip()

    vault_password = create_password(prompt="Please enter a master password: ")

    confirm_password(vault_password, attempts=5, prompt="Please confirm the master password: ")

    vault_file_path = utils.vault_path(utils.vault_file_name(vault_name, vault_password))

    try:
        with open(vault_file_path, "x") as file:
            file.write("-\n" + vault_name)
            file.write("\n" + h(vault_name))
            file.write("\n-")
            file.close()
    except FileExistsError:
        print("The vault already exists")
        exit(1)

    print("New vault created and saved as:", vault_name + VAULT_EXTENSION)


if __name__ == "__main__":
    create_vault()

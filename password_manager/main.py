from display_menu import display_menu

menu = {
    "title": "",
    "subtitle": "Welcome to SCC Password Manager",
    "description": "What would you like to do?",
    "items": [
        {
            "auth": False,
            "label": "Create a new password vault",
            "title": "Creating a new vault",
            "action": "create_vault",
            "keys": ["1"]
        },
        {
            "auth": False,
            "label": "Sign in to a password vault",
            "title": "Signing in",
            "action": "sign_in_to_vault",
            "keys": ["2"]
        },
        {
            "auth": True,
            "label": "Add a password to a vault",
            "title": "Adding password",
            "action": "add_password_to_vault",
            "keys": ["3"]
        },
        {
            "auth": True,
            "label": "Fetch a password from a vault",
            "title": "Fetching password",
            "action": "fetch_password_from_vault",
            "keys": ["4"]
        },
        {
            "auth": True,
            "label": "Update a password from a vault",
            "title": "Updating password",
            "action": "update_record_from_vault",
            "keys": ["5"]
        }
    ]
}


def main():
    try:
        display_menu(menu)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

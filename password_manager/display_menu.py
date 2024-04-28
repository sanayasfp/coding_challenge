import runpy

import utils


def display_menu(menu, transferred_params: dict = None):
    title, subtitle, description, items = menu.values()

    last_item = items[-1]

    if "quit" not in last_item["keys"]:
        last_item = {
            "label": "Quit (enter q or quit)",
            "action": "quit",
            "keys": ["q", "quit"]
        }

        items.append(last_item)

    if title:
        print(title)
    if subtitle:
        print(subtitle)
    if description:
        print(description)

    for index, item in enumerate(items):
        if index + 1 == len(items) and item["action"] == "quit":
            print(item["label"])
        else:
            print(f"{index + 1}. {item['label']}")

    key = input("Select an option: ").strip()

    display = True

    if key:
        res = list(filter(lambda x: str(key).lower() in x["keys"], items))

        if len(res) == 0:
            print("No such option")
        else:
            item = res[0]
            action = item["action"] if "action" in item else None
            title = item["title"] if "title" in item else None
            auth = item["auth"] if "auth" in item else False

            if not action:
                print("Invalid action")
            else:
                if auth and not utils.check_signed():
                    print("You are not signed in!")
                else:
                    if title:
                        n_dash = (len(title) + 4)
                        print("-" * n_dash)
                        print(title.center(n_dash))
                        print("-" * n_dash)

                    res = runpy.run_module(action, run_name="__main__",
                                           init_globals={"TRANSFERRED_PARAMS": transferred_params or {}})

                    if "TRANSFERRED_PARAMS" in res:
                        transferred_params = res["TRANSFERRED_PARAMS"]

                    if "DISPLAY_MENU" in res:
                        display = res["DISPLAY_MENU"]

    if display:
        print("\n")
        display_menu(menu, transferred_params)

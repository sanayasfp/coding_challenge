import os

from Crypto.Random import get_random_bytes
from dotenv import load_dotenv

load_dotenv()


def load_salt():
    if not os.getenv("SALT"):
        with open(".env", "x") as file:
            salt = get_random_bytes(32)
            salt_str = salt.hex()
            file.write("SALT=" + salt_str)
            file.close()

        load_dotenv()


def load_env():
    load_dotenv()

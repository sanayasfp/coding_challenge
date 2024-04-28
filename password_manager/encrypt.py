import os

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad

import env
from kdf import derive

env.load_salt()


def encrypt(password: str, message: str | bytes, salt: bytes | str = os.getenv("SALT")):
    salt = salt if isinstance(salt, bytes) else bytes.fromhex(salt)
    key = derive(password=password, salt=salt)
    message = message if isinstance(message, bytes) else message.encode()

    cipher = AES.new(key=key, mode=AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(message, AES.block_size))
    encrypted_text = cipher.iv + cipher_text

    return encrypted_text

import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

import env
from kdf import derive

env.load_salt()


def decrypt(password: str, encrypted_message: bytes, salt: bytes | str = os.getenv("SALT")):
    salt = salt if isinstance(salt, bytes) else bytes.fromhex(salt)
    key = derive(password=password, salt=salt)
    iv = encrypted_message[:16]
    decrypted_message = encrypted_message[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    original = unpad(cipher.decrypt(decrypted_message), AES.block_size)

    return original.decode('utf-8')

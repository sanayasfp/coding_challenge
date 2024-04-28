from Crypto.Protocol.KDF import PBKDF2


def derive(password: str, salt: bytes, dk_len: int = 32) -> bytes:
    return PBKDF2(password=password, salt=salt, dkLen=dk_len)

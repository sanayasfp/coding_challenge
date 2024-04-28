import hashlib


def h(*messages: bytes | str):
    hlib = hashlib.new("SHA256")

    for message in messages:
        message = message if isinstance(message, bytes) else message.encode()
        hlib.update(message)

    return hlib.hexdigest()


def compare(h_password, password):
    return h_password == h(password)

import os


def get_file(filepath: str, dictionary: dict={}) -> bytes:
    if not(os.path.exists(filepath) and os.path.isfile(filepath)):
        return None

    with open(filepath, 'rb') as f:
        data = f.read()

    # TODO Replace occurences of dictionary items with data,
    #      do some base template stuff etc.

    return data

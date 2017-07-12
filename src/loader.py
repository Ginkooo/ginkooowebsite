import os


def prepare_data(data: bytes) -> bytes:
    """prepare_data
    prepare data so it can be sent by http without errors

    :param data:
    :type data: bytes

    :rtype: bytes
    """
    data = data.replace(b'\r\n', b'\n')
    return data


def replace_occurences(data: bytes, dictionary: dict) -> bytes:
    # TODO replace that occurences
    return data


def get_file(filepath: str, dictionary: dict={}) -> bytes:
    """get_file
    get file contents as bytes and optionally replace occurences of
    dict key with dict value

    :param filepath:
    :type filepath: str
    :param dictionary:
    :type dictionary: dict

    :rtype: bytes
    """
    if not(os.path.exists(filepath) and os.path.isfile(filepath)):
        return None

    with open(filepath, 'rb') as f:
        data = f.read()

    # TODO Replace occurences of dictionary items with data,
    #      do some base template stuff etc.
    data = prepare_data(data)
    if dictionary:
        data = replace_occurences(data, dictionary)

    return data

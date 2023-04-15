import re


def __replace(input_str: str, pytokens: dict):
    for k, v in pytokens.items():
        input_str = re.sub("{{" + k + "}}", str(v), input_str)
    return input_str


def __json_replacer(pyinput, pytokens):
    if isinstance(pyinput, str):
        return __replace(pyinput, pytokens)

    if isinstance(pyinput, list):
        return [__json_replacer(v, pytokens) for v in pyinput]

    if isinstance(pyinput, dict):
        return {k: __json_replacer(v, pytokens) for k, v in pyinput.items()}

    return pyinput
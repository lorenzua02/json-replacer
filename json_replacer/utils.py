import re


def __replace(input_str: str, pytokens: dict):
    for k, v in pytokens.items():
        input_str = re.sub("{{" + k + "}}", str(v), input_str)
    return input_str


def __json_replacer(pyinput, pytokens: dict):
    # TODO DRY: code is doubled, code this part again
    if isinstance(pyinput, str):
        return __replace(pyinput, pytokens)

    if isinstance(pyinput, list):
        for i in range(len(pyinput)):
            pyinput[i] = __json_replacer(pyinput[i], pytokens)
            return

    if not isinstance(pyinput, dict):
        return pyinput

    res = {}
    # for x in itertools.chain.from_iterable(pyinput.keys()):  # "Flattens" the .keys() -> [k1, v1, k2, v2, ...]
    for k, v in pyinput.items():
        if isinstance(v, str):
            v = __replace(v, pytokens)

        if isinstance(v, list):
            for i in range(len(v)):
                v[i] = __json_replacer(v[i], pytokens)

        if isinstance(v, dict):
            v = __json_replacer(v, pytokens)

        res[k] = v

    return res

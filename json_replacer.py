import json
from utils import __json_replacer


def json_replacer(
        input_json: str | dict | list,
        tokens_json: str | dict,
        output_filename: str = None
) -> dict | list:
    """
    Excepts path of json file or python dict/list.

    Returns a python dict/list.
    If output_filename is filled, a json file will be saved too.
    """
    if isinstance(input_json, str):
        input_json = json.load(open(input_json))

    if isinstance(tokens_json, str):
        tokens_json = json.load(open(tokens_json))

    result = __json_replacer(input_json, tokens_json)

    if output_filename is not None:
        if not output_filename.endswith(".json"):
            output_filename += ".json"

        with open(output_filename, "w") as f:
            json.dump(result, f)
            # return

    return result

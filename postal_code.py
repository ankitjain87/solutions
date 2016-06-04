import re


def match(res):
    if res is None:
        return "Invalid"

    return "Valid"


def is_valid(code):
    pattern = re.compile(
        r"^[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}$")

    return match(pattern.match(code))


# is_valid(raw_input())

"""UK postal code validation."""

import re


def match(res):
    if res is None:
        return "Invalid"

    return "Valid"


def is_valid(code):
    pattern = re.compile(r"^[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW]) ?[0-9][ABD-HJLNP-UW-Z]{2}$")

    return match(pattern.match(code))


# print is_valid(raw_input())


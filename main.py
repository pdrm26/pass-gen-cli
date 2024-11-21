from random import choices
from string import digits, punctuation, ascii_lowercase, ascii_uppercase, printable


def create_password(length=8, digit=False, upper=False, lower=False, pun=False):
    available_characters = ""

    if digit:
        available_characters += digits

    if upper:
        available_characters += ascii_uppercase

    if lower:
        available_characters += ascii_lowercase

    if pun:
        available_characters += punctuation

    if not len(available_characters):
        available_characters += printable

    available_characters = available_characters.strip()

    return ''.join(choices(available_characters, k=length))


if __name__ == "__main__":
    print(create_password())
    print(create_password(12))
    print(create_password(upper=True))
    print(create_password(lower=True))
    print(create_password(upper=True, digit=True))
    print(create_password(130, lower=True, digit=True, pun=True))
    print(create_password(lower=False, digit=False, pun=False))

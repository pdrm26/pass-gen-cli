from random import choices
from string import digits, punctuation, ascii_lowercase, ascii_uppercase, printable
import argparse


def create_password(length=10, digit=False, upper=False, lower=False, pun=False):
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
    parser = argparse.ArgumentParser(
        prog='Password generator CLI',
        description="You can generate random password with any length you want with any characters you want.",
    )

    parser.add_argument('-c', '--length', type=int, default=10,
                        help="Specify the length of the password.")
    parser.add_argument('-d', '--digit', action='store_true',
                        help="Include digits (0-9) in the password.")
    parser.add_argument('-u', '--upper', action='store_true',
                        help="Include uppercase letters (A-Z) in the password.")
    parser.add_argument('-l', '--lower', action='store_true',
                        help="Include lowercase letters (a-z) in the password.")
    parser.add_argument('-p', '--punc', action='store_true',
                        help="Include punctuation/special characters in the password.")

    args = parser.parse_args()

    print(create_password(args.length, digit=args.digit,
          upper=args.upper, lower=args.lower, pun=args.punc))

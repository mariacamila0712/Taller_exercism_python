from string import ascii_lowercase


def is_pangram(input):
    input = input.lower()
    return all(c in input for c in ascii_lowercase)

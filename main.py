import json
from pprint import pprint

with open('words_dictionary.json') as f:
    data = json.load(f)


def possible(known: str) -> list:
    """
    returns the list of all possible words with the known letters
    :param known: reference check_word
    """
    known = convert(known)
    lst = []
    for row in data:
        if check_word(row, known):
            lst.append(row)
    return lst


def convert(string: str) -> list:
    """
    converts the string into a list to ease later functions
    :param string: string with _ when letter is unknown
    :return: converted list
    """
    lst = []
    c = 0
    for i in string:
        if i == '_':
            c += 1
        else:
            lst.append(c)
            lst.append(i)
            c = 0
    lst.append(c)
    return lst


def check_word(word: str, known: list) -> bool:
    """
    takes in a word and known positions of letters and indices and returns if it fits
    :param word: word
    :param known: length of at least 3, [0] is how much potential space before first fixed letter,
    [1] is first letter, [i + 1] where i is a letter is how much space between [i] and next letter
    (0 if right after), [-1] is potential space after last fixed
    """
    i = word.find(known[1])  # index in word
    if i == -1 or i > known[0]:  # word doesn't have first letter or prefix issues
        return False
    j = 1  # index in known
    while True:
        if word[i] != known[j]:
            return False

        i += known[j + 1] + 1  # fixed space
        j += 2  # next letter

        if j == len(known):  # check suffix
            if len(word) - i <= 0:
                return True
            else:
                return False

        if i > len(word) - 1:  # too short
            return False

import string
from collections import Counter

class Alphabet:
    @staticmethod
    def get_alphabet_dict():
        alphabet_dict = dict()
        for letter in string.ascii_letters:
            alphabet_dict[letter] = len(alphabet_dict)
        for letter in string.punctuation:
            alphabet_dict[letter] = len(alphabet_dict)
        return alphabet_dict
    @staticmethod
    def get_alphabet():
        alphabet = []
        for letter in string.ascii_letters:
            alphabet.append(letter)
        for letter in string.punctuation:
            alphabet.append(letter)
        return alphabet
    alphabet = get_alphabet.__func__()
    alphabet_dict = get_alphabet_dict.__func__()


def calc_difference(frequency1, frequency2):
    alphabet = Alphabet.alphabet
    dif = 0
    for letter in alphabet:
        dif += (frequency1[letter] - frequency2[letter]) ** 2
    return dif


def calc_frequency(text):
    alphabet = Alphabet.alphabet
    counter = Counter(text)
    amount = sum(counter[letter] for letter in alphabet)
    frequency = {}
    for letter in alphabet:
        frequency[letter] = counter[letter] / amount
    return frequency

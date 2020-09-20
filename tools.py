import string
from collections import Counter


class Alphabet:

    @staticmethod
    def get_alphabet():
        return string.ascii_letters + string.punctuation

    alphabet = get_alphabet.__func__()

    alphabet_dict = {letter: index for index, letter in enumerate(alphabet)}


def calc_difference(frequency1, frequency2):
    dif = 0
    for letter in Alphabet.alphabet:
        dif += (frequency1[letter] - frequency2[letter]) ** 2
    return dif


def calc_frequency(text):
    counter = Counter(text)
    amount = sum(counter[letter] for letter in Alphabet.alphabet)
    return {letter: counter[letter] / amount for letter in Alphabet.alphabet}


def shift_letter(letter, shift):
    return Alphabet.alphabet[(Alphabet.alphabet_dict[letter] + shift) % len(Alphabet.alphabet)]


def shift_frequency(frequencies, shift):
    return {shift_letter(letter, shift): frequency for letter, frequency in frequencies.items()}

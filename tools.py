import string


def get_alphabet():
    alphabet = []
    for letter in string.ascii_letters:
        alphabet.append(letter)
    for letter in string.punctuation:
        alphabet.append(letter)
    return alphabet


def calc_difference(freq1, freq2):
    alphabet = get_alphabet()
    dif = 0
    for letter in alphabet:
        dif += (freq1[letter] - freq2[letter]) ** 2
    return dif


def calc_frequency(text):
    alphabet = get_alphabet()
    amount = sum(text.count(letter) for letter in alphabet)
    frequency = {}
    for letter in alphabet:
        frequency[letter] = text.count(letter) / amount
    return frequency

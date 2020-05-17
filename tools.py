import string


def get_alphabet():
    alphabet = []
    for i in string.ascii_letters:
        alphabet.append(i)
    for i in string.punctuation:
        alphabet.append(i)
    return alphabet


def calc_difference(freq1, freq2):
    alphabet = get_alphabet()
    dif = 0
    for i in alphabet:
        dif += (freq1[i] - freq2[i]) ** 2
    return dif


def calc_frequency(text):
    alphabet = get_alphabet()
    amount = sum(text.count(i) for i in alphabet)
    frequency = {}
    for i in alphabet:
        frequency[i] = text.count(i) / amount
    return frequency

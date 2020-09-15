import tools


class Caesar:

    def __do(text, key, flag):
        alphabet = tools.Alphabet.alphabet
        alphabet_dict = tools.Alphabet.alphabet_dict
        key = int(key)
        newtext = ''
        for letter in text:
            if letter in alphabet_dict:
                ind = (alphabet_dict[letter] + flag * key) % len(alphabet)
                newtext += alphabet[ind]
            else:
                newtext += letter
        return newtext

    def decode(text, key):
        return Caesar.__do(text, key, -1)

    def encode(text, key):
        return Caesar.__do(text, key, 1)

    def hack(text, frequency):
        alphabet = tools.Alphabet.alphabet
        min_difference = len(text)
        ans_shift = -1
        for shift in range(len(alphabet)):
            newtext = Caesar.encode(text, shift)
            temp_freq = tools.calc_frequency(newtext)
            difference = tools.calc_difference(frequency, temp_freq)
            if difference <= min_difference:
                min_difference = difference
                ans_shift = shift
        return Caesar.encode(text, ans_shift)

import tools


class Caesar:

    def __do(text, key, flag):
        alphabet = tools.get_alphabet()
        key = int(key)
        newtext = ''
        for letter in text:
            if letter in alphabet:
                ind = (alphabet.index(letter) + flag * key) % len(alphabet)
                newtext += alphabet[ind]
            else:
                newtext += letter
        return newtext

    def decode(text, key):
        return Caesar.__do(text, key, -1)

    def encode(text, key):
        return Caesar.__do(text, key, 1)

    def hack(text, frequency):
        alphabet = tools.get_alphabet()
        min_d = len(text)
        ans_shift = -1
        for shift in range(len(alphabet)):
            newtext = Caesar.encode(text, shift)
            temp_freq = tools.calc_frequency(newtext)
            d = tools.calc_difference(frequency, temp_freq)
            if d <= min_d:
                min_d = d
                ans_shift = shift
        return Caesar.encode(text, ans_shift)
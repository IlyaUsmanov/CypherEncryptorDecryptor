from tools import Alphabet, calc_frequency, calc_difference, shift_frequency, shift_letter


class Caesar:

    @staticmethod
    def __do_encode_or_decode(text, key, flag):
        key = int(key)
        result = []
        for letter in text:
            if letter in Alphabet.alphabet_dict:
                result.append(shift_letter(letter, flag * key))
            else:
                result.append(letter)
        return ''.join(result)

    @classmethod
    def decode(cls, text, key):
        return cls.__do_encode_or_decode(text, key, -1)

    @classmethod
    def encode(cls, text, key):
        return cls.__do_encode_or_decode(text, key, 1)

    @classmethod
    def hack(cls, text, frequency):
        base_frequency = calc_frequency(text)
        min_difference = calc_difference(base_frequency, frequency)
        ans_shift = 0

        for shift in range(1, len(Alphabet.alphabet)):
            temp_freq = shift_frequency(base_frequency, shift)
            difference = calc_difference(frequency, temp_freq)
            if difference <= min_difference:
                min_difference = difference
                ans_shift = shift
        return cls.encode(text, ans_shift)

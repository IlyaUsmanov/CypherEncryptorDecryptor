from tools import Alphabet


class Vigenere:

    @staticmethod
    def __do_encode_or_decode(text, key, flag):
        result = []
        for index, letter in enumerate(text):
            if letter in Alphabet.alphabet_dict:
                key_ind = Alphabet.alphabet_dict[key[index % len(key)]]
                shift = Alphabet.alphabet_dict[letter] + flag * key_ind
                ind = shift % len(Alphabet.alphabet)
                result.append(Alphabet.alphabet[ind])
            else:
                result.append(letter)
        return ''.join(result)

    @classmethod
    def decode(cls, text, key):
        return Vigenere.__do_encode_or_decode(text, key, -1)

    @classmethod
    def encode(cls, text, key):
        return Vigenere.__do_encode_or_decode(text, key, 1)

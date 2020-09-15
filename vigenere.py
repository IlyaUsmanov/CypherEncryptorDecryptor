import tools


class Vigenere:

    def __do(text, key, flag):
        alphabet = tools.Alphabet.alphabet
        alphabet_dict = tools.Alphabet.alphabet_dict
        newtext = ''
        for i in range(len(text)):
            if text[i] in alphabet_dict:
                key_ind = alphabet_dict[key[i % len(key)]]
                shift = alphabet_dict[text[i]] + flag * key_ind
                ind = shift % len(alphabet)
                newtext += alphabet[ind]
            else:
                newtext += text[i]
        return newtext

    def decode(text, key):
        return Vigenere.__do(text, key, -1)

    def encode(text, key):
        return Vigenere.__do(text, key, 1)

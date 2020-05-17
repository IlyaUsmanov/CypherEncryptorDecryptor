import tools


class Vigenere:

    def __do(text, key, flag):
        alphabet = tools.get_alphabet()
        newtext = ''
        for i in range(len(text)):
            if text[i] in alphabet:
                key_ind = alphabet.index(key[i % len(key)])
                shift = alphabet.index(text[i]) + flag * key_ind
                ind = shift % len(alphabet)
                newtext += alphabet[ind]
            else:
                newtext += text[i]
        return newtext

    def decode(text, key):
        return Vigenere.__do(text, key, -1)

    def encode(text, key):
        return Vigenere.__do(text, key, 1)

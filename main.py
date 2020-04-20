import string
import json
import argparse
import sys


alph = []

def calc_difference(freq1, freq2):
    dif = 0
    for i in alph:
        dif += (freq1[i] - freq2[i]) ** 2
    return dif

def fill_alph():
    for i in string.ascii_letters:
        alph.append(i)
    for i in string.punctuation:
        alph.append(i)
    for i in range(1040, 1104):
        alph.append(chr(i))

def calc_frequency(text):
    amount = sum(text.count(i) for i in alph)
    frequency = {}
    for i in alph:
        frequency[i] = text.count(i) / amount
    return frequency
        
def code_caesar(text, key, flag):
    key = int(key)
    newtext = ''
    for i in text:
        if i in alph:
            ind = (alph.index(i) + flag * key) % len(alph)
            newtext += alph[ind]
        else:
            newtext += i
    return newtext

def decode_caesar(text, key):
    return code_caesar(text, key, -1)

def encode_caesar(text, key):
    return code_caesar(text, key, 1)

def code_vigenere(text, key, flag):
    newtext = ''
    for i in range(len(text)):
        if text[i] in alph:
            key_ind = alph.index(key[i % len(key)])
            ind = (alph.index(text[i]) + flag * key_ind) % len(alph)
            newtext += alph[ind]
        else:
            newtext += text[i]
    return newtext

def decode_vigenere(text, key):
    return code_vigenere(text, key, -1)       

def encode_vigenere(text, key):
    return code_vigenere(text, key, 1) 

def hack_caesar(text, frequency):
    min_d = 100000000
    ans_shift = -1
    for shift in range(len(alph)):
        newtext = encode_caesar(text, shift)
        temp_freq = calc_frequency(newtext)
        d = calc_difference(frequency, temp_freq)
        if d < min_d:
            min_d = d
            ans_shift = shift
    return encode_caesar(text, ans_shift)

parser = argparse.ArgumentParser()
parser.add_argument('mode')
parser.add_argument('--input_file')
parser.add_argument('--output_file')
parser.add_argument('--cipher')
parser.add_argument('--key')
parser.add_argument('--frequency_file')
args = parser.parse_args()

if not args.input_file:
    print('Enter your text')
    text = ''
    for i in sys.stdin:
        text += i
else:
    with open(args.input_file, 'r', encoding='utf-8') as f:
        text = f.read()

fill_alph()
if args.mode == 'frequency':
    result = calc_frequency(text)
    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f)
    else:
        print(result)
else:
    if args.mode in ('encode', 'decode'):
        result = eval(args.mode + '_' + args.cipher + '(text, args.key)')
    else:
        with open(args.frequency_file, 'r', encoding='utf-8') as f:
            frequency = json.load(f)
        result = eval(args.mode + '_' + args.cipher + '(text, frequency)')
    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            print(result, file=f, end = '')
    else:
        print(result, end = '')



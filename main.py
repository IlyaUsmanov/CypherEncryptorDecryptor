import string
import json
import argparse
import sys
from caesar import Caesar
from vigenere import Vigenere
import tools


def parse_input():
    parser = argparse.ArgumentParser(description='This project allow you to encode or decode ciphers')
    parser.add_argument('mode', help='one of four modes: encode/decode/frequency/hack')
    parser.add_argument('--input_file', help='your input file or nothing if you want to use console')
    parser.add_argument('--output_file', help='your output file or nothing if you want to use console')
    parser.add_argument('--cipher', help='one of two ciphers: caesar/vigenere')
    parser.add_argument('--key', help='key for encoding')
    parser.add_argument('--frequency_file', help='frequency file for hack caesar')
    args = parser.parse_args()

    if not args.input_file:
        print('Enter your text')
        text = sys.stdin.read()
    else:
        with open(args.input_file, 'r', encoding='utf-8') as input_file:
            text = input_file.read()

    return (args, text)


def create_output(args, text):
    if args.mode == 'frequency':
        result = tools.calc_frequency(text)
        if args.output_file:
            with open(args.output_file, 'w', encoding='utf-8') as output_file:
                json.dump(result, output_file)
        else:
            print(result)
    else:
        if args.mode == 'encode':
            if args.cipher == 'caesar':
                result = Caesar.encode(text, args.key)
            else:
                result = Vigenere.encode(text, args.key)
        elif args.mode == 'decode':
            if args.cipher == 'caesar':
                result = Caesar.decode(text, args.key)
            else:
                result = Vigenere.decode(text, args.key)
        else:
            with open(args.frequency_file, 'r', encoding='utf-8') as frequency_file:
                frequency = json.load(frequency_file)
            result = Caesar.hack(text, frequency)

        if args.output_file:
            with open(args.output_file, 'w', encoding='utf-8') as output_file:
                print(result, file=output_file, end='')
        else:
            print(result, end='')


def main():
    args, text = parse_input()
    create_output(args, text)


if __name__ == '__main__':
    main()

import string
import json
import argparse
import sys
import caesar
import vigenere
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
        text = ''
        for i in sys.stdin:
            text += i
    else:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            text = f.read()

    return (args, text)


def create_output(args, text):
    if args.mode == 'frequency':
        result = tools.calc_frequency(text)
        if args.output_file:
            with open(args.output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f)
        else:
            print(result)
    else:
        function = '.'.join([args.cipher, args.cipher.capitalize(), args.mode])
        if args.mode in ('encode', 'decode'):
            result = eval(function + '(text, args.key)')
        else:
            with open(args.frequency_file, 'r', encoding='utf-8') as f:
                frequency = json.load(f)
            result = eval(function + '(text, frequency)')
        if args.output_file:
            with open(args.output_file, 'w', encoding='utf-8') as f:
                print(result, file=f, end='')
        else:
            print(result, end='')


def main():
    args, text = parse_input()
    create_output(args, text)


if __name__ == '__main__':
    main()

import os
import sys
import random
import re
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def check_file():
    input_file = sys.argv[1]
    if os.path.isfile(input_file):
        if input_file.endswith('.txt'):
            message_to_decrypt = open(input_file)
            message = message_to_decrypt.read()
            print("File found and of correct file type.")
            print("\nMessage to Decrypt:\n" + message)
            return message

        else:
            print("Incorrect file type.")
            print(input_file)
    else:
        print("File not found in the current working directory.")


message = check_file()


def decrypt_message(key, cipher):
    de_translated = ''
    charsA = LETTERS
    charsB = key
    for symbol in cipher:
        if symbol.upper() in charsB:
            symIndex = charsB.find(symbol.upper())
            if symbol.isupper():
                de_translated += charsA[symIndex].upper()
            else:
                de_translated += charsA[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            de_translated += symbol

    print(de_translated)





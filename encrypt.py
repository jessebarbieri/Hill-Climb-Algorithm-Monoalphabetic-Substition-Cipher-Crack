import sys
import os

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    myMessage = "Congress had multiple advantages if the rebellion turned into a protracted war. Their prosperous state populations depended on local production for food and supplies rather than on imports from their mother country that lay six to twelve weeks away by sail. They were spread across most of the North American Atlantic seaboard, stretching 1,000 miles. Most farms were remote from the seaports, and controlling four or five major ports did not give British armies control over the inland areas. Each state had established internal distribution systems."
    myKey = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    checkValidKey(myKey)
    translated = encryptMessage(myKey, myMessage)
    encrypted_file = open(os.path.join(os.getcwd(), 'file.txt'), 'w')
    encrypted_file.write(translated)
    encrypted_file.close()
    decrypt_message(myKey, cipher=encryptMessage(myKey, myMessage))
    ##print(translated)


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('This is not a valid monoalphabetic substitution cipher key!')


def encryptMessage(key, message):
    translated = ''
    charsA = LETTERS
    charsB = key
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol
    return translated


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


if __name__ == "__main__":
    main()

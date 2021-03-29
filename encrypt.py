import sys
import os

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    myMessage = "According to Wikipedia, in cryptography, a substitution cipher is a method of encrypting by which units of plaintext are replaced with ciphertext, according to a fixed system; the 'units' may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth. The receiver deciphers the text by performing the inverse substitution. A simple substitution is the substitution of single letters separately. The substitution key is usually represented by writing out the alphabet in some order. The Caesar cipher is a form of a simple substitution cipher. For example, its ROT2 key can be presented as CDEFGHIJKLMNOPQRSTUVWXYZAB. This means that A is replaced with C, B with D, and so on. The number of all possible keys for a simple substitution cipher is a factorial of 26 (26!). However, you can break it if you have enough ciphered text by using frequency analysis or the stochastic optimization algorithm (check out our Substitution cipher breaker). The cipher does not change language letter frequencies (it is said to be monoalphabetic), unlike, for example, the polyalphabetic Vigenère cipher, so it is considered to be rather weak. Paste text into the field, fill the key, choose 'encode' if you have pasted clear text or 'decode' if you have pasted ciphered text, and press 'Calculate'. Traditionally, punctuation and spaces are removed to disguise word boundaries and text is written in blocks of letters, usually five. This option is supported for encoding as well."
    myKey = 'CDEFGHIJKLMNOPQRSTUVWXYZAB'
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

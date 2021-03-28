import os
import sys
import random
import re
from ngram import ngram

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fitness = ngram()


def check_file():
    input_file = sys.argv[1]
    if os.path.isfile(input_file):
        if input_file.endswith('.txt'):
            message_to_decrypt = open(input_file)
            message = message_to_decrypt.read()
            ##print("File found and of correct file type.")
            ##print("\nMessage to Decrypt:\n" + message)
            return message

        else:
            print("Incorrect file type.")
            print(input_file)
    else:
        print("File not found in the current working directory.")


message = check_file()

solutions = {}


def hill_climb_algorithm():
    key_max = list(LETTERS)
    max_score = -99e9
    parentscore, parentkey = max_score, key_max[:]

    iterations = 0
    count = 0
    while iterations < 3:
        random.shuffle(parentkey)  # randomly generate a key
        #print(parentkey)
        deciphered = re.sub('[^A-Za-z0-9]+', '', decrypt_message(''.join(parentkey), message).upper())
        #print(deciphered)
        #print(len(deciphered))
        parentscore = fitness.score(deciphered)

        while count < 3000:
            a = random.randint(0, 25)
            b = random.randint(0, 25)
            child = parentkey[:]

            child[a], child[b] = child[b], child[a]
            deciphered = re.sub('[^A-Za-z0-9]+', '', decrypt_message(''.join(child), message).upper())
            score = fitness.score(deciphered)

            if score > parentscore:
                parentscore = score
                parentkey = child[:]
                count = 0
            count += 1

        if parentscore > max_score:
            max_score, key_max = parentscore, parentkey[:]
            ##print("\nBest Score: " + max_score + " on iteration: " + i)
            ##print("\nBest Key: " + "".join(key_max) + " Score: " + str(max_score) + " Iteration: " + str(iterations))
            solutions.update({"".join(key_max): max_score})

        count = 0
        iterations += 1

    return solutions


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

    ##print(de_translated)
    return de_translated

solutions = hill_climb_algorithm()
best_key = max(solutions.keys(), key=(lambda k: solutions[k]))
#print("The best possible key is: \n" + best_key)

key_file = open(os.path.join(os.getcwd(), 'key.txt'), 'w')
key_file.write(best_key)
key_file.close()

# 1. Remove spaces from encrypted
# 2. Remove spaces and non-letters from the decrypted

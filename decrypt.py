import os
import sys
import random
import re
from math import log10

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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


def create_ngram():
    ngram_dict = {}
    for line in open('english_trigrams.txt'):
        key, count, = line.split()
        ngram_dict[key] = int(count)
    length = len(key)
    sum_val = sum(ngram_dict.values())

    for key in ngram_dict.keys():
        ngram_dict[key] = log10(float(ngram_dict[key]) / sum_val)

    floor = log10(0.01 / sum_val)
    return floor, ngram_dict, length


ngram_floor, dict_ngram, length = create_ngram()


def ngram_score(decrypted, ngram_floor, dict_ngram, length):
    score = 0
    for i in range(len(decrypted) - length + 1):
        if decrypted[i:i + length] in dict_ngram:
            score += dict_ngram.get(decrypted[i:i + length])
        else:
            score += ngram_floor

    return score


def hill_climb_algorithm():
    key_max = list(LETTERS)
    max_score = -99e9
    parentscore, parentkey = max_score, key_max[:]

    iterations = 0
    count = 0
    while iterations < 8:
        random.shuffle(parentkey)  # randomly generate a key
        deciphered = re.sub('[^A-Za-z0-9]+', '', decrypt_message(''.join(parentkey), message).upper())
        print(len(deciphered))
        parentscore = ngram_score(deciphered, ngram_floor, dict_ngram, length)

        while count < 5000:
            a = random.randint(0, 25)
            b = random.randint(0, 25)
            child = parentkey[:]

            child[a], child[b] = child[b], child[a]
            deciphered = re.sub('[^A-Za-z0-9]+', '', decrypt_message(''.join(child), message).upper())
            score = ngram_score(deciphered, ngram_floor, dict_ngram, length)

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

    return de_translated


solutions = hill_climb_algorithm()
print(solutions)
best_key = max(solutions.keys(), key=(lambda k: solutions[k]))

key_file = open(os.path.join(os.getcwd(), 'key.txt'), 'w')
key_file.write(best_key)
key_file.close()

print(decrypt_message(best_key, message))

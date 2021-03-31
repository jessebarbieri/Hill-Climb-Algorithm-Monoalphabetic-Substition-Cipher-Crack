import os
import sys
import random
import re
from math import log10

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Checks if our file is valid for decryption
def check_file():
    input_file = sys.argv[1]
    if os.path.isfile(input_file):
        if input_file.endswith('.txt'):
            message_to_decrypt = open(input_file)
            message = message_to_decrypt.read()
            return message

        else:
            print("Incorrect file type -- files must been of type 'filename.txt'.")
            sys.exit()
    else:
        print("File not found in the current working directory.")
        sys.exit()

# Creates our ngram dictionary for decryption comparison
def create_ngram():
    ngram_dict = {}
    for line in open('Data/english_trigrams.txt'):
        trigram, trigram_score, = line.split()
        ngram_dict[trigram] = int(trigram_score)
    key_length = 3
    sum_val = sum(ngram_dict.values())

    for trigram in ngram_dict.keys():
        ngram_dict[trigram] = log10(float(ngram_dict[trigram]) / sum_val)

    floor = log10(0.01 / sum_val)
    return floor, ngram_dict, key_length

# Returns the score of found matches of decryption against our ngram dictionary
def ngram_score(d_attempt, floor, ngram, l_key):
    score = 0
    for i in range(len(d_attempt) - l_key + 1):
        if d_attempt[i:i + l_key] in ngram:
            score += ngram.get(d_attempt[i:i + l_key])
        else:
            score += floor

    return score

# Runs the hill climb algorithm until best possible global maximum is found (within 8 iterations)
def hill_climb_algorithm():
    print("Cracking the code...")
    key_max = list(LETTERS)
    max_score = -99e9
    original_score, original_key = max_score, key_max[:]

    iterations = 0
    count = 0
    while iterations < 8:
        random.shuffle(original_key)  # randomly generates a key per iteration
        deciphered = re.sub('[^A-Za-z0-9]+', '', decrypt_message(''.join(original_key), message).upper())
        print("Iteration: " + str(iterations + 1) + "/8")
        #print(len(deciphered))
        original_score = ngram_score(deciphered, ngram_floor, dict_ngram, length)

        while count < 5000:
            a = random.randint(0, 25)
            b = random.randint(0, 25)
            swapped_key = original_key[:]

            swapped_key[a], swapped_key[b] = swapped_key[b], swapped_key[a]
            deciphered = re.sub('[^A-Za-z0-9]+', '', decrypt_message(''.join(swapped_key), message).upper())
            score = ngram_score(deciphered, ngram_floor, dict_ngram, length)

            if score > original_score:
                original_score = score
                original_key = swapped_key[:]
                count = 0
            count += 1

        if original_score > max_score:
            max_score, key_max = original_score, original_key[:]
            solutions.update({"".join(key_max): max_score})

        count = 0
        iterations += 1

    return solutions

# Print out of cryption, based on the original encryption provided by the professor
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
            de_translated += symbol

    return de_translated

# Set our values and variables and run the algorithm
ngram_floor, dict_ngram, length = create_ngram()
message = check_file()
solutions = {}
solutions = hill_climb_algorithm()
# Obtain the global maximum from our solutions dictionary
best_key = max(solutions.keys(), key=(lambda k: solutions[k]))

# Write our key to file
key_file = open(os.path.join(os.getcwd(), 'key.txt'), 'w')
key_file.write(best_key)
key_file.close()

# Show the decryption to user
#print(decrypt_message(best_key, message))

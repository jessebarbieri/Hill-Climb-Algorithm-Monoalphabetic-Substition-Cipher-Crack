import sys
import os

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    myMessage = "Aware it would be easier to enter the United States from Canada,[26] Musk applied for a Canadian passport through his Canadian-born mother.[27][28] While awaiting the documentation, he attended the University of Pretoria for five months; this allowed Musk to avoid mandatory service in the South African military.[29] Arriving in Canada in June 1989, Musk failed to locate his great-uncle in Montreal and instead stayed at a youth hostel. He then traveled west to live with a second-cousin in Saskatchewan.[30] He stayed there for a year, working odd jobs at a farm and lumber-mill.[31] In 1990, Musk entered Queen's University in Kingston, Ontario.[32][33] Two years later, he transferred to the University of Pennsylvania; he graduated in 1997 with a Bachelor of Science (BS) degree in economics from the Wharton School and a Bachelor of Arts (BA) degree in physics.[34][35][36] In 1994, Musk held two internships in Silicon Valley during the summer: at an energy storage startup called Pinnacle Research Institute, which researched electrolytic ultracapacitors for energy storage, and at the Palo Alto-based startup Rocket Science Games.[37] In 1995, Musk was accepted to a Ph.D. program in energy physics/materials science at Stanford University in California.[38] Musk attempted to get a job at Netscape but never received a response to his inquiries.[27] He dropped out of Stanford after two days, deciding instead to join the Internet boom and launch an Internet startup.[39]"
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

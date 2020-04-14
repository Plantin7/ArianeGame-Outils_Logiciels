import os
import sys
import time

alphabet = {}


# -------------------------------------- Alphabet --------------------------------------------------- #
def info_letter(array):
    longest_line = 0
    for line in array:
        if longest_line < len(line.strip("\n")):
            longest_line = len(line.strip("\n"))

    letter = [[" " for _ in range(longest_line)] for _ in range(8)]

    for i, line, in enumerate(array):
        for j, c in enumerate(line.strip('\n')):
            letter[i][j] = c

    for idx, line in enumerate(letter):
        letter[idx] = ''.join(line)

    return letter


def extract_ascii(file):
    with open(file, "r") as fp:
        tmp = []
        ext = []
        for i, line in enumerate(fp, 1):
            tmp.append(line)
            if i % 8 == 0:
                ext.append(info_letter(tmp))
                tmp = []
    return ext


def extract_alphabet_ascii():
    ext = extract_ascii("alphabet.txt")
    split = [ext[x:x + 26] for x in range(0, len(ext), 26)]  # split list into two list
    uppercase(split[0])
    lowercase(split[1])


def extract_numbers_ascii():
    ext = extract_ascii("chiffres.txt")
    numbers(ext)


def extract_symbols_ascii():
    ext = extract_ascii("symbols.txt")
    symbols(ext)


def uppercase(uppsercase_alphabet):
    for i, letter in enumerate(uppsercase_alphabet):
        x = chr(ord('A') + i)
        alphabet[x] = letter


def lowercase(lowercase_alphabet):
    for i, letter in enumerate(lowercase_alphabet):
        x = chr(ord('a') + i)
        alphabet[x] = letter


def numbers(numbers):
    for i, number in enumerate(numbers):
        x = chr(ord('0') + i)
        alphabet[x] = number


def symbols(symbols):
    arr = [",", ";", ":", "!", "?", ".", "/", "\"", "'", "(", "-", ")", "[", "|", "]", " "]
    for i, sb in enumerate(symbols):
        alphabet[arr[i]] = sb


# -------------------------------------- Alphabet --------------------------------------------------- #

def print_string(string):
    for j in range(8):
        for letter in string:
            if letter in alphabet:
                print(alphabet[letter][j], end="")
            else:
                print("Error : Letter Unknown !")
                sys.exit(1)
        print("")


def splitString(string, x=80):
    length, nb = anotherComputeStringLenght(string, x)
    if length < x:
        return [string]
    else:
        res_first, res_second = string[:nb], string[nb:]
        return [res_first.strip()] + splitString(res_second.strip(), x)


def computeStringLenght(string, x):
    length = 0
    nbLetter = 0
    for letter in string:
        length += len(alphabet[letter][0])
        if length < x:
            nbLetter += 1
    return length, nbLetter


def anotherComputeStringLenght(string, x):
    length = 0
    nbLetter = 0
    if len(string.split()) == 1:
        return computeStringLenght(string, x)
    else:
        for word in string.split():
            tmpLength, nb = computeStringLenght(word, x)
            if tmpLength + len(alphabet[" "][0]) < x:
                length += tmpLength + len(alphabet[" "][0])
                if length < x:
                    nbLetter += nb + 1
                else:
                    return length, nbLetter
            else:
                tmpLength
                return computeStringLenght(string, x)
    return length, nbLetter


if __name__ == '__main__':
    extract_alphabet_ascii()
    extract_numbers_ascii()
    extract_symbols_ascii()
    if len(sys.argv) != 2:
        print("File missing !")
        sys.exit(1)
    file = open(sys.argv[1], "r")
    txt = "".join(file.readlines())
    arr = splitString(txt.replace('\n', ''))

    for string in arr:
        print_string(string)

    '''    
    while True:
        txt = input("Type something to test this out: ")
        arr = test(txt)
        print("")
        for string in arr:
            print_string(string)'''

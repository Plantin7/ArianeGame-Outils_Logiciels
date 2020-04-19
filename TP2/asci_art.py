import sys

alphabet = {}


# -------------------------------------- Alphabet --------------------------------------------------- #
def info_letter(array):
    longest_line = 0
    # get the longest line for a letter
    for line in array:
        if longest_line < len(line.strip("\n")):
            longest_line = len(line.strip("\n"))

    # create an array of array with the longuest line
    letter = [[" " for _ in range(longest_line)] for _ in range(8)]

    # fill my array of array
    for i, line, in enumerate(array):
        for j, c in enumerate(line.strip('\n')):
            letter[i][j] = c

    # Reduce the array of array of character to array of string
    for i, line in enumerate(letter):
        letter[i] = ''.join(line)

    return letter


def extract_ascii(fileToExtract):
    with open(fileToExtract, "r") as fp:
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


def uppercase(uppercase_alphabet):
    for i, letter in enumerate(uppercase_alphabet):
        x = chr(ord('A') + i)
        alphabet[x] = letter


def lowercase(lowercase_alphabet):
    for i, letter in enumerate(lowercase_alphabet):
        x = chr(ord('a') + i)
        alphabet[x] = letter


def numbers(nb):
    for i, number in enumerate(nb):
        x = chr(ord('0') + i)
        alphabet[x] = number


def symbols(sym):
    array = [",", ";", ":", "!", "?", ".", "/", "\"", "'", "(", "-", ")", "[", "|", "]", " "]
    for i, sb in enumerate(sym):
        alphabet[array[i]] = sb


# -------------------------------------- Alphabet --------------------------------------------------- #

def print_string(st):
    for j in range(8):
        for letter in st:
            if letter in alphabet:
                print(alphabet[letter][j], end="")
            else:
                print("########", end="")
        print("")


def splitString(st, x=80):
    length, nb = getNumberOfStringToPrint(st, x)
    if length < x:
        return [st]
    else:
        res_first, res_second = st[:nb], st[nb:]
        return [res_first.strip()] + splitString(res_second.strip(), x)


def computeStringLenght(st, x):
    length = 0
    nbLetter = 0
    for letter in st:
        if letter in alphabet:
            length += len(alphabet[letter][0])
            if length < x:
                nbLetter += 1
        else:
            length += 8
            if length < x:
                nbLetter += 1
    return length, nbLetter


def getNumberOfStringToPrint(st, x):
    length = 0
    nbLetter = 0
    if len(st.split()) == 1:
        return computeStringLenght(st, x)
    else:
        for word in st.split():
            tmpLength, nb = computeStringLenght(word, x)
            if tmpLength + len(alphabet[" "][0]) < x:
                length += tmpLength + len(alphabet[" "][0])
                if length < x:
                    nbLetter += nb + 1
                else:
                    return length, nbLetter
            else:
                return computeStringLenght(st, x)
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

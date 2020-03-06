import os
import pickle
import sys
import numpy as np


def distance1(st1, st2):
    if len(st1) < len(st2):
        return distance1(st2, st1)

    if len(st2) == 0:
        return len(st1)

    # We call tuple() to force strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    st1 = np.array(tuple(st1))
    st2 = np.array(tuple(st2))

    # We use a dynamic programming algorithm, but with the
    # added optimization that we only need the last two rows
    # of the matrix.
    previous_row = np.arange(st2.size + 1)
    for s in st1:
        # Insertion (st2 grows longer than st1):
        current_row = previous_row + 1

        # Substitution or matching:
        # Target and st1 items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = np.minimum(
            current_row[1:],
            np.add(previous_row[:-1], st2 != s))

        # Deletion (st2 grows shorter than st1):
        current_row[1:] = np.minimum(
            current_row[1:],
            current_row[0:-1] + 1)

        previous_row = current_row

    return previous_row[-1]


def createFile():
    if not os.path.exists('dictionary.txt'):
        f = open('dictionary.txt', 'w+')
        f.close()


def save_obj(obj):
    with open('dictionary.txt', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj():
    createFile()
    if os.path.getsize('dictionary.txt') > 0:
        with open('dictionary.txt', 'rb') as f:
            return pickle.load(f)
    return {}


distance2_memory = load_obj()


def distance2(string1, string2):
    key = (string1, string2)
    if key in distance2_memory:
        return distance2_memory[key]
    else:
        d = distance1(string1, string2)
        distance2_memory[key] = d
        distance2_memory[(string2, string1)] = d
        return d


def plusProche(string, possibilities):
    string_close = []
    small_distance = sys.maxsize
    for st in possibilities:
        d = distance2(string, st)
        if d == small_distance:
            string_close.append(st)
        elif d < small_distance:
            small_distance = d
            string_close.clear()
            string_close.append(st)
    save_obj(distance2_memory)
    return string_close


if __name__ == '__main__':
    print("[DEBUG] - distance1(abracadabra, macabre)  = " + str(distance1("abracadabra", "macabre")))
    print("[DEBUG] - distance1(macabre, abracadabra)  = " + str(distance1("macabre", "abracadabra")))
    print("[DEBUG] - distance1(, macabre)             = " + str(distance1("", "macabre")))
    print("[DEBUG] - distance1(macabre, )             = " + str(distance1("macabre", "")))
    print("[DEBUG] - distance1(chiens, niche)         = " + str(distance1("chiens", "niche")))
    print("[DEBUG] - distance1(examen, examen)        = " + str(distance1("examen", "examen")))
    print("[DEBUG] - distance1(examen, examan)        = " + str(distance1("examen", "examan")))
    print("[DEBUG] - distance1(plage, bravo)          = " + str(distance1("plage", "bravo")))
    print("-----------------------------------------------------------------------------------------")
    print("[DEBUG] - distance2(abracadabra, macabre)  = " + str(distance2("abracadabra", "macabre")))
    print("[DEBUG] - distance2(macabre, abracadabra)  = " + str(distance2("macabre", "abracadabra")))
    print("[DEBUG] - distance2(plage, bravo)          = " + str(distance2("plage", "bravo")))
    print("[DEBUG] - distance2(bravo, plage)          = " + str(distance2("bravo", "plage")))
    print("-----------------------------------------------------------------------------------------")
    array = ["Tomme", "Forme", "Rome", "Gomme", "Homme", "Tomat", "Tamate", "tomate",
             "Pomme", "total", "ragout", "chantier", "Rouge", "Test", "Banane"]
    print("[DEBUG] - Le(s) mot(s) le(s) plus proche(s) du mot << Tomate >> : " + str(plusProche("Tomate", array)))
    print("[DEBUG] - (Après memoisation) Le(s) mot(s) le(s) plus proche(s) du mot << Tomate >> : " + str(
        plusProche("Tomate", array)))

'''
- 4 Après memoisation, le mot le plus proche est trouvé instantanément. Alors que le premier passage met un peu de temps.

'''

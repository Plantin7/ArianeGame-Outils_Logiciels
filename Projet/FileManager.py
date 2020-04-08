import sys


def chargeLabyrinth(file):
    """
    Charge la map du labyrinthe depuis le fichier nom.txt
    :param file: nom du fichier contenant la map du labyrinthe (avec l'extension .txt)
    :return: Les données du labynrinthe dans une liste, le nombre de cellule, la position des personnages
    """
    try:
        file = open(file, "r")
        size = 2 * int(file.readline().rstrip('\n\r')) + 1
        data = file.read().splitlines()
        laby = [[0 for _ in range(size)] for _ in range(size)]
        posObject = {}
        for i, line in enumerate(data):
            for j, car in enumerate(line):
                if car == "|" or car == "-" or car == "+":
                    laby[i][j] = 1
                elif car == "A" or car == "T" or car == "P":
                    posObject[car] = [i, j]
                elif car == "V" or car == "H":
                    if car in posObject:
                        posObject[car] = [i, j]
                    else:
                        posObject[car] = [[i, j]]
        file.close()
    except IOError:
        print("[ERROR] - Le fichier ({}) n'a pas pu etre chargé".format(file))
        sys.exit(1)
    return laby, size, posObject

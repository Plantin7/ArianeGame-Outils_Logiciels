def readFile(file):
    f = open(file, 'r')
    x = f.read().splitlines()
    f.close()
    return x


if __name__ == '__main__':
    import Exercice2 as ex

    series = readFile("series_2000-2019.txt")
    print("Hero -> titre suggéré pour Hero       :  " + str(ex.plusProche("Hero", series)))
    print("SOS -> titre suggéré pour SOS         :  " + str(ex.plusProche("SOS", series)))
    print("Chambre -> titre suggéré pour Chambre :  " + str(ex.plusProche("Chambre", series)))
    print("Journal -> titre suggéré pour Journal :  " + str(ex.plusProche("Journal", series)))
    print("Monstre -> titre suggéré pour Monstre :  " + str(ex.plusProche("Monstre", series)))


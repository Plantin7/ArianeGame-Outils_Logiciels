
if __name__ == '__main__':
    import FileManager as fd
    map = []

    level = open("maps/labyrinthe1.txt")
    try:
        size = fd.parsingHeaderLevel(level)
        map = [[0 for _ in range(size)] for _ in range(size)]
        print(map)
        fd.parsingMapLevel(level)
    finally:
        level.close()

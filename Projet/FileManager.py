class FileManager:
    """Class parsing file"""


def parsingLineLevel(level):
    return level.readline().rstrip('\n\r')


def parsingHeaderLevel(level):
    """
    :param level: to know the size of the map
    :return: the size of the map
    """
    levelSize = parsingLineLevel(level)
    return int(levelSize)


def parsingMapLevel(level):
    tests = parsingLineLevel(level)
    print(tests)

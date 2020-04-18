import copy


class Engine:

    def __init__(self, laby, posElements):
        self.laby = laby
        self.posElements = copy.deepcopy(posElements)
        self.arianePos = posElements.get("A")
        self.theseePos = posElements.get("T")
        self.minotorHPos = posElements.get("H")
        self.minotorVPos = posElements.get("V")
        self.doorPos = posElements.get("P")
        self.save = []
        self.registerElements()
        self.currentConf = (tuple(self.arianePos),
                            tuple(self.theseePos),
                            tuple(tuple(x) for x in self.minotorVPos),
                            tuple(tuple(x) for x in self.minotorHPos))

    # ----------------------------- Player Move ----------------------------------- #
    def checkPlayerMove(self, x, y):
        if self.laby[x][y] == 1:
            return False
        elif self.checkCollisionVMinotor([x, y]) or self.checkCollisionHMinotor([x, y]):
            return False
        return True

    def updatePlayerMove(self, keyName):
        x = self.arianePos[0]
        y = self.arianePos[1]
        if keyName == 'Up':
            if self.checkPlayerMove(x - 1, y) and self.checkPlayerMove(x - 2, y):
                self.arianePos[0] = x - 2
                return True
        elif keyName == 'Down':
            if self.checkPlayerMove(x + 1, y) and self.checkPlayerMove(x + 2, y):
                self.arianePos[0] = x + 2
                return True
        elif keyName == 'Left':
            if self.checkPlayerMove(x, y - 1) and self.checkPlayerMove(x, y - 2):
                self.arianePos[1] = y - 2
                return True
        elif keyName == 'Right':
            if self.checkPlayerMove(x, y + 1) and self.checkPlayerMove(x, y + 2):
                self.arianePos[1] = y + 2
                return True

        elif keyName == 'r':
            if len(self.save) - 1 > 0:
                del self.save[-1]
                idx = len(self.save) - 1
                self.arianePos[0] = self.save[idx][0][0]
                self.arianePos[1] = self.save[idx][0][1]
                self.theseePos[0] = self.save[idx][1][0]
                self.theseePos[1] = self.save[idx][1][1]
                for i, mv in enumerate(self.save[idx][2]):
                    self.minotorVPos[i][0] = mv[0]
                    self.minotorVPos[i][1] = mv[1]
                for i, mh in enumerate(self.save[idx][3]):
                    self.minotorHPos[i][0] = mh[0]
                    self.minotorHPos[i][1] = mh[1]
        return False

    def registerElements(self):
        ariane = [self.arianePos[0], self.arianePos[1]]
        thesee = [self.theseePos[0], self.theseePos[1]]
        minotorV = []
        minotorH = []
        for mv in self.minotorVPos:
            minotorV.append([mv[0], mv[1]])
        for mh in self.minotorHPos:
            minotorH.append([mh[0], mh[1]])

        self.save.append([ariane, thesee, minotorV, minotorH])

    # ----------------------------- Player Move ----------------------------------- #

    # ------------------------------- IA Move ------------------------------------- #
    def updateTheseeMove(self):
        if self.checkTheseeMove():
            self.theseePos[0] = self.arianePos[0]
            self.theseePos[1] = self.arianePos[1]

    def checkTheseeMove(self):
        tx, ty = self.theseePos
        ax, ay = self.arianePos

        if self.checkPlayerMove(tx, ty - 1) and self.checkPlayerMove(tx, ty - 2) and ax == tx and ay == ty - 2:
            return True
        elif self.checkPlayerMove(tx, ty + 1) and self.checkPlayerMove(tx, ty + 2) and ax == tx and ay == ty + 2:
            return True
        elif self.checkPlayerMove(tx + 1, ty) and self.checkPlayerMove(tx + 2, ty) and ax == tx + 2 and ay == ty:
            return True
        elif self.checkPlayerMove(tx - 1, ty) and self.checkPlayerMove(tx - 2, ty) and ax == tx - 2 and ay == ty:
            return True
        return False

    # ------------------------------- IA Move ------------------------------------- #
    # -------------------------- Minotors  Move ---------------------------------- #
    def updateMinotorsVMove(self):
        for mv in self.minotorVPos:
            self.updateMinotorVMove(mv)

    def updateMinotorsHMove(self):
        for mh in self.minotorHPos:
            self.updateMinotorHMove(mh)

    def updateMinotorVMove(self, mv):
        diff = self.arianePos[0] - mv[0]
        if diff < 0:
            self.fastestLeftVMinotorMove(mv)
        elif diff > 0:
            self.fastestRightVMinotorMove(mv)
        else:
            diff = self.arianePos[1] - mv[1]
            if diff < 0:
                self.fastestUpHMinotorMove(mv)
            elif diff > 0:
                self.fastestDownHMinotorMove(mv)

    def updateMinotorHMove(self, mh):
        diff = self.arianePos[1] - mh[1]
        if diff < 0:
            self.fastestUpHMinotorMove(mh)
        elif diff > 0:
            self.fastestDownHMinotorMove(mh)
        else:
            diff = self.arianePos[0] - mh[0]
            if diff < 0:
                self.fastestLeftVMinotorMove(mh)
            elif diff > 0:
                self.fastestRightVMinotorMove(mh)

    def fastestLeftVMinotorMove(self, minotor):
        x, y = minotor
        while self.checkMinotorMove(x - 1, y) and self.checkMinotorMove(x - 2, y) and self.arianePos[0] != x:
            minotor[0] = x - 2
            x = x - 2

    def fastestRightVMinotorMove(self, minotor):
        x, y = minotor
        while self.checkMinotorMove(x + 1, y) and self.checkMinotorMove(x + 2, y) and self.arianePos[0] != x:
            minotor[0] = x + 2
            x = x + 2

    def fastestUpHMinotorMove(self, minotor):
        x, y = minotor
        while self.checkMinotorMove(x, y - 1) and self.checkMinotorMove(x, y - 2) and self.arianePos[1] != y:
            minotor[1] = y - 2
            y = y - 2

    def fastestDownHMinotorMove(self, minotor):
        x, y = minotor
        while self.checkMinotorMove(x, y + 1) and self.checkMinotorMove(x, y + 2) and self.arianePos[1] != y:
            minotor[1] = y + 2
            y = y + 2

    def checkMinotorMove(self, x, y):
        if self.laby[x][y] == 1:
            return False
        elif self.checkCollisionVMinotor([x, y]) or \
                self.checkCollisionHMinotor([x, y]):
            return False
        elif self.checkCollisionHMinotor(self.theseePos):
            return False
        elif self.checkCollisionVMinotor(self.theseePos):
            return False
        return True

    def checkCollisionHMinotor(self, pos):
        for mh in self.minotorHPos:  # A bug minotor, we need to exclude the minotor which call this function
            if pos == mh:  # This code works because the minotor cannot have a collision with himself
                return True
        return False

    def checkCollisionVMinotor(self, pos):
        for mv in self.minotorVPos:
            if pos == mv:
                return True
        return False

    # -------------------------- Minotors Move ------------------------------------ #
    # -------------------------- Victory Condition ------------------------------------ #
    def isVictory(self):
        if self.theseePos == self.arianePos and self.arianePos == self.doorPos:
            return True
        return False

    def isGameOver(self):
        return self.checkCollisionHMinotor(self.arianePos) or \
               self.checkCollisionVMinotor(self.arianePos) or \
               self.checkCollisionHMinotor(self.theseePos) or \
               self.checkCollisionVMinotor(self.theseePos)

    # -------------------------- Victory Condition ------------------------------------ #
    # ---------------------------- Solver Method ------------------------------------- #

    def loadConf(self, conf):
        self.arianePos[0] = conf[0][0]
        self.arianePos[1] = conf[0][1]

        self.theseePos[0] = conf[1][0]
        self.theseePos[1] = conf[1][1]

        for i, mv in enumerate(conf[2]):
            self.minotorVPos[i][0] = mv[0]
            self.minotorVPos[i][1] = mv[1]

        for i, mh in enumerate(conf[3]):
            self.minotorHPos[i][0] = mh[0]
            self.minotorHPos[i][1] = mh[1]

    def reset(self):
        self.arianePos = self.posElements.get("A")
        self.theseePos = self.posElements.get("T")
        self.minotorHPos = self.posElements.get("H")
        self.minotorVPos = self.posElements.get("V")
        self.doorPos = self.posElements.get("P")
        self.save.clear()
        self.registerElements()

    # ---------------------------- Solver Methods ------------------------------------- #

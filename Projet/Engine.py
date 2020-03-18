import upemtk as tk


class Engine:

    def __init__(self, laby, posElements):
        self.laby = laby
        self.arianePos = posElements.get("A")
        self.theseePos = posElements.get("T")
        self.minotorHPos = posElements.get("H")
        self.minotorVPos = posElements.get("V")
        self.doorPos = posElements.get("P")

    # ----------------------------- Player Move ----------------------------------- #
    def checkPlayerMove(self, x, y):
        if self.laby[x][y] == 1:
            return False
        elif self.checkCollisionVMinotor([x, y]) or self.checkCollisionHMinotor([x, y]):
            return False
        return True

    def updateMovePlayer(self, ev):
        keyName = tk.touche(ev)

        x = self.arianePos[0]
        y = self.arianePos[1]
        if keyName == 'Left':
            if self.checkPlayerMove(x, y - 1) and self.checkPlayerMove(x, y - 2):
                self.arianePos[1] = y - 2
                return True
        elif keyName == 'Right':
            if self.checkPlayerMove(x, y + 1) and self.checkPlayerMove(x, y + 2):
                self.arianePos[1] = y + 2
                return True
        elif keyName == 'Up':
            if self.checkPlayerMove(x - 1, y) and self.checkPlayerMove(x - 2, y):
                self.arianePos[0] = x - 2
                return True
        elif keyName == 'Down':
            if self.checkPlayerMove(x + 1, y) and self.checkPlayerMove(x + 2, y):
                self.arianePos[0] = x + 2
                return True
        return False
    # ----------------------------- Player Move ----------------------------------- #

    # ------------------------------- IA Move ------------------------------------- #
    def updateMoveThesee(self):
        if self.checkMoveThesee():
            self.theseePos[0] = self.arianePos[0]
            self.theseePos[1] = self.arianePos[1]

    def checkMoveThesee(self):
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
        return True

    def checkCollisionHMinotor(self, pos):
        for mh in self.minotorHPos:  # A bug minotor, we need to exclude the minotor which call this function
            if pos == mh:            # This code works because the minotor cannot have a collision with himself
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


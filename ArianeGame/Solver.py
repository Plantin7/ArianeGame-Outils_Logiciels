class Solver:
    def __init__(self, engine, graphics):
        self.engine = engine
        self.graphics = graphics
        self.v = set()
        self.lst = []

    def DFS(self, c, isVisible=False):
        if isVisible:
            self.graphics.updateGraphicalSolver()

        if self.engine.isVictory():
            return True
        elif self.engine.isGameOver():
            return False
        else:
            # Adding c into v
            self.v.update({c})

            for d in ["Up", "Down", "Left", "Right"]:
                newC = self.computeC(d)
                if newC is not None:
                    if newC not in self.v:
                        if self.DFS(newC, isVisible):
                            self.lst.insert(0, d)
                            return True
                        else:
                            self.engine.loadConf(c)
                    else:
                        self.engine.loadConf(c)
            return False

    def BFS(self, c, isVisible=False):
        a_traiter = [(c, [])]
        self.v.update({c})
        while a_traiter:
            extract = a_traiter.pop(0)
            c = extract[0]
            arrayMove = extract[1]
            self.engine.loadConf(c)
            if isVisible:
                self.graphics.updateGraphicalSolver()
            if self.engine.isVictory():
                self.lst = arrayMove
                return True
            elif self.engine.isGameOver():
                continue
            else:
                for d in ["Up", "Down", "Left", "Right"]:
                    newC = self.computeC(d)
                    if newC is not None:
                        self.engine.loadConf(c)
                        if newC not in self.v:
                            self.v.update({newC})
                            tmp = arrayMove.copy()
                            tmp.append(d)
                            newElement = (newC, tmp)
                            a_traiter.append(newElement)

        if not a_traiter:
            return False

    def computeC(self, d):
        if self.engine.updatePlayerMove(d):
            self.engine.updateTheseeMove()
            self.engine.updateMinotorsVMove()
            self.engine.updateMinotorsHMove()
            newC = (tuple(self.engine.arianePos),
                    tuple(self.engine.theseePos),
                    tuple(tuple(x) for x in self.engine.minotorVPos),
                    tuple(tuple(x) for x in self.engine.minotorHPos))
            return newC
        return None

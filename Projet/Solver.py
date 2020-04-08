class Solver:
    def __init__(self, engine, graphics):
        self.engine = engine
        self.graphics = graphics
        self.v = set()
        self.lst = []

    def DFS(self, c, isVisible=False):
        if isVisible:
            self.graphics.updateSolver()
        self.engine.setConf(c)
        if self.engine.isVictory():
            return True
        elif self.engine.isGameOver():
            return False
        else:
            # Adding c into v
            self.v.update({self.engine.currentConf})
            directions = ["Up", "Down", "Left", "Right"]

            for d in directions:
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

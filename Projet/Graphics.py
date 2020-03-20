import upemtk as tk
import Engine


class Graphics:

    def __init__(self, laby, engine, grid_size, nb_cell, margin):
        self.laby = laby
        self.margin = margin
        self.cellSize = grid_size / nb_cell
        self.arianePos = engine.arianePos
        self.theseePos = engine.theseePos
        self.minotorHPos = engine.minotorHPos
        self.minotorVPos = engine.minotorVPos
        self.doorPos = engine.doorPos
        self.size = grid_size

    # Ariane
    def drawPlayerPos(self):
        tk.image(self.arianePos[1] * self.cellSize + self.margin,
                 self.arianePos[0] * self.cellSize + self.margin,
                 "media/ariane.png")

    # Thesee
    def drawIAPos(self):
        tk.image(self.theseePos[1] * self.cellSize + self.margin,
                 self.theseePos[0] * self.cellSize + self.margin,
                 "media/thesee.png")

    # All H minotors
    def drawHMinotors(self):
        for i in range(len(self.minotorHPos)):
            tk.image(self.minotorHPos[i][1] * self.cellSize + self.margin,
                     self.minotorHPos[i][0] * self.cellSize + self.margin,
                     "media/minoH.png")

    # All V minotors
    def drawVMinotors(self):
        for i in range(len(self.minotorVPos)):
            tk.image(self.minotorVPos[i][1] * self.cellSize + self.margin,
                     self.minotorVPos[i][0] * self.cellSize + self.margin,
                     "media/minoV.png")

    # Door
    def drawDoor(self):
        tk.image(self.doorPos[1] * self.cellSize + self.margin,
                 self.doorPos[0] * self.cellSize + self.margin,
                 "media/porte.png")

    # Horizontal Wall
    def drawHLine(self, i, j):
        tk.ligne((j - 1) * self.cellSize + self.margin,
                 i * self.cellSize + self.margin,
                 (j + 1) * self.cellSize + self.margin,
                 i * self.cellSize + self.margin,
                 "black", 3)

    # Vertical Wall
    def drawVLine(self, i, j):
        tk.ligne(j * self.cellSize + self.margin,
                 (i - 1) * self.cellSize + self.margin,
                 j * self.cellSize + self.margin,
                 (i + 1) * self.cellSize + self.margin,
                 "black", 3)

    # Labyrinth
    def drawLabyrinth(self):
        for i, line in enumerate(self.laby):
            for j, num in enumerate(line):
                if num == 1:
                    if j % 2 == 1 and j != 0 and j != self.size:
                        self.drawHLine(i, j)
                    elif i % 2 == 1 and i != 0 and i != self.size:
                        self.drawVLine(i, j)

    def drawVictory(self):
        tk.texte(self.size / 2, self.size / 2, "VICTORY", "blue", ancrage="center", police="Helvetica", taille=48)

    def drawGameOver(self):
        tk.texte(self.size / 2, self.size / 2, "GAME OVER", "red", ancrage="center", police="Helvetica", taille=48)

    def drawQuitTheGame(self):
        tk.texte(self.size / 2, self.size / 2 + self.size / 4, "Press 'Echap' to quit the game", "yellow",
                 ancrage="center", police="Helvetica", taille=30)

    def drawUndoAction(self):
        tk.texte(self.size / 2, self.size / 2 + self.size / 3, "Press 'R' to undo your action", "yellow",
                 ancrage="center", police="Helvetica", taille=30)

    # Update the game
    def update(self):
        tk.efface_tout()
        self.drawLabyrinth()
        self.drawDoor()
        self.drawPlayerPos()
        self.drawIAPos()
        self.drawHMinotors()
        self.drawVMinotors()

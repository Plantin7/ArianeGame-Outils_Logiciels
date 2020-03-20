from FileManager import *
from Graphics import *
from upemtk import *
from Engine import *


def waiting_key():
    while True:
        event = donne_evenement()
        type_ev = type_evenement(event)
        if type_ev == "Touche":
            break
        mise_a_jour()
    return event, type_ev


if __name__ == '__main__':
    laby, nbCell, posElements = chargeLabyrinth("maps/sandbox.txt")

    gridSize = 840
    margin = nbCell

    engine = Engine(laby, posElements)
    graphics = Graphics(laby, engine, gridSize, nbCell, margin)

    # Create Windows
    cree_fenetre(gridSize + 10, gridSize + 10)
    validPlay = False
    # Game Loop
    while True:
        graphics.update()

        if engine.isVictory():
            graphics.drawVictory()
            graphics.drawQuitTheGame()
            ev, tev = waiting_key()
            if touche(ev) == 'Escape':
                break
        elif engine.isGameOver():
            graphics.drawGameOver()
            graphics.drawQuitTheGame()
            graphics.drawUndoAction()
            ev, tev = waiting_key()
            if touche(ev) == 'Escape':
                break
            elif touche(ev) == 'r':
                engine.updateMovePlayer(ev)
        else:
            ev, tev = waiting_key()
            validPlay = engine.updateMovePlayer(ev)
            if touche(ev) == 'Escape':
                break
            if validPlay:
                engine.updateMoveThesee()
                engine.updateMinotorsVMove()
                engine.updateMinotorsHMove()
                engine.registerElements()

        mise_a_jour()
    ferme_fenetre()

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
    fm = FileManager("maps/labyrinthe1.txt")
    laby, nbCell, posElements = fm.chargeLabyrinth()

    gridSize = 840
    margin = nbCell

    engine = Engine(laby, posElements)
    graphics = Graphics(laby, engine, gridSize, nbCell, margin)

    # Create Windows
    cree_fenetre(gridSize + 10, gridSize + 10)

    # Game Loop
    while True:
        graphics.update()

        if engine.isVictory():
            graphics.drawVictory()
            break
        elif engine.isGameOver():
            graphics.drawGameOver()
            break

        validPlay = False
        ev, tev = waiting_key()
        if tev == 'Touche':  # on indique la touche pressée
            validPlay = engine.updateMovePlayer(ev)
            if touche(ev) == 'Escape':
                break
        if validPlay:
            engine.updateMoveThesee()
            engine.updateMinotorsVMove()
            engine.updateMinotorsHMove()

        mise_a_jour()

    graphics.drawPressAnyKey()
    tk.attente_touche()

    ferme_fenetre()

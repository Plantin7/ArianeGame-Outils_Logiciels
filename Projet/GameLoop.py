from FileManager import *
from Graphics import *
from upemtk import *
from Engine import *
from Solver import *
import argparse
import sys


def resetGame(engine, graphics):
    engine.reset()
    graphics.reset()


def printSolverDFS(plays):
    for p in plays:
        graphics.updateSolver()
        engine.updatePlayerMove(p)
        engine.updateTheseeMove()
        engine.updateMinotorsVMove()
        engine.updateMinotorsHMove()


def checkSolverMode(mode):
    if mode == 'DFS':
        return True
    elif mode == 'BFS':
        return True
    else:
        print('[Error] - Solver Mode Unknown : Only DFS or BFS')
        sys.exit(1)


def checkOptionSolverMode(args):
    if args.graphics or args.solver:
        return True
    print('[Error] - Solver Mode must be followed by -g or -s')
    sys.exit(1)


def waiting_key():
    while True:
        event = donne_evenement()
        type_ev = type_evenement(event)
        if type_ev == "Touche":
            break
        mise_a_jour()
    return event, type_ev


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' - Guide utilisateur du jeu Ariane et Minotaure -')
    parser.add_argument('level', type=str, help='maps/labyrintheX.txt')
    parser.add_argument("-g", "--graphics", action="store_true", help='Graphics Solver Mode = True')
    parser.add_argument("-s", "--solver", action="store_true", help='Solver Mode = True; IA Play for you')
    parser.add_argument('solver_mode', nargs='?', type=str, help='DFS or BFS')
    args = parser.parse_args()

    # Checking arguments
    laby, nbCell, posElements = chargeLabyrinth(args.level)

    # windows size
    windowsSize = 840

    # initialisation of all objects
    engine = Engine(laby, posElements)
    graphics = Graphics(laby, engine, windowsSize, nbCell)
    solver = Solver(engine, graphics)
    # InitialConf Used by Solver
    initialConf = (engine.arianePos, engine.theseePos, engine.minotorVPos, engine.minotorHPos)

    # Create Windows
    cree_fenetre(windowsSize + 10, windowsSize + 10)

    if args.solver_mode:
        checkSolverMode(args.solver_mode)
        checkOptionSolverMode(args)
        if args.solver_mode == 'DFS':
            if args.graphics:
                solver.DFS(initialConf, True)
            else:
                solver.DFS(initialConf)
            if args.solver:
                resetGame(engine, graphics)
                printSolverDFS(solver.lst)
        elif args.solver_mode == 'BFS':
            # TODO
            pass
        ferme_fenetre()
        sys.exit(0)

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
            keyName = touche(ev)
            if keyName == 'Escape':
                break
            elif keyName == 'r':
                engine.updatePlayerMove(keyName)
        else:
            ev, tev = waiting_key()
            keyName = touche(ev)
            validPlay = engine.updatePlayerMove(keyName)
            if touche(ev) == 'Escape':
                break
            if validPlay:
                engine.updateTheseeMove()
                engine.updateMinotorsVMove()
                engine.updateMinotorsHMove()
                engine.registerElements()

    ferme_fenetre()

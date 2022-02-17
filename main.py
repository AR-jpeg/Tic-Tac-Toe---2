import core.gloabals as globals
import core.utils as utils

boardSize = utils.fancyInput(
    "What size would you like the game board to be? ", globals.GREEN, int, end="\n")
mainBoard = utils.createGameBoard(size=boardSize)


utils.setMove(mainBoard, (0, 0), "X")
utils.setMove(mainBoard, (0, 1), "O")

print(utils.isMoveValid(mainBoard, (0, 0)))

utils.printGameBoard(mainBoard)

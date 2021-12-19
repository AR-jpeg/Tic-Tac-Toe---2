import core.gloabals as globals
import core.utils as utils


boardSize = utils.fancyInput(
    "What size would you like the game board to be? ", globals.GREEN, int, end="\n")
mainBoard = utils.createGameBoard(size=boardSize)

utils.printGameBoard(mainBoard)

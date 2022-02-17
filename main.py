import core.gloabals as globals
import core.utils as utils
import core.checks as checks

boardSize = utils.fancyInput(
    "What size would you like the game board to be? ", globals.GREEN, int, end="\n")
mainBoard = utils.createGameBoard(size=boardSize)

mainBoard = \
[
    [1, 2, 3],
    [5, 5, 5],
    [7, 8, 9]
]

print(checks.gameOver(mainBoard))

utils.printGameBoard(mainBoard)

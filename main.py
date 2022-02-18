import core.gloabals as globals
import core.utils as utils
import core.checks as checks
import core.errors as errors
from time import sleep

boardSize = utils.fancyInput(
    "What size would you like the game board to be? ", globals.GREEN, int, end="\n")
mainBoard = utils.createGameBoard(size=boardSize)

print(utils.fancyInput("test ", globals.RED, resultType=str, allowedValues=["yes", "no"]))

# while True:
#     utils.clearScreen()
#     utils.printGameBoard(mainBoard)
    
#     print()

#     while True:
#         try:
#             row = int(utils.fancyInput("What row do you want to place your move in? ", globals.ORANGE, int)-1)
#             column = int(utils.fancyInput("What column do you want to place your move in? ", globals.ORANGE, int)-1)

#             utils.setMove(mainBoard, (row, column), "X")

#         except errors.SquareAlreadyTakenError:
#             pass
#         except errors.SqareOutOfBoundsError:
#             pass
#         else: 
#             break
    
#     if checks.gameOver(mainBoard)[0]:
#         utils.fancyPrint(f"Player {checks.gameOver(mainBoard)[1]} won!", globals.GREEN)
#         break

#     sleep(2)

# utils.printGameBoard(mainBoard)

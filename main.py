import core.gloabals as globals
import core.utils as utils
import core.checks as checks
import core.errors as errors
from time import sleep

boardSize = utils.fancyInput(
	"What size would you like the game board to be? ", globals.GREEN, int, end="\n")
mainBoard = utils.createGameBoard(size=boardSize)

# print(utils.fancyInput("test ", globals.RED, resultType=str, allowedValues=["yes", "no"]))
minSizeToWin = utils.fancyInput("What is the minimum size that you need to win? ", globals.GREEN, int)

while minSizeToWin > boardSize:
	minSizeToWin = utils.fancyInput(
		f"Your input of {minSizeToWin} was larger than the size of the board, {boardSize}. Please try selecting another minimum size. ", globals.RED, int
	)

numberOfPlayers = utils.fancyInput("How many players will be playing? ", globals.GREEN, int)
players = []

utils.clearScreen()

# print(utils.itemAlreadyInDictOfList("test", "joe", {
# 	"my": "god",
# 	"this": "is tough",
# 	"joe": "test"
# }))
# Create all players
for p in range(0, numberOfPlayers):
	pSymbol = utils.fancyInput(
		f"Player {p+1}, what symbol do you want to choose? ", globals.GREEN, str
	)

	while len(pSymbol) > 1 or utils.itemAlreadyInDictOfList(pSymbol, "symbol", players) or pSymbol == "":
		if len(pSymbol) > 1:
			pSymbol = utils.fancyInput(
				f"Player {p+1}, your symbol, '{pSymbol}' was more than 1 character long, please enter a new symbol. ", globals.RED, str
			)   

		if utils.itemAlreadyInDictOfList(pSymbol, "symbol", players):
			otherPlayerWithSameName = utils.itemAlreadyInDictOfList(pSymbol, "symbol", players)[1]
			pSymbol = utils.fancyInput(
				f"Player {p+1}, your symbol, '{pSymbol}' was already selected by {otherPlayerWithSameName}. Please choose a new symbol. ",
				globals.RED, str
			)

		if pSymbol == "":
			pSymbol = utils.fancyInput(f"Player {p+1}, the symbol '' is not a valid symbol, please enter a new symbol. ", globals.RED, str)

	pName = utils.fancyInput(
		f"What is your name? (will default to `Player {p+1}` if nothing is typed in). ", globals.GREEN
	)

	while utils.itemAlreadyInDictOfList(pName, "name", players):
		pName = utils.fancyInput(f"The name '{pName}' was already taken, please enter a new name. ", globals.RED, str)

	if pName in ["", " "]:
		pName = f"Player {p+1}"


	players.append({
		"name": pName,
		"symbol": pSymbol
	})

	print()
	
	utils.fancyPrint(f"Sucessfully set {pName}'s symbol to {pSymbol}!", globals.BLUE)

	sleep(1.5)
	utils.clearScreen()
	print(players)

utils.fancyPrint(f"Sucessfully created a game board with a size of {boardSize} with {numberOfPlayers} players!", globals.GREEN, "\n\n")
utils.printGameBoard(mainBoard)




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

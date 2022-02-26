import core.errors as errors
from core.checks import isMoveValid, gameOver
import core.gloabals as globals
from core.move import setMove
import core.utils as utils
from time import sleep



boardSize = utils.fancyInput(
	"What size would you like the game board to be? ", globals.GREEN, int, end="\n")
mainBoard = utils.createGameBoard(size=boardSize)

minSizeToWin = utils.fancyInput("What is the minimum size that you need to win? ", globals.GREEN, int)

while minSizeToWin > boardSize or minSizeToWin <= 1:
	if minSizeToWin > boardSize:
		minSizeToWin = utils.fancyInput(
			f"Your input of {minSizeToWin} was larger than the size of the board, {boardSize}. Please try selecting another minimum size. ", globals.RED, int
		)

	if minSizeToWin <= 1:
		minSizeToWin = utils.fancyInput(
			f"Your input of '{minSizeToWin}' was equal to or smaller than 1. Please try selecting another minimum size. ", globals.RED, int
		)

numberOfPlayers = utils.fancyInput("How many players will be playing? ", globals.GREEN, int)
players = []

utils.clearScreen()

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

stop = False

while not stop:
	for p in players:
		if gameOver(mainBoard, minSizeToWin)[0]:
			utils.clearScreen()
			utils.printGameBoard(mainBoard)

			utils.fancyPrint(f"{gameOver(mainBoard, minSizeToWin)[1]} won, GG!", globals.GREEN)
			
			stop = True
			break


		utils.clearScreen()

		utils.fancyPrint(f"{p['name']}, it is now your turn. \n", globals.BLUE)
		utils.printGameBoard(mainBoard)
		print("\n")

		playerGrid = utils.fancyInput("Which row would you like to place your move in? ", globals.GREEN, int) - 1
		playerCollumn = utils.fancyInput("Which collumn would you like to place your move in? ", globals.GREEN, int) - 1

		playerMove = (playerGrid, playerCollumn)

		# Make sure the move is always valid
		while True:
			try:
				if isMoveValid(mainBoard, playerMove):
					# Only break once the move was valid
					break

			except errors.SqareOutOfBoundsError:
				utils.clearScreen()

				utils.fancyPrint(f"{p['name']}, your move of ({playerGrid+1}, {playerCollumn+1}) " + 
				"was not a valid move because it was out of bounds, please try entering another move! \n", globals.RED)

				utils.printGameBoard(mainBoard)

				playerGrid = utils.fancyInput("Which row would you like to place your move in? ", globals.GREEN, int) - 1
				playerCollumn = utils.fancyInput("Which collumn would you like to place your move in? ", globals.GREEN, int) - 1

				playerMove = (playerGrid, playerCollumn)

			except errors.SquareAlreadyTakenError:
				utils.clearScreen()

				utils.fancyPrint(f"{p['name']}, your move of ({playerGrid+1}, {playerCollumn+1}) " + 
				"was not a valid move because the square you were trying to move at was already taken, please try entering another move! \n", globals.RED)

				utils.printGameBoard(mainBoard)

				playerGrid = utils.fancyInput("Which row would you like to place your move in? ", globals.GREEN, int) - 1
				playerCollumn = utils.fancyInput("Which collumn would you like to place your move in? ", globals.GREEN, int) - 1

				playerMove = (playerGrid, playerCollumn)

		# Once the move has been validated, set the move and move on to the next player
		setMove(mainBoard, playerMove, p['symbol'])

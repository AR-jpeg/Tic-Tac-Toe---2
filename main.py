from core.utils import \
 (  fancyInput, fancyPrint,
	createGameBoard, clearScreen, printGameBoard,
	itemAlreadyInDictOfList, findPlayerWithSymbol)

import core.errors as errors
from core.checks import isMoveValid, gameOver
import core.gloabals as globals
from core.move import setMove
from time import sleep


boardSize = fancyInput(
	"What size would you like the game board to be? ", globals.GREEN, int, end="\n")
mainBoard = createGameBoard(size=boardSize)

minSizeToWin = fancyInput("What is the minimum size that you need to win? ", globals.GREEN, int)

while minSizeToWin > boardSize or minSizeToWin <= 1:
	if minSizeToWin > boardSize:
		minSizeToWin = fancyInput(
			f"Your input of {minSizeToWin} was larger than the size of the board, {boardSize}. Please try selecting another minimum size. ", globals.RED, int
		)

	if minSizeToWin <= 1:
		minSizeToWin = fancyInput(
			f"Your input of '{minSizeToWin}' was equal to or smaller than 1. Please try selecting another minimum size. ", globals.RED, int
		)

numberOfPlayers = fancyInput("How many players will be playing? ", globals.GREEN, int)
players = []

clearScreen()

# Create all players
for p in range(0, numberOfPlayers):
	pSymbol = fancyInput(
		f"Player {p+1}, what symbol do you want to choose? ", globals.GREEN, str
	)

	while len(pSymbol) > 1 or itemAlreadyInDictOfList(pSymbol, "symbol", players) or pSymbol == "":
		if len(pSymbol) > 1:
			pSymbol = fancyInput(
				f"Player {p+1}, your symbol, '{pSymbol}' was more than 1 character long, please enter a new symbol. ", globals.RED, str
			)   

		if itemAlreadyInDictOfList(pSymbol, "symbol", players):
			otherPlayerWithSameName = itemAlreadyInDictOfList(pSymbol, "symbol", players)[1]
			pSymbol = fancyInput(
				f"Player {p+1}, your symbol, '{pSymbol}' was already selected by {otherPlayerWithSameName}. Please choose a new symbol. ",
				globals.RED, str
			)

		if pSymbol == "":
			pSymbol = fancyInput(f"Player {p+1}, the symbol '' is not a valid symbol, please enter a new symbol. ", globals.RED, str)

	pName = fancyInput(
		f"What is your name? (will default to `Player {p+1}` if nothing is typed in). ", globals.GREEN
	)

	while itemAlreadyInDictOfList(pName, "name", players):
		pName = fancyInput(f"The name '{pName}' was already taken, please enter a new name. ", globals.RED, str)

	if pName in ["", " "]:
		pName = f"Player {p+1}"


	players.append({
		"name": pName,
		"symbol": pSymbol
	})

	print()
	
	fancyPrint(f"Sucessfully set {pName}'s symbol to {pSymbol}!", globals.BLUE)

	sleep(1.5)
	clearScreen()
	print(players)

fancyPrint(f"Sucessfully created a game board with a size of {boardSize} with {numberOfPlayers} players!", globals.GREEN, "\n\n")
printGameBoard(mainBoard)

stop = False

while not stop:
	for p in players:
		if gameOver(mainBoard, minSizeToWin)[0]:
			clearScreen()
			printGameBoard(mainBoard)

			fancyPrint(f"{ findPlayerWithSymbol(players, gameOver(mainBoard, minSizeToWin)[1]) } won, GG!", globals.GREEN)
			
			stop = True
			break


		clearScreen()

		fancyPrint(f"{p['name']}, it is now your turn. \n", globals.BLUE)
		printGameBoard(mainBoard)
		print("\n")

		playerGrid = fancyInput("Which row would you like to place your move in? ", globals.GREEN, int) - 1
		playerCollumn = fancyInput("Which collumn would you like to place your move in? ", globals.GREEN, int) - 1

		playerMove = (playerGrid, playerCollumn)

		# Make sure the move is always valid
		while True:
			try:
				if isMoveValid(mainBoard, playerMove):
					# Only break once the move was valid
					break

			except errors.SqareOutOfBoundsError:
				clearScreen()

				fancyPrint(f"{p['name']}, your move of ({playerGrid+1}, {playerCollumn+1}) " + 
				"was not a valid move because it was out of bounds, please try entering another move! \n", globals.RED)

				printGameBoard(mainBoard)

				playerGrid = fancyInput("Which row would you like to place your move in? ", globals.GREEN, int) - 1
				playerCollumn = fancyInput("Which collumn would you like to place your move in? ", globals.GREEN, int) - 1

				playerMove = (playerGrid, playerCollumn)

			except errors.SquareAlreadyTakenError:
				clearScreen()

				fancyPrint(f"{p['name']}, your move of ({playerGrid+1}, {playerCollumn+1}) " + 
				"was not a valid move because the square you were trying to move at was already taken, please try entering another move! \n", globals.RED)

				printGameBoard(mainBoard)

				playerGrid = fancyInput("Which row would you like to place your move in? ", globals.GREEN, int) - 1
				playerCollumn = fancyInput("Which collumn would you like to place your move in? ", globals.GREEN, int) - 1

				playerMove = (playerGrid, playerCollumn)

		# Once the move has been validated, set the move and move on to the next player
		setMove(mainBoard, playerMove, p['symbol'])

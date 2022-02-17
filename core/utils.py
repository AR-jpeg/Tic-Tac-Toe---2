from .gloabals import EMPTY, RED, GREEN, WHITE, BLUE
from .errors import SquareAlreadyTakenError
from .checks import isMoveValid
from typing import List, Tuple
import colorama
import os

def convertFromZeroBased(move: Tuple[int, int]):
    return (move[0]+1, move[1]+1)

def convertFromOneBased(move: Tuple[int, int]):
    return (move[0]-1, move[1]-1)

def fancyInput(text: str, color, resultType=object, end=""):
    print(color + text + WHITE, end="")

    while True:
        result = input()

        if result == "exit" or result == "leave" or result == "l":
            leave = fancyInput("Are you sure you want to leave (y/n)? ",
                               color=RED, resultType=str)

            if leave == "yes" or leave == "y":
                clearScreen()
                fancyPrint("Thank you for playing! ", GREEN)
                quit()

            else:
                continue

        try:
            return resultType(result)

        except:
            fancyPrint("Oh no, the expected type of the input was " +
                       str(resultType) + ". Please try again! ", RED, end="")

def fancyPrint(text: str, color, end="\n") -> None:
    print(color + text + WHITE, end=end)

def printGameBoard(board: List[List[str]], color=BLUE) -> None:
    """Prints the game board out in a default color of blue.

    Arguments:
        board -- The game board to be printed out

    Keyword Arguments:
        color -- The color that the game board will be printed in (default: {BLUE})
    """

    print(colorama.Fore.BLUE+"-" + ('-' * len(board)*4))

    for row in board:
        for index, char in enumerate(row):
            if index == 0:
                print(colorama.Fore.BLUE + "| ", end="")

            print(colorama.Fore.LIGHTBLUE_EX + str(char), end="")
            if index != len(row):
                print(colorama.Fore.BLUE+" | ", end="")

        print()

    print("-" + ('-' * len(board)*4)+colorama.Fore.WHITE)

def createGameBoard(size: int) -> List[List[str]]:
    board: List[List[str]] = []
    for i in range(size):
        board.append([])
        for k in range(size):
            board[i].append(EMPTY)

    return board

def setMove(board: List[List[str]], move: Tuple[int, int], charToSet: str):
    if not isMoveValid(board, move):
        fancyPrint(f"Move at {convertFromZeroBased(move)} was not valid, the selected square was already taken", RED)
        raise SquareAlreadyTakenError
    
    board[move[0]][move[1]] = charToSet
    fancyPrint(f"Succesfully set the square at {convertFromZeroBased(move)} to {charToSet}!", GREEN)
    
    return

def clearScreen() -> None:
    os.system("clear")


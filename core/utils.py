from .gloabals import EMPTY, RED, GREEN, WHITE, BLUE, ORANGE
from .errors import SquareAlreadyTakenError, SqareOutOfBoundsError
from .checks import isMoveValid
from typing import List, Tuple
import colorama
import os

def convertFromZeroBased(move: Tuple[int, int]):
    return (move[0]+1, move[1]+1)

def convertFromOneBased(move: Tuple[int, int]):
    return (move[0]-1, move[1]-1)

def convertListToString(l: List) -> str:
    res = ""
    for e in l:
        res += str(e)

    return res

def createSubStrings(s, maxLen: int) -> List[str]:
    if type(s) == list:
        s = convertListToString(s)
    


def fancyInput(text: str, color, resultType=object, end="", allowedValues=[]):
    print(color + text + WHITE, end="")

    while True:
        try:
            result = input()
        except (KeyboardInterrupt, EOFError):
            print()
            leave = fancyInput("Do you want to quit? ", RED, str, allowedValues=['yes', 'no', 'y', 'n'])

            if leave in ['y', 'yes']:
                clearScreen()
                fancyPrint("Thank you for playing!", GREEN)
                quit()

            fancyPrint(text, color)
            continue

        if result not in allowedValues and allowedValues != []:
            result = fancyInput(f"Your input '{result}' was not a valid input, please enter something like '{allowedValues[0]}'. ", RED, resultType, end, allowedValues)


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
            fancyPrint(f"Oh no, the expected type of the input was '{str(resultType)[8:-2]}'. Please try again! ", RED, end="")

def fancyPrint(text: str, color, end="\n") -> None:
    print(color + text + WHITE, end=end)

def printGameBoard(board: List[List[str]], color=BLUE) -> None:
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
    try:
        isMoveValid(board, move)
    except SquareAlreadyTakenError:
        fancyPrint(f"Move at {convertFromZeroBased(move)} was not valid, the selected square was already taken. Please try again.", RED)
        raise SquareAlreadyTakenError
    except SqareOutOfBoundsError:
        fancyPrint(f'Move at {convertFromZeroBased(move)} was not valid, the move was out of bounds. Please try again.', RED)
        raise SqareOutOfBoundsError
    
    board[move[0]][move[1]] = charToSet
    fancyPrint(f"Succesfully set the square at {convertFromZeroBased(move)} to {charToSet}!", GREEN)
    
    return

def clearScreen() -> None:
    os.system("clear")


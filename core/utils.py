from .gloabals import EMPTY, RED, GREEN, WHITE, BLUE
from typing import Dict, List, Tuple
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
    
def fancyInput(text: str, color, resultType=None, end="", allowedValues=[]):
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

        if resultType == None:
            return result

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


def createSubStrings(s, maxLen: int) -> List[str]:
    if type(s) == list:
        s = convertListToString(s)

    res: List[str] = []

    for i in range(0, len(s)+1):
        for j in range(i, len(s)+1):
            if len(s[i:j]) != maxLen:
                continue
            
            res.append(s[i:j])

    return res


def itemAlreadyInDictOfList(item, key, l: List[Dict]):
    for d in l:
        if d[key] == item:
            return True, d["name"]
    
    return False

def clearScreen() -> None:
    os.system("clear")

def findPlayerWithSymbol(players: List[Dict[str, str]], symbol: str) -> str:
    for player in players:
        if player["symbol"] == symbol:
            return player["name"]

    return -1
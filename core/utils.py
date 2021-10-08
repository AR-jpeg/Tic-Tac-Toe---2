from typing import List
import colorama


def fancyInput(i: str, color) -> None:
    print(color + i + colorama.Fore.WHITE, end=" ")
    input()

def printGameBoard(board: List[List[str]]) -> None:
    for row in board:
        for index, char in enumerate(row):
            print(char, end="")
            if index != len(row):
                print(" | ", end="")

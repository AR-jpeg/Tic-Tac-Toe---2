from .errors import SqareOutOfBoundsError, SquareAlreadyTakenError
from .utils import createSubStrings
from typing import List, Tuple
from .gloabals import EMPTY

def getValidPositions(board: List[List[str]]) -> List[Tuple[int, int]]:
    res = []

    for rIndex, row in enumerate(board):
        for cIndex, char in enumerate(row):
            if char == EMPTY:
                res.append((rIndex, cIndex))

    return res

def isMoveValid(board: List[List[str]], move: Tuple[int, int]) -> bool:
    moveG, moveC = move

    if moveG > len(board)-1 or moveC > len(board[moveG])-1:
        raise SqareOutOfBoundsError

    if board[moveG][moveC] != EMPTY:
        raise SquareAlreadyTakenError
    
    return True

def allElementsSame(list: List[object]) -> bool:
    firstElement = list[0]

    if firstElement == EMPTY:
        return False

    for element in list:
        if element != firstElement:
            return False

    return True

def gameOver(board: List[List[str]], sizeToWin: int):
    patternsToCheck = []

    for line in board:
        # Add horizontal patterns
        for subPattern in createSubStrings(line, sizeToWin):
            patternsToCheck.append(subPattern)

    # Add the collumns
    collumns: List[List] = []

    for verticlePointer in range(0, len(board[0])):
        collumns.append([])

        for line in board:
            collumns[verticlePointer].append(line[verticlePointer])

    for collumn in collumns:
        for subPattern in createSubStrings(collumn, sizeToWin):
            patternsToCheck.append(subPattern)

    # # Add all of the diagonals
    # tl_br_diagonal = []

    # for y in range(len(board), -1, -1):
    #     for x in range(len(board)):
    #         print(board[y])

    # Add the top left -> bottom right diagonal
    tl_br_diagonal = []
    for i in range(len(board)):
        tl_br_diagonal.append(board[i][i])

    for subPattern in createSubStrings(tl_br_diagonal, sizeToWin):
        patternsToCheck.append(subPattern)

    # Add the bottom left -> top right diagonal
    bl_tr_diagonal = []
    for i in range(len(board)-1, -1,-1):
        bl_tr_diagonal.append(list(reversed(board[i]))[i])

    for subPattern in createSubStrings(bl_tr_diagonal, sizeToWin):
        patternsToCheck.append(subPattern)


    for pattern in patternsToCheck:
        if allElementsSame(pattern):
            return True, pattern[0]
    
    return False, ""
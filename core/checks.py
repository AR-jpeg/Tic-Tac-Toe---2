from typing import List, Literal, Tuple, Union
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
        return False

    if board[moveG][moveC] != EMPTY:
        return False
    
    return True

def allElementsSame(list: List[object]) -> bool:
    firstElement = list[0]

    if firstElement == EMPTY:
        return False

    for element in list:
        if element != firstElement:
            return False

    return True

def gameOver(board: List[List[str]]):
    patternsToCheck = []

    for line in board:
        # Add horizontal patterns
        patternsToCheck.append(line)


    # Add the collumns
    collumns: List[List] = []

    for verticlePointer in range(0, len(board[0])):
        collumns.append([])

        for line in board:
            collumns[verticlePointer].append(line[verticlePointer])

    for collumn in collumns:
        patternsToCheck.append(collumn)

    # Add the top left -> bottom right diagonal
    tl_br_diagonal = []
    for i in range(len(board)):
        tl_br_diagonal.append(board[i][i])

    patternsToCheck.append(tl_br_diagonal)

    # Add the bottom left -> top right diagonal
    bl_tr_diagonal = []
    for i in range(len(board)-1, -1,-1):
        bl_tr_diagonal.append(list(reversed(board[i]))[i])

    patternsToCheck.append(bl_tr_diagonal)

    for pattern in patternsToCheck:
        if allElementsSame(pattern):
            return True, pattern[0]
    
    return False
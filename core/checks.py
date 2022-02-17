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
        return False

    if board[moveG][moveC] != EMPTY:
        return False
    
    return True
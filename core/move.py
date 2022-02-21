from .utils import convertFromZeroBased, fancyPrint
from .errors import SqareOutOfBoundsError, SquareAlreadyTakenError
from .gloabals import RED, GREEN
from .checks import isMoveValid
from typing import List, Tuple


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
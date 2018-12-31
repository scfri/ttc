"""Perfect AI, using tree to determine winning prob"""

from ttc.ttc import *

class PerfectAi:
    """Perfect AI class"""

    def __init__(self, board):
        self.board = board
        print_board(board)

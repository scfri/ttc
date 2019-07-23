"""Perfect AI, using tree to determine winning prob"""

import ttc


class Node:
    """Nodes for AI tree"""

    def __init__(self, board, expected_value):
        self.board = board
        self.expected_value = expected_value

    def get_value(self):
        return self.expected_value


class PerfectAi:
    """Perfect AI class"""

    def __init__(self, board):
        self.board = board
        print_board(board)

    def get_move(self, board):
        """Get move"""

        get_tree(board)

def get_tree(board):
    """Get tree of all remaining moves"""

    pass

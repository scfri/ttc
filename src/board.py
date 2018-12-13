

class Board:
    """Tic-Tac-Toe board to hold game - will only create square board"""

    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        return [[None, None, None], [None, None, None], [None, None, None]]

    def get_current_board(self):
        return "current board"

    def print_board(self):
        for i in self.board:
            for j in i:
                print(j)


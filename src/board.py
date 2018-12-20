from point import *


class Board:
    """Tic-Tac-Toe board to hold game - will only create square board"""

    def __init__(self, size):
        self.size = size
        self.board = self.create_board()

    def create_board(self):
        board = []

        for _ in range(0, self.size):
            tmp = []
            for _ in range(0, self.size):
                tmp.append(None)
            board.append(tmp)

        return board

    def add_point_to_board(self, point: Point):
        """Add specified point to board"""

        if self.is_valid_move(point):
            # if move is valid
            # update board
            self.update_board(point)
        else:
            # move is invalid, prompt again
            print("Invalid move!")

    def is_valid_move(self, point: Point) -> bool:
        """determines if move is valid (i.e. there is no point on board yet)"""

        move_column = point.get_column()
        move_row = point.get_row()
        if self.get_point_on_board(move_column, move_row) is None:
            return True
        return False

    def get_point_on_board(self, column: int, row: int) -> bool:
        """Determine if board is "None" at given row and column"""

        print(type(row))
        print(type(column))

        print(self.board[row][column])

    def update_board(self, point: Point):
        """update board to reflect most recent move"""
        pass

    def get_current_board(self):
        return "current board"

    def print_board(self):
        """Print the current board"""
        num = 0
        print("  ", end="")
        for letter in range(97, 97 + len(self.board)):
            print('{:^6}'.format(chr(letter)), end="")
        print("")
        for i in self.board:
            print("%s|"%(num), end="")
            num += 1
            for j in i:
                print('{:^5}'.format(str(j)), end="")
                print("|", end="")
            print("")

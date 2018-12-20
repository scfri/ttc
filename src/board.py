from point import *


class Board:
    """Tic-Tac-Toe board to hold game - will only create square board"""

    def __init__(self, size):
        self.size = size
        self.board = self.create_board()

    def create_board(self):
        """Create the initial board, using size given by the user"""

        board = []

        for _ in range(0, self.size):
            tmp = []
            for _ in range(0, self.size):
                tmp.append(None)
            board.append(tmp)

        return board

    def add_point_to_board(self, point: Point, player: str) -> bool:
        """Add specified point to board"""

        if self.is_valid_move(point):
            self.update_board(point, player)
            return True
        else:
            print("Invalid move! Please try again...")
            return False

    def is_valid_move(self, point: Point) -> bool:
        """determines if move is valid (i.e. there is no point on board yet)"""

        move_column = point.get_column()
        move_row = point.get_row()
        try:
            if self.get_point_on_board(move_column, move_row) is None:
                return True
            return False
        except IndexError:
            return False

    def get_point_on_board(self, column: int, row: int) -> bool:
        """Determine if board is "None" at given row and column"""

        print(type(row))
        print(type(column))

        print(self.board[row][column])

    def update_board(self, point: Point, player: str):
        """update board to reflect most recent move"""

        self.board[point.get_row()][point.get_column()] = player
        self.print_board()

    def print_board(self):
        """Print the current board"""

        num = 0
        print("  ", end="")
        for letter in range(97, 97 + len(self.board)):
            print('{:^6}'.format(chr(letter)), end="")
        print("")
        for i in self.board:
            print("%s|"%(num+1), end="")
            num += 1
            for j in i:
                print('{:^5}'.format(str(j)), end="")
                print("|", end="")
            print("")

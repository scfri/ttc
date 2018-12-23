import random
from typing import NamedTuple


class Point(NamedTuple):
    """To store point of next move"""

    column: str
    row: int

    def __repr__(self):
        return str(self.column) + str(self.row)

    def get_column(self) -> int:
        """Returns column number - 0 indexed"""

        return ord(self.column) - 97

    def get_row(self) -> int:
        """Returns row number - visual board is 1 indexed, so converts to 0-index"""

        return int(self.row)-1


class Ttc:
    """Tic-Tac-Toe game - main class"""

    def __init__(self):
        self.board = Board(3)
        self.current_player = True # TODO: determine what value user wants to be
        self.num_valid_moves = 0
        self.opponet = AImee("O")
        self.run_ttc()

    def run_ttc(self):
        """run TTC game"""

        self.board.print_board()

        while self.num_valid_moves < 9:
            # TODO: make this "AI"
            if current_player:
                point = get_move(self.get_current_player())
            else:
                point = self.ai.get_move()
            if point is not None:
                valid = self.board.is_valid_move(point)
                if valid:
                    self.num_valid_moves += 1
                    print(self.num_valid_moves)
                    c_player = self.get_current_player()
                    self.board.update_board(point, c_player)
                    if self.board.check_winner():
                        print("YOU ARE THE WINNER!!!")
                        break
                    self.current_player = not self.current_player
                else:
                    print("Invalid move! Please try again...")
        print("It's a DRAW!!!")

    def get_current_player(self) -> str:
        """Returns current player -- either 'X' or 'O'"""

        if self.current_player:
            return 'X'
        return 'O'


class AImee:
    """(AI)mee is the AI class you will play againstQ"""

    def __init__(self, player: str):
        self.player = player

    def get_player(self) -> str:
        """returns player representaion (i.e. X or O)"""

        return self.player

    def get_move(self) -> point:
        """get AImee to return a move"""

        # TODO: get random move
        try:
            column: str = move[0]
            row: int = move[1]
        except (IndexError, ValueError):
            print("Invalid move! Please try again...")
            return None
        return Point(column=column.lower(), row=row)

class Board:
    """Tic-Tac-Toe board to hold game - will only create square board"""

    def __init__(self, size: int):
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

    def is_valid_move(self, point: Point) -> bool:
        """determines if move is valid (i.e. there is no point on board yet)"""

        try:
            move_column = point.get_column()
            move_row = point.get_row()
            return point_is_none(self.board, move_column, move_row)
        except (IndexError, ValueError):
            return False

    def update_board(self, point: Point, player: str):
        """update board to reflect most recent move"""

        self.board[point.get_row()][point.get_column()] = player
        self.print_board()

    def check_winner(self) -> bool:
        """Check if last move created a winner!"""

        is_winner = False

        is_winner |= self.check_horizontal_winner()
        is_winner |= self.check_vertical_winner()
        is_winner |= self.check_diagonal_winner()

        return is_winner

    def check_horizontal_winner(self) -> bool:
        """checks for horizontal winner"""

        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return True
        return False

    def check_vertical_winner(self) -> bool:
        """checks for vertial winner"""

        for column in range(0, self.size):
            """
            board[0][0] == board[0][1] == board[0][2]
            """
            b = self.board
            if b[0][column] == b[1][column] == b[2][column] and b[0][column] is not None:
                return True
        return False


    def check_diagonal_winner(self) -> bool:
        """checks for diagonal winner"""

        mid = self.board[1][1]
        if mid is not None:
            if self.board[0][0] == mid == self.board[2][2]:
                return True
            if self.board[2][0] == mid == self.board[0][2]:
                return True
        return False

    def print_board(self):
        """Print the current board"""

        num = 0
        print()
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
        print()


def get_move(current_player):
    """Get move from player"""

    print("CURRENT PLAYER: %s" %(current_player))
    move: str = input("Please enter move <column><row>: ")
    try:
        column: str = move[0]
        row: int = move[1]
    except (IndexError, ValueError):
        print("Invalid move! Please try again...")
        return None
    return Point(column=column.lower(), row=row)


def point_is_none(board, column: int, row: int) -> bool:
    """Determine if board is "None" at given row and column"""

    if board[row][column] == None:
        print("self.board[row][column] == None")
        return True
    return False


if __name__ == "__main__":
    ttc = Ttc()


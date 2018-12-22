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
        self.winner = False
        self.current_player = True # TODO: figure out current player situation
        self.run_ttc()

    def run_ttc(self):
        """run TTC game"""
        self.board.print_board()

        # TODO: while true; or, take size of board == max num moves (e.g. 3*3 = 9)
        for i in range(0, 6):
            point = get_move(self.get_current_player())
            if point is not None:
                valid = self.board.add_point_to_board(point, self.get_current_player())
                if valid:
                    winner = self.board.check_winner()
                    if winner:
                        print("YOU ARE THE WINNER!!!")
                        break
                    self.current_player = not self.current_player

    def get_current_player(self) -> str:
        """Returns current player -- either 'X' or 'O'"""

        if self.current_player:
            return 'X'
        return 'O'


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
            return point_is_none(self.board, move_column, move_row)
        except IndexError:
            return False

    def update_board(self, point: Point, player: str):
        """update board to reflect most recent move"""

        self.board[point.get_row()][point.get_column()] = player
        self.print_board()

    def check_winner(self) -> bool:
        """Check if last move created a winner!"""

        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return True
        # TODO: check for vertical winner
        # TODO: check for horizontal winner
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

    # TODO: need to check user input
    print("CURRENT PLAYER: %s" %(current_player))
    move: str = input("Please enter move <column><row>: ")
    try:
        column: str = move[0]
        row: int = move[1]
    except IndexError:
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


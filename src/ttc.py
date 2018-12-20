from board import *
from point import *


def get_move(current_player):
    """Get move from player"""
    print("CURRENT PLAYER: %s" %(current_player))
    column: str = input("Please enter column: ")
    row: int = input("Please enter row: ")
    return Point(column=column.lower(), row=row)


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

        # while not self.winner:
        point = get_move(self.get_current_player())
        print(point)
        self.board.add_point_to_board(point, self.get_current_player())

    def get_current_player(self) -> str:
        """Returns current player -- either 'X' or 'O'"""

        if self.current_player:
            return "X"
        return "O"

if __name__ == "__main__":
    ttc = Ttc()


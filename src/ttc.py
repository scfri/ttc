from board import *
from point import *


def get_move(current_player):
    """Get move from player"""
    print("CURRENT PLAYER: %s" %(current_player))
    row: str = input("Please enter x: ")
    column: int = input("Please enter y: ")
    return Point(row=row, column=column)


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

    def make_move():
        return "made a move"

    def get_current_player(self):
        if self.current_player:
            return "X"
        else:
            return "O"

if __name__ == "__main__":
    ttc = Ttc()


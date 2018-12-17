from board import *
from point import *


class Ttc:
    """Tic-Tac-Toe game - main class"""

    def __init__(self):
        self.board = Board(3)
        self.winner = False
        self.run_ttc()

    def run_ttc(self):
        self.board.print_board()

        # while not self.winner:
        point = self.get_move()
        print(point)

    def get_move(self):
        x: str = input("Please enter x: ")
        y: int = input("Please enter y: ")
        return Point(x=x, y=y)

    def make_move():
        return "made a move"

if __name__ == "__main__":
    ttc = Ttc()


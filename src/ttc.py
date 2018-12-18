from board import *
from point import *


class Ttc:
    """Tic-Tac-Toe game - main class"""

    def __init__(self):
        self.board = Board(3)
        self.winner = False
        self.run_ttc()

    def run_ttc(self):
        """run TTC game"""
        self.board.print_board()

        # while not self.winner:
        current_player = 1
        point = self.get_move(current_player)
        print(point)

    def get_move(self, current_player):
        """Get move from player"""
        print("CURRENT PLAYER: %s" %(current_player))
        x: str = input("Please enter x: ")
        y: int = input("Please enter y: ")
        return Point(x=x, y=y)

    def make_move():
        return "made a move"

if __name__ == "__main__":
    ttc = Ttc()


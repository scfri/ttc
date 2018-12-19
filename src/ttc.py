from board import *
from point import *
from players import *


def get_move(players):
    """Get move from player"""
    print("CURRENT PLAYER: %s" %(players.get_current_player()))
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
        point = get_move(self.players)
        print(point)

    def make_move():
        return "made a move"

    def get_players(self):
        return self.players

if __name__ == "__main__":
    ttc = Ttc()


from board import *
from point import *


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


if __name__ == "__main__":
    ttc = Ttc()


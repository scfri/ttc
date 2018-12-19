from point import *

class Board:
    """Tic-Tac-Toe board to hold game - will only create square board"""

    def __init__(self, size):
        self.size = size
        self.board = self.create_board()

    def create_board(self):
        board = []

        for row in range(0, self.size):
            tmp = []
            for col in range(0, self.size):
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

    def is_valid_move(self, point: Point):
        """determines if move is valid (i.e. there is no point on board yet)"""
        pass

    def update_board(self, point: Point):
        """update board to reflect most recent move"""
        pass

    def get_current_board(self):
        return "current board"

    def print_board(self):
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

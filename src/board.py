
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

    def get_current_board(self):
        return "current board"

    def print_board(self):
        num = 0
        print("  ", end="")
        for i in range(0, len(self.board)):
            print('{:^6}'.format(i), end="")
        print("")
        for i in self.board:
            print("%s|"%(num), end="")
            num += 1
            for j in i:
                print('{:^5}'.format(str(j)), end="")
                print("|", end="")
            print("")

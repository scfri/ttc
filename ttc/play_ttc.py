"""Simple Tic Tac Toe game written, its called Ttc!"""

import random
import point
import aimee


BOARD_SIZE = 3


def find_horizontal_winner(board, player_id) -> point.Point:
    """Find horizontal winner"""

    # TODO: make this work for diff board sizes
    for i, row in enumerate(board):
        if row[0] == row[1] == player_id and row[2] is None:
            return point.Point(column='c', row=i+1)
        if row[1] == row[2] == player_id and row[0] is None:
            return point.Point(column='a', row=i+1)
        if row[0] == row[2] == player_id and row[1] is None:
            return point.Point(column='b', row=i+1)
    return None


def find_vertical_winner(board, player_id) -> point.Point:
    """Find vertical winner"""

    # TODO: make this work for diff board sizes
    for i in range(0, BOARD_SIZE):
        if board[0][i] == board[1][i] == player_id and board[2][i] is None:
            return point.Point(column=chr(97+i), row=3)
        if board[1][i] == board[2][i] == player_id and board[0][i] is None:
            return point.Point(column=chr(97+i), row=1)
        if board[0][i] == board[2][i] == player_id and board[1][i] is None:
            return point.Point(column=chr(97+i), row=2)
    return None


def find_diagonal_winner(board, player_id) -> point.Point:
    """Find diagonal winner"""

    if board[0][0] == board[1][1] == player_id:
        return point.Point(column='c', row=3)
    if board[1][1] == board[2][2] == player_id:
        return point.Point(column='a', row=1)
    if board[0][0] == board[2][2] == player_id:
        return point.Point(column='b', row=2)
    if board[0][2] == board[1][1] == player_id:
        return point.Point(column='a', row=3)
    if board[0][2] == board[2][0] == player_id:
        return point.Point(column='b', row=2)
    if board[1][1] == board[2][0] == player_id:
        return point.Point(column='a', row=3)
    return None


def run_ttc():
    """run TTC game"""

    board = create_board(BOARD_SIZE)
    # TODO: dynamically determine what value user wants to be
    current_player_is_user = random.choice([True, False])
    num_valid_moves = 0
    opponent = aimee.Aimee("O")
    is_winner = False

    print_board(board)

    def get_current_player() -> str:
        """Returns current player -- either 'X' or 'O'"""

        if current_player_is_user:
            return 'X'
        return 'O'

    while num_valid_moves < 9:
        if current_player_is_user:
            point = get_move(get_current_player())
        else:
            point = opponent.get_move(board)
        if point is not None:
            valid = is_valid_move(board, point)
            if valid:
                num_valid_moves += 1
                c_player = get_current_player()
                update_board(board, point, c_player)
                if check_winner(board):
                    is_winner = True
                    if current_player_is_user:
                        print("YOU ARE THE WINNER!!!")
                    else:
                        print("Aimee is the winner!")
                    break
                current_player_is_user = not current_player_is_user
            else:
                if current_player_is_user:
                    print("Invalid move! Please try again...")
    if not is_winner:
        print("It's a DRAW!!!")


def create_board(size):
    """Create the initial board, using size given by the user"""

    board = []

    try:
        for _ in range(0, size):
            tmp = []
            for _ in range(0, size):
                tmp.append(None)
            board.append(tmp)

        return board
    except TypeError:
        print("Invalid board size given")


def is_valid_move(board, point: point.Point) -> bool:
    """determines if move is valid (i.e. there is no point on board yet)"""

    try:
        move_column = point.get_column()
        move_row = point.get_row()
        return point_is_none(board, move_column, move_row)
    except (IndexError, ValueError):
        print("%s is invalid move" % (point))
        return False


def update_board(board, point: point.Point, player: str):
    """update board to reflect most recent move"""

    board[point.get_row()][point.get_column()] = player
    print_board(board)


def check_horizontal_winner(board) -> bool:
    """checks for horizontal winner"""

    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return True
    return False


def check_vertical_winner(board) -> bool:
    """checks for vertial winner"""

    for column in range(0, BOARD_SIZE):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] is not None:
            return True
    return False


def check_diagonal_winner(board) -> bool:
    """checks for diagonal winner"""

    mid = board[1][1]
    if mid is not None:
        if board[0][0] == mid == board[2][2]:
            return True
        if board[2][0] == mid == board[0][2]:
            return True
    return False


def check_winner(board) -> bool:
    """Check if last move created a winner!"""

    is_winner = False

    is_winner |= check_horizontal_winner(board)
    is_winner |= check_vertical_winner(board)
    is_winner |= check_diagonal_winner(board)

    return is_winner


def print_board(board):
    """Print the current board"""

    num = 0
    print()
    print("  ", end="")
    for letter in range(97, 97 + len(board)):
        print('{:^6}'.format(chr(letter)), end="")
    print("")
    for i in board:
        print("%s|" % (num+1), end="")
        num += 1
        for j in i:
            print('{:^5}'.format(str(j)), end="")
            print("|", end="")
        print("")
    print()


def get_move(current_player):
    """Get move from player"""

    print("CURRENT PLAYER: %s" % (current_player))
    move: str = input("Please enter move <column><row>: ")
    try:
        column: str = move[0]
        row: int = move[1]
    except (IndexError, ValueError):
        print("Invalid move! Please try again...")
        return None
    return point.Point(column=column.lower(), row=row)


def point_is_none(board, column: int, row: int) -> bool:
    """Determine if board is "None" at given row and column"""

    try:
        if board[row][column] is None:
            return True
        return False
    except IndexError:
        print("That is an invalid move, please try again")
        return False


if __name__ == "__main__":
    run_ttc()

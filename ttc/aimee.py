"""Aimee AI"""

import random
import point
from play_ttc import find_diagonal_winner
from play_ttc import find_horizontal_winner
from play_ttc import find_vertical_winner
from play_ttc import BOARD_SIZE

class Aimee:
    """(AI)mee is the AI class you will play against"""

    def __init__(self, player_id: str):
        self.player_id = player_id

    def get_player_id(self) -> str:
        """returns player representaion (i.e. X or O)"""

        return self.player_id

    def get_move(self, board) -> point.Point:
        """get Aimee to return a move"""

        def find_winning_move(board, player_id) -> point.Point:
            """Find a winning move, if there is one"""

            horizontal_winner = find_horizontal_winner(board, player_id)
            vertical_winner = find_vertical_winner(board, player_id)
            diagonal_winner = find_diagonal_winner(board, player_id)

            if horizontal_winner is not None:
                return horizontal_winner
            if vertical_winner is not None:
                return vertical_winner
            if diagonal_winner is not None:
                return diagonal_winner
            return None

        move_to_make = find_winning_move(board, self.get_player_id())

        if self.get_player_id() == 'X':
            opponent_id = 'O'
        else:
            opponent_id = 'X'

        if move_to_make is None:
            move_to_make = find_winning_move(board, opponent_id)

        if move_to_make is None:
            column = chr(random.randint(0, BOARD_SIZE) + 96)
            row = random.randint(0, BOARD_SIZE)
            move_to_make = point.Point(column=column.lower(), row=row)

        return move_to_make

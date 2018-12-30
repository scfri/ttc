"""Test suite for Ttc"""


from ttc.ttc import *


def test_board_size():
    """test board size is correct"""

    board = create_board(3)
    assert len(board) == 3

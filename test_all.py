"""Test suite for Ttc"""


from ttc.ttc import *


def test_find_horizontal_winner():
    """test horizontal winner"""
    board = []
    board.append(['O', 'O', None])
    board.append([None, None, None])
    board.append([None, None, None])

    assert find_horizontal_winner(board) == Point(column='c', row=0)

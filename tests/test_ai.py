"""Aimee test suite"""

from ttc.ttc import *

def test_find_horizontal_winner():
    """test find_horizontal_winner"""

    aimee = Aimee('O')
    aimee_player_id = aimee.get_player_id()

    solution_board = []
    solution_board.append([None, 'O', 'O'])
    solution_board.append([None, None, None])
    solution_board.append([None, None, None])

    assert find_horizontal_winner(solution_board, aimee_player_id) == Point(column='a', row=1)

    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append(['O', None, 'O'])
    solution_board.append([None, None, None])

    assert find_horizontal_winner(solution_board, aimee_player_id) == Point(column='b', row=2)

    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append([None, None, None])
    solution_board.append(['O', 'O', None])

    assert find_horizontal_winner(solution_board, aimee_player_id) == Point(column='c', row=3)

    # test if no solution
    no_solution_board = []
    no_solution_board.append([None, None, None])
    no_solution_board.append([None, None, None])
    no_solution_board.append([None, None, None])

    assert find_horizontal_winner(no_solution_board, aimee_player_id) is None


def test_get_move():
    """Test Aimee find_winning_move method"""

    aimee = Aimee('O')

    # test horizontal
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append([None, 'O', 'O'])
    solution_board.append([None, None, None])

    assert aimee.get_move(solution_board) == Point(column='a', row=2)

    # test vertical
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append([None, None, 'O'])
    solution_board.append([None, None, 'O'])

    assert aimee.get_move(solution_board) == Point(column='c', row=1)

    # test diagonal
    solution_board = []
    solution_board.append(['O', None, None])
    solution_board.append([None, None, None])
    solution_board.append([None, None, 'O'])

    assert aimee.get_move(solution_board) == Point(column='b', row=2)

    # test if no solution -- should return a random point
    no_solution_board = []
    no_solution_board.append([None, None, None])
    no_solution_board.append([None, None, None])
    no_solution_board.append([None, None, None])

    assert aimee.get_move(no_solution_board) is not None


def test_get_vertical_winner():
    """test aimee vertical winner"""

    aimee = Aimee('X')
    aimee_player_id = aimee.get_player_id()

    # test if solution in 1,1
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append(['X', None, None])
    solution_board.append(['X', None, None])

    assert find_vertical_winner(solution_board, aimee_player_id) == Point(column='a', row=1)

    # test if solution in 1,2
    solution_board = []
    solution_board.append(['X', None, None])
    solution_board.append([None, None, None])
    solution_board.append(['X', None, None])

    assert find_vertical_winner(solution_board, aimee_player_id) == Point(column='a', row=2)

    # test if solution in 1,3
    solution_board = []
    solution_board.append(['X', None, None])
    solution_board.append(['X', None, None])
    solution_board.append([None, None, None])

    assert find_vertical_winner(solution_board, aimee_player_id) == Point(column='a', row=3)


def test_find_diagonal_winner():
    """Test to find diagonal winner"""

    aimee = Aimee('O')
    aimee_player_id = aimee.get_player_id()

    # test simple solution
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append([None, 'O', None])
    solution_board.append([None, None, 'O'])

    assert find_diagonal_winner(solution_board, aimee_player_id) == Point(column='a', row=1)

    solution_board = []
    solution_board.append(['O', None, None])
    solution_board.append([None, 'O', None])
    solution_board.append([None, None, None])

    assert find_diagonal_winner(solution_board, aimee_player_id) == Point(column='c', row=3)

    solution_board = []
    solution_board.append([None, None, 'O'])
    solution_board.append([None, 'O', None])
    solution_board.append([None, None, None])

    assert find_diagonal_winner(solution_board, aimee_player_id) == Point(column='a', row=3)

    solution_board = []
    solution_board.append([None, None, 'O'])
    solution_board.append([None, None, None])
    solution_board.append(['O', None, None])

    assert find_diagonal_winner(solution_board, aimee_player_id) == Point(column='b', row=2)

    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append([None, None, None])
    solution_board.append(['O', None, None])

    assert find_diagonal_winner(solution_board, aimee_player_id) is None


def test_aimee_player():
    """Make sure AImee knows correct player"""

    aimee = Aimee('O')

    assert aimee.get_player_id() == 'O'

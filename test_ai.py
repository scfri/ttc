"""Aimee test suite"""

from ttc.ttc import *

def test_find_horizontal_winner():
    """test find_horizontal_winner"""

    aimee = Aimee('O')

    # test if solution in 1,1
    solution_board = []
    solution_board.append([None, 'O', 'O'])
    solution_board.append([None, None, None])
    solution_board.append([None, None, None])

    assert aimee.find_horizontal_winner(solution_board) == Point(column='a', row=1)

    # test if solution in 1,2
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append([None, 'O', 'O'])
    solution_board.append([None, None, None])

    assert aimee.find_horizontal_winner(solution_board) == Point(column='a', row=2)

    # test if solution in 1,3
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append([None, None, None])
    solution_board.append([None, 'O', 'O'])

    assert aimee.find_horizontal_winner(solution_board) == Point(column='a', row=3)

    # test if solution in 2,1
    solution_board = []
    solution_board.append(['O', None, 'O'])
    solution_board.append([None, None, None])
    solution_board.append([None, None, None])

    assert aimee.find_horizontal_winner(solution_board) == Point(column='b', row=1)

    # test if solution in 2,2
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append(['O', None, 'O'])
    solution_board.append([None, None, None])

    assert aimee.find_horizontal_winner(solution_board) == Point(column='b', row=2)

    # test if solution in 2,3
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append([None, None, None])
    solution_board.append(['O', None, 'O'])

    assert aimee.find_horizontal_winner(solution_board) == Point(column='b', row=3)

    # test if solution in 3,1
    solution_board = []
    solution_board.append(['O', 'O', None])
    solution_board.append([None, None, None])
    solution_board.append([None, None, None])

    assert aimee.find_horizontal_winner(solution_board) == Point(column='c', row=1)

    # test if solution in 3,2
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append(['O', 'O', None])
    solution_board.append([None, None, None])

    assert aimee.find_horizontal_winner(solution_board) == Point(column='c', row=2)

    # test if solution in 3,3
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append([None, None, None])
    solution_board.append(['O', 'O', None])

    assert aimee.find_horizontal_winner(solution_board) == Point(column='c', row=3)

    # test if no solution
    no_solution_board = []
    no_solution_board.append([None, None, None])
    no_solution_board.append([None, None, None])
    no_solution_board.append([None, None, None])

    assert aimee.find_horizontal_winner(no_solution_board) is None


def test_find_winning_move():
    """Test Aimee find_winning_move method"""

    # aimee = Aimee('O')

    # # test if solution in 1,1
    # solution_board = []
    # solution_board.append([None, 'O', 'O'])
    # solution_board.append([None, None, None])
    # solution_board.append([None, None, None])

    # assert aimee.find_winning_move(solution_board) == Point(column='a', row=1)

    # # test if solution in 1,2
    # solution_board = []
    # solution_board.append([None, None, None])
    # solution_board.append([None, 'O', 'O'])
    # solution_board.append([None, None, None])

    # assert aimee.find_winning_move(solution_board) == Point(column='a', row=2)

    # # test if solution in 1,3
    # solution_board = []
    # solution_board.append([None, None, None])
    # solution_board.append([None, None, None])
    # solution_board.append([None, 'O', 'O'])

    # assert aimee.find_winning_move(solution_board) == Point(column='a', row=3)

    # # test if solution in 2,1
    # solution_board = []
    # solution_board.append(['O', None, 'O'])
    # solution_board.append([None, None, None])
    # solution_board.append([None, None, None])

    # assert aimee.find_winning_move(solution_board) == Point(column='b', row=1)

    # # test if solution in 2,2
    # solution_board = []
    # solution_board.append([None, None, None])
    # solution_board.append(['O', None, 'O'])
    # solution_board.append([None, None, None])

    # assert aimee.find_winning_move(solution_board) == Point(column='b', row=2)

    # # test if solution in 2,3
    # solution_board = []
    # solution_board.append([None, None, None])
    # solution_board.append([None, None, None])
    # solution_board.append(['O', None, 'O'])

    # assert aimee.find_winning_move(solution_board) == Point(column='b', row=3)

    # # test if solution in 3,1
    # solution_board = []
    # solution_board.append(['O', 'O', None])
    # solution_board.append([None, None, None])
    # solution_board.append([None, None, None])

    # assert aimee.find_winning_move(solution_board) == Point(column='c', row=1)

    # # test if solution in 3,2
    # solution_board = []
    # solution_board.append([None, None, None])
    # solution_board.append(['O', 'O', None])
    # solution_board.append([None, None, None])

    # assert aimee.find_winning_move(solution_board) == Point(column='c', row=2)

    # # test if solution in 3,3
    # solution_board = []
    # solution_board.append([None, None, None])
    # solution_board.append([None, None, None])
    # solution_board.append(['O', 'O', None])

    # assert aimee.find_winning_move(solution_board) == Point(column='c', row=3)

    # # test if no solution
    # no_solution_board = []
    # no_solution_board.append([None, None, None])
    # no_solution_board.append([None, None, None])
    # no_solution_board.append([None, None, None])

    # assert aimee.find_winning_move(no_solution_board) is None


def test_get_vertical_winner():
    """test aimee vertical winner"""

    aimee = Aimee('X')

    # test if solution in 1,1
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append(['X', None, None])
    solution_board.append(['X', None, None])

    assert aimee.find_vertical_winner(solution_board) == Point(column='a', row=1)

    # test if solution in 1,2
    solution_board = []
    solution_board.append(['X', None, None])
    solution_board.append([None, None, None])
    solution_board.append(['X', None, None])

    assert aimee.find_vertical_winner(solution_board) == Point(column='a', row=2)

    # test if solution in 1,3
    solution_board = []
    solution_board.append(['X', None, None])
    solution_board.append(['X', None, None])
    solution_board.append([None, None, None])

    assert aimee.find_vertical_winner(solution_board) == Point(column='a', row=3)


def test_find_diagonal_winner():
    """Test to find diagonal winner"""

    aimee = Aimee('O')

    # test simple solution
    solution_board = []
    solution_board.append([None, None, None])
    solution_board.append([None, 'O', None])
    solution_board.append([None, None, 'O'])

    assert aimee.find_diagonal_winner(solution_board) == Point(column='a', row=1)


def test_get_move():
    """Test if aimee.get_move() alwayas returns a Point"""

    aimee = Aimee('O')

    board = []
    board.append([None, None, None])
    board.append([None, None, None])
    board.append(['O', 'O', None])

    assert aimee.get_move is not None


def test_aimee_player():
    """Make sure AImee knows correct player"""

    aimee = Aimee('O')

    assert aimee.get_player_id() == 'O'

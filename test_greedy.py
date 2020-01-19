import csv
import time

import numpy as np
import pytest

from .libgreedy.greedy import greedy_solve
from .libgreedy.kadane import auxiliary, greedy_kadane_solve
from .libgreedy.utils import matrix_from_matrix_csv, matrix_from_rel_csv


def test_matrix_csv_15():

    input_file = "resources/problems/15x15-0.1.csv"

    matrix = matrix_from_matrix_csv(input_file)
    solution = greedy_solve(matrix)

    print(solution)

    # Bigger solution, just assert lengthes equal
    assert solution == {2, 3, 5, 8, 11, 13, 14}


def test_matrix_csv_100():

    input_file = "resources/problems/100x100-0.02.csv"

    matrix = matrix_from_matrix_csv(input_file)
    solution = greedy_solve(matrix)

    print(solution)

    # Bigger solution, just assert lengthes equal
    assert len(solution) == 47


def test_matrix_csv_3000():

    input_file = "resources/problems/3000x3000-0.0001.csv"

    matrix = matrix_from_matrix_csv(input_file)
    solution = greedy_solve(matrix)

    print(solution)

    # Bigger solution, just assert lengthes equal
    assert len(solution) == 2414


def test_rel_csv():

    input_file = "resources/problems/CE-rel.csv"

    matrix = matrix_from_rel_csv(input_file)
    solution = greedy_solve(matrix)

    print(solution)

    assert solution == {6, 11, 12}


def test_xkadanes_matrix():

    input_file = "resources/problems/CE-matrix.csv"

    matrix = matrix_from_matrix_csv(input_file)
    solution = greedy_kadane_solve(matrix)

    print(solution)

    assert solution == {0, 1, 2, 3}

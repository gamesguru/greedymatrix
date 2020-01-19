import csv
import time

import numpy as np
import pytest

from .libgreedy.greedy import greedy_solve
from .libgreedy.kadane import auxiliary, greedy_kadane_solve
from .libgreedy.utils import matrix_from_matrix_csv, matrix_from_rel_csv


def test_kadanes_aux_matrix():

    input_file = "resources/problems/CE.csv"

    matrix = matrix_from_rel_csv(input_file)
    solution = greedy_kadane_solve(matrix)

    print(solution)

    assert solution == {0, 1, 2, 3}


def test_matrix_csv():

    input_file = "resources/problems/_100x100-0.1.csv"

    matrix = matrix_from_matrix_csv(input_file)
    solution = greedy_solve(matrix)

    print(solution)

    assert solution == {0, 96, 67, 37, 5, 73, 75, 44, 45, 14, 77, 84, 56, 89, 61, 94}


def test_matrix_csv_3000():

    input_file = "resources/problems/_3000x3000-0.03.csv"

    matrix = matrix_from_matrix_csv(input_file)
    solution = greedy_solve(matrix)

    print(solution)

    assert len(solution) == 92


def test_rel_csv():

    input_file = "resources/problems/CE.csv"

    matrix = matrix_from_rel_csv(input_file)
    solution = greedy_solve(matrix)

    print(solution)

    assert solution == set({6, 11, 12})

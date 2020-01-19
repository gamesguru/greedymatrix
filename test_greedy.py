import csv
import time

import numpy as np
import pytest

from .libgreedy.greedy import solve
from .libgreedy.utils import matrix_from_matrix_csv, matrix_from_rel_csv


def test_matrix_csv():

    input_file = "resources/problems/_100x100-0.1.csv"

    matrix = matrix_from_matrix_csv(input_file)
    solution = solve(matrix)

    print(solution)

    assert solution == {0, 96, 67, 37, 5, 73, 75, 44, 45, 14, 77, 84, 56, 89, 61, 94}


def test_rel_csv():

    input_file = "resources/problems/CE.csv"

    matrix = matrix_from_rel_csv(input_file)
    solution = solve(matrix)

    print(solution)

    assert solution == set({6, 11, 12})

import csv
import time

import matplotlib.pyplot as plt
import numpy as np
import pytest
import seaborn

from .libgreedy.foresight import greedy_ahead
from .libgreedy.greedy import solve
from .libgreedy.utils import matrix_from_matrix_csv, matrix_from_rel_csv


def test_matrix_csv_15():

    input_file = "resources/problems/15x15-0.1.csv"

    matrix = matrix_from_matrix_csv(input_file)
    solution = solve(matrix)

    # Bigger solution, just assert lengthes equal
    assert solution == {0, 3, 7, 9, 12, 13, 14}


def test_matrix_csv_100():

    input_file = "resources/problems/100x100-0.02.csv"

    matrix = matrix_from_matrix_csv(input_file)
    solution = solve(matrix)

    # Bigger solution, just assert lengthes equal
    assert len(solution) == 47


def test_matrix_csv_3000():

    input_file = "resources/problems/3000x3000-0.0001.csv"

    matrix = matrix_from_matrix_csv(input_file)
    solution = solve(matrix)

    # Bigger solution, just assert lengthes equal
    assert len(solution) == 2414


def test_rel_csv():

    input_file = "resources/problems/CE-rel.csv"

    matrix = matrix_from_rel_csv(input_file)
    matrix = np.rot90(matrix)
    matrix = np.rot90(matrix)
    solution = solve(matrix)

    # assert solution == {6, 11, 12}
    assert solution == {9, 10, 11, 12}


def test_tricky_matrix():
    input_file = "resources/problems/CE-2-r270.csv"

    matrix = matrix_from_matrix_csv(input_file)
    solution = solve(matrix)

    assert solution


def test_xgreedy_ahead():

    input_file = "resources/problems/CE-matrix.csv"

    matrix = matrix_from_matrix_csv(input_file)
    tree = greedy_ahead(matrix)

    assert tree


def test_xstats_size():
    pass


def test_xstats_sparsity():
    pass


def test_xstats_distribution_style():
    pass


@pytest.mark.xfail
def test_xstats_matrix_heatmap():

    input_file = "resources/matrix.csv"

    matrix = matrix_from_matrix_csv(input_file)

    # Create heatmap
    ax = seaborn.heatmap(matrix)

    # Set axes labels and invert Y-axis
    plt.title("Matrix HeatMap (ESRI - missing entries and zeros)")
    plt.xlabel("Origin #")
    plt.ylabel("Destination #")
    plt.gca().invert_yaxis()

    plt.savefig("resources/matrix_heatmap.png", dpi=350)

    assert ax

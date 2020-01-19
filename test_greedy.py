import csv
import time

from .libgreedy.greedy import solve
from .libgreedy.utils import matrix_from_rel_csv

import pytest
import numpy as np


def test_rel_csv(input_file=None):

    if not input_file:
        input_file = "resources/problems/CE.csv"

    matrix = matrix_from_rel_csv(input_file)

    solution = solve(matrix)
    print(solution)

    assert solution == set({6, 11, 12})



def test_matrix_csv(input_file=None):

    # Get pairs and singles
    nums = set()
    pairs = set()

    if not input_file:
        input_file = "resources/problems/esri.csv"

    # Create matrix
    n = sum(1 for line in open(input_file))
    matrix = np.zeros((n, n), dtype=np.byte,)

    # Read in
    t0 = time.time()
    print("Read in CSV")
    with open(input_file) as f:
        reader = csv.reader(f)

        i = 0
        for line in reader:
            # row = matrix[i]
            matrix[i] = line
            i += 1
    # Fill diag with ones
    np.fill_diagonal(matrix, 1)
    print(f"{time.time() - t0}s")

    # Find max
    n = len(nums)
    m = max(nums)
    print(
        f"""Pre-pruning
    Span:  {n}
    Max:   {m}
    Miss:  {[x for x in range(0, m) if not x in nums]}
    Pairs: {len(pairs)}
    """
    )
    print(f"Num stops: {n}\n")

    # Remove compliments
    t0 = time.time()
    print("Prune compliments")
    for i in nums:
        for j in nums:
            pair = (i, j)
            anti_pair = (j, i)
            if not pair in pairs and anti_pair in pairs:
                pairs.remove(anti_pair)
    print(f"Post pruning: {len(pairs)} entries")
    print(f"{time.time() - t0}s")

    # Create the matrix
    t0 = time.time()
    print("Dump into numpy matrix[][]")
    matrix = np.zeros((n, n), dtype=np.byte,)
    for p in pairs:
        i = p[0]
        j = p[1]
        # Set cell True
        matrix[i][j] = 1
    del pairs
    print(f"{time.time() - t0}s")

    solution = solve(matrix)
    print(solution)

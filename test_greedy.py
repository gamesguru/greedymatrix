import csv
import time

from .greedy import solve
from .utils import matrix_from_rel_csv

import pytest
import numpy as np


def test_rel_csv(input_file=None):

    if not input_file:
        input_file = "resources/problems/CE.csv"

    matrix = matrix_from_rel_csv(input_file)
    solution = solve(matrix)
    print(solution)
    assert solution == set(
        {
            0,
            8,
            11,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            29,
            30,
            31,
            32,
            33,
            35,
            36,
            37,
            38,
            39,
            41,
            44,
            45,
            48,
            49,
        }
    )

    # Stream output to new CSV

    # print("\n==> Streaming new filtered CSV")
    # with open(input_file.replace(".csv", ".filtered.csv"), "w+") as csv_out:
    #     writer = csv.writer(csv_out)

    #     # Read in
    #     with open(input_file) as csv_in:
    #         reader = csv.reader(csv_in)

    #         for row in reader:
    #             i = int(row[o_index])
    #             j = int(row[d_index])
    #             # Add only members of the square solution
    #             if i in solution and j in solution and i != j:
    #                 writer.writerow(row)


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

import sys
import csv
import time

import numpy as np

MAX_PRINT_SIZE = 75


def greedy_solve(matrix):

    #
    # Init dict
    print("\nInit dict")
    t0 = time.time()
    matches = {i: 0 for i in range(0, matrix.shape[0])}

    for i in matches.keys():
        row = matrix[i]

        for j in matches.keys():
            if row[j]:
                # Symmetric, so only sum rows
                matches[i] += 1
    print(f"{time.time() - t0}s")

    #
    #
    # Apply Greedy algorithm
    print(
        """
--------------------
Begin GREEDY algo
--------------------
    """
    )

    #
    # Setup algo
    loops = 1
    purged_key = None
    t0 = time.time()

    while True:

        print(f"==> ITERATION #{loops} ({len(matches)} remaining)")

        #
        # Detract purged key from tallies
        if purged_key is not None:
            # Only worry about remaining keys
            for key in matches.keys():
                row = matrix[key]

                if row[purged_key]:
                    # We lost a 1, so detract from the match
                    matches[key] -= 1

        #
        # Purged keys
        purged_key = None

        #
        # Break if square
        if all(x == len(matches) for x in matches.values()):
            # Print matrix if small
            if len(matches) <= MAX_PRINT_SIZE:
                print_matrix(matrix, matches, purged_key)
            elapsed_micros = round((time.time() - t0) * 1000, 3)
            print(
                f"""
-------------------------------------------
DONE:     {len(matches)} x {len(matches)} matches!
found in: {elapsed_micros:,} ms
-------------------------------------------
"""
            )
            break

        #
        # Greedy selection
        purged_key = min(matches, key=matches.get)
        index = list(matches.keys()).index(purged_key)
        print(f"  del {index}->{purged_key}  (x{matches[purged_key]})")
        # Print matrix if small
        if len(matches) <= MAX_PRINT_SIZE:
            print_matrix(matrix, matches, purged_key)
        # Delete key
        del matches[purged_key]

        # Continue
        loops += 1

    #
    # Return solution
    solution = set(matches.keys())
    return solution


def print_matrix(matrix, matches, purging_key):

    # Get inputs ready
    n = len(matches)

    m2 = np.zeros((n, n), dtype=np.int)
    np.fill_diagonal(m2, 1)

    # Fill truncated matrix
    for i, x in enumerate(matches):

        row = matrix[x]

        for j, y in enumerate(matches):
            if x == y or i == j:
                continue
            # Add cell
            m2[i][j] = row[y]

    # Print
    # np.savetxt(sys.stdout.buffer, m2, fmt="%i")
    for i, x in enumerate(matches):
        row = m2[i]
        row = " ".join([str(e) for e in row])
        if x == purging_key:
            row += f"  <- del  {matches[x]}"
        else:
            row += f"          {matches[x]}"
        print(row)
    print()

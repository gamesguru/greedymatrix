import time

import numpy as np


def alloc_aux(matrix):

    # Assume square for now
    n = matrix.shape[0]

    # Init auxiliary matrix
    _aux = np.zeros((n, n), dtype=np.byte,)

    # Put first row and first column in
    _aux[0] = matrix[0]
    for i in range(1, n):
        _aux[i][0] = matrix[i][0]

    # # Put zeros back in
    # for i in range(1, n):
    #     for j in range(1, n):
    #         if not matrix[i][j]:
    #             # Required initial condition
    #             _aux[i][j] = 0
    print(_aux)
    return _aux


def auxiliary(matrix):

    print(f"malloc")
    aux = alloc_aux(matrix)

    # Assume square for now
    n = matrix.shape[0]

    # Fill aux
    for i in range(1, n):
        for j in range(1, n):
            # Apply Kaden's algo
            if matrix[i][j]:
                aux[i][j] = min(aux[i][j - 1], aux[i - 1][j], aux[i - 1][j - 1],) + 1
            else:
                aux[i][j] = 0

    # Return aux matrix
    return aux


def irange(aux):
    k = np.amax(aux)
    indicies = np.where(aux == k)

    y_max = indicies[0][0]
    y_range = set(range(y_max, y_max - k, -1))

    return y_range
    # return min(y_range), max(y_range) + 1


#
# https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
def printMaxSubSquare(M):
    R = len(M)  # no. of rows in M[][]
    C = len(M[0])  # no. of columns in M[][]

    S = [[0 for k in range(C)] for l in range(R)]
    # here we have set the first row and column of S[][]
    S[0] = M[0]
    for i in range(0, C):
        S[i][0] = M[i][0]

    # Construct other entries
    for i in range(1, R):
        for j in range(1, C):
            if M[i][j] == 1:
                S[i][j] = min(S[i][j - 1], S[i - 1][j], S[i - 1][j - 1]) + 1
            else:
                S[i][j] = 0

    # Find the maximum entry and
    # indices of maximum entry in S[][]
    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if max_of_s < S[i][j]:
                max_of_s = S[i][j]
                max_i = i
                max_j = j

    print("Maximum size sub-matrix is: ")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print(M[i][j], end=" ")
        print("")


def greedy_kadane_solve(matrix):

    aux = auxiliary(matrix)

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
        # Greedy-Kadane selection
        candidate_range = irange(aux)
        purged_key = min(
            filter(lambda k: k not in candidate_range, matches), key=matches.get
        )
        print(f"  del {purged_key}  {matches[purged_key]}")
        del matches[purged_key]

        # Continue
        loops += 1

    #
    # Return solution
    solution = set(matches.keys())
    return solution

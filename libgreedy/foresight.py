import numpy as np


def greedy_ahead(matrix):

    cands = candidates(matrix)
    return cands


def candidates(matrix):
    n = matrix.shape[0]
    rank = np.zeros(n, dtype=np.int)

    for i in range(0, n):
        row = matrix[i]

        # Add tallies for each row
        for j in range(0, n):
            if row[j]:
                rank[i] += 1

    mins = np.where(rank == np.amin(rank))
    return mins

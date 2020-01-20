import numpy as np


def greedy_ahead(matrix):

    # Brute force for now
    while True:
        weaks, smallest = weak_rows(matrix)
        sub_matrices = [candidate(matrix, weak) for weak in weaks]

        for sub_matrix in sub_matrices:
            weaks, smallest = weak_rows(matrix)
        break

    return sub_matrices


def weak_rows(matrix):
    n = matrix.shape[0]
    rank = np.zeros(n, dtype=np.int)

    for i in range(0, n):
        row = matrix[i]

        # Add tallies for each row
        for j in range(0, n):
            if row[j]:
                rank[i] += 1

    smallest = np.amin(rank)
    mins = np.where(rank == smallest)
    return mins[0], smallest


def candidate(matrix, weak_index):
    matrix = np.copy(matrix)
    matrix = np.delete(matrix, weak_index, axis=0)
    matrix = np.delete(matrix, weak_index, axis=1)
    return matrix

#!/usr/bin/env python3
import sys

import numpy as np


def main(args):

    input_file = args[0]
    pairs = []
    nums = set()

    # Stream thru CSV
    for line in open(input_file):
        els = line.split(',')
        i = int(els[0])
        j = int(els[1])
        nums.add(i)
        nums.add(j)
        pairs.append((i, j))

    # Create matrix
    n = len(nums)
    matrix = np.zeros((n, n), dtype=np.byte,)

    # Inject 1s
    for p in pairs:
        i = p[0]
        j = p[1]
        matrix[i][j] = 1

    # Make symmetric
    for i in range(0, matrix.shape[0]):
        row = matrix[i]
        for j in range(0, matrix.shape[0]):
            if not row[j]:
                matrix[j][i] = 0

    # Save to disk
    np.savetxt(f"matrix.csv", matrix, fmt="%i", delimiter=",")


# Make script executable
if __name__ == '__main__':
    main(sys.argv[1:])

#!/usr/bin/env python3

import sys
from random import random

import numpy as np


def gen_matrix(n, ):
    """ Generates relative i,j CSV format with missing entirs, like ESRI/Arc """

    # Get input args
    if len(args) > 0:
        n = int(args[0])
        missing_perc = float(args[1])
    else:
        n = 5
        missing_perc = 0.1

    # Create the matrix
    matrix = np.ones((n, n), dtype=np.byte,)

    # Inject missing values
    for i in range(0, n):
        for j in range(0, n):
            if random() < missing_perc:
                matrix[i][j] = 0
                # TODO - comment out for real tests
                matrix[j][i] = 0
    # For convenience
    np.fill_diagonal(matrix, 1)

    # Write to CSV file
    np.savetxt(
        f"resources/problems/{n}x{n}-{missing_perc}.csv",
        matrix,
        fmt="%i",
        delimiter=",",
    )
    np.fill_diagonal(matrix, 0)
    np.savetxt(
        f"resources/problems/{n}x{n}-{missing_perc}.0.csv",
        matrix,
        fmt="%i",
        delimiter=",",
    )


# Main script executable
if __name__ == "__main__":
    main(sys.argv[1:])

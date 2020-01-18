#!/usr/bin/env python3

import sys
from random import random

import numpy as np


def main(args):
    """ Generates relative i,j CSV format with missing entirs, like ESRI/Arc """

    if len(args) > 0:
        n = int(args[0])
        missing_perc = float(args[1])
    else:
        n = 300
        missing_perc = 0.04

    # Create the matrix
    matrix = np.ones((n, n), dtype=np.byte,)

    # Inject missing values
    for i in range(0, n):
        for j in range(0, n):
            if random() < missing_perc:
                matrix[i][j] = 0
                # matrix[j][i] = 0

    # Write to CSV file
    np.savetxt(f'resources/_{n}x{n}-{missing_perc}.csv', matrix, fmt='%i', delimiter=',')

    # Auxilary format
    rows = []
    for i in range(0, n):
        for j in range(0, n):
            if random() > missing_perc:
                rows.append(f'{i},{j}')

    # with open(f'resources/{n},{n}.csv', 'w+') as f:
    with open(f'resources/{n}-{missing_perc}.csv', 'w+') as f:
        for row in rows:
            f.writelines(row + '\n')


# Main script executable
if __name__ == '__main__':
    main(sys.argv[1:])

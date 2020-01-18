#!/usr/bin/env python3

import json
from random import random

import numpy as np

# Create the matrix
n = 21
missing_perc = 0.04

matrix = np.zeros((n, n), dtype=np.byte,)

for i in range(0, n):
    for j in range(0, n):
        if random() > missing_perc:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

# open('matrix.txt', 'w+').write(json.dump(matrix))
np.savetxt('matrix.txt', matrix, fmt='%i')

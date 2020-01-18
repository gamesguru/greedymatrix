#!/usr/bin/env python3

import json
from random import random

import numpy as np

# Create the matrix
n = 21
missing_perc = 0.04

matrix = np.ones((n, n), dtype=np.byte,)

# Inject missing values
for i in range(0, n):
    for j in range(0, n):
        if random() < missing_perc:
            matrix[i][j] = 0
            matrix[j][i] = 0

# Write to CSV file
np.savetxt(f'{n}x{n}.csv', matrix, fmt='%i', delimiter=',')

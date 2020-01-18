#!/usr/bin/env python3

import csv

# Get pairs and singles
nums = set()
pairs = set()

with open('small.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        i = int(row[2])
        j = int(row[3])
        pairs.add((i, j))
        nums.add(i)
        nums.add(j)

# Find max
n = max(nums)

# Remove compliments
for i in range(0, n):
    for j in range(0, n):
        pair = (i, j)
        anti_pair = (j, i)
        if not pair in pairs and anti_pair in pairs:
            print(anti_pair)
            pairs.remove(anti_pair)

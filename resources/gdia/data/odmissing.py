#!/usr/bin/env python3

import csv
import sys

# dist = {}
nums = set()
pairs = set()
with open("durations.csv") as f:
    reader = csv.reader(f)

    # Iterate, build the list of nums and the dict(): `orig: set(dests)`
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        i += 1
        o = int(row[0])
        d = int(row[1])
        nums.add(o)
        nums.add(d)
        pairs.add((o, d))

# Show memory usage (MB)
print(sys.getsizeof(nums) / 1000 / 1000)
print(sys.getsizeof(pairs) / 1000 / 1000)

# Print missing
for num1 in nums:
    for num2 in nums:
        if num1 == num2:
            continue
        if not (num1, num2) in pairs:
            print(f"{num1},{num2}")

#!/usr/bin/env python3

import csv
import sys

nums = set()
pairs = set()
with open('small.csv') as f:
    reader = csv.reader(f)

    # Iterate, build the list of nums and the dict(): `orig: set(dests)`
    for row in reader:
        o = int(row[2])
        d = int(row[3])
        nums.add(o)
        pairs.add((o, d))
nums = [i for i in range(1, max(nums) + 1)]
print(len(pairs))

# Show memory usage (MB)
# print(sys.getsizeof(nums) / 1000 / 1000)
# print(sys.getsizeof(pairs) / 1000 / 1000)

# Print missing
# print(nums)
for num1 in nums:
    for num2 in nums:
        # Skip identity
        if num1 == num2:
            continue
        p1 = (num1, num2)
        p2 = (num2, num1)

        # Remove missing
        if not p1 in pairs:
            try:
                pairs.remove(p2)
                # print(p2)
            except:
                pass
        elif not p2 in pairs:
            try:
                pairs.remove(p1)
                # print(p1)
            except:
                pass

# print(len(pairs))
# Good rows must have n-1 columns?

pdict = {}
# print(pairs)
# print(sorted(pairs, key=lambda x: x[0]))
for row in sorted(pairs, key=lambda x: x[0]):

    print(row)
    # srow = sorted(row, key=lambda x: x[0])
    srow = list(sorted(row))
    k = srow[0]
    v = srow[1]
    if not k in pdict:
        pdict[k] = []
    pdict[k].append(v)

for row in pdict.values():
    print(row)

# vals = sorted(pdict.values(), key=lambda x: x[0])
# for row in pdict.values():
#     print(row)

# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
#       for row in pairs]))
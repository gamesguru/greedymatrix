#!/usr/bin/env python3

import csv

# Get pairs and singles
nums = set()
pairs = set()

print("Read in CSV")
# Read in
with open("small.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        i = int(row[2])
        j = int(row[3])
        pairs.add((i, j))
        nums.add(i)
        nums.add(j)

# Find max
n = max(nums)
print(n)

print("Prune compliments")
# Remove compliments
for i in range(0, n):
    for j in range(0, n):
        pair = (i, j)
        anti_pair = (j, i)
        if not pair in pairs and anti_pair in pairs:
            pairs.remove(anti_pair)

print(len(pairs))

matches = {i: 0 for i in range(min(nums), n)}
# Apply Greedy
# while len(matches) > min(matches.values()):
while True:

    print(f"[CONTINUE] {len(matches)} > {min(matches.values())}")
    matches = {i: 0 for i in matches.keys()}
    print(f"\nIterate..")
    for pair in pairs:
        k = pair[0]
        v = pair[1]
        # Tally matches
        if k in matches and v in matches:
            matches[k] += 1
    
    print(f"{len(matches)} stops remaining")

    k = min(matches, key=matches.get)
    v = matches[k]
    floor = v

    print("Prune weakest links")
    while matches[k] == floor:
        print(f"  del {k}  ({matches[k]} occurances)")
        del matches[k]
        k = min(matches, key=matches.get)
        v = matches[k]

    # Re-iterate
    matches = {i: 0 for i in matches.keys()}
    print(f"\nRe-iterate..")
    for pair in pairs:
        k = pair[0]
        v = pair[1]
        # Tally matches
        if k in matches and v in matches:
            matches[k] += 1

    print(f"..done!  {len(matches)} remaining")
    # TODO - retally..
    if len(matches) > min(matches.values()):
        break

print(list(matches.keys()))

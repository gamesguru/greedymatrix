#!/usr/bin/env python3

import csv


# Get pairs and singles
nums = set()
pairs = set()


print("Read in CSV")
# Read in
with open("large.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        i = int(row[2])
        j = int(row[3])
        pairs.add((i, j))
        nums.add(i)
        nums.add(j)


# Find max
n = max(nums)
print(f"Num stops: {n}\n")


print("Prune compliments")
# Remove compliments
for i in range(0, n):
    for j in range(0, n):
        pair = (i, j)
        anti_pair = (j, i)
        if not pair in pairs and anti_pair in pairs:
            pairs.remove(anti_pair)

print(f"Post pruning: {len(pairs)} entries")
print(
    """
--------------------
Begin GREEDY algo
--------------------
"""
)

# Init dict
matches = {i: 0 for i in range(min(nums), n)}

# Apply Greedy
loops = 1
while True:

    print(f"\n\n==> ITERATION #{loops}")
    # Restart tallies
    matches = {i: 0 for i in matches.keys()}

    # Tallies
    for i, j in pairs:
        if i in matches and j in matches:
            matches[i] += 1
    print(f"{len(matches)} stops remaining")

    k = min(matches, key=matches.get)
    v = matches[k]
    floor = v

    # Break if square
    if all(x == floor for x in matches.values()):
        print(
            f"""
----------------------------------
DONE: all have {floor} matches!
----------------------------------
"""
        )
        break

    print("Prune weakest links")
    # Greedy selection
    while matches[k] == floor:
        print(f"  del {k}  ({matches[k]} occurances)")
        del matches[k]
        k = min(matches, key=matches.get)
        v = matches[k]

    # Continue
    loops += 1


print(list(matches.keys()))


# print(f"[CONTINUE] {len(matches)} > {min(matches.values())}")
# matches = {i: 0 for i in matches.keys()}
# print(f"\nIterate..")
# for pair in pairs:
#     k = pair[0]
#     v = pair[1]
#     # Tally matches
#     if k in matches and v in matches:
#         matches[k] += 1

# print(f"{len(matches)} stops remaining")

# k = min(matches, key=matches.get)
# v = matches[k]
# floor = v

# print("Prune weakest links")
# while matches[k] == floor:
#     print(f"  del {k}  ({matches[k]} occurances)")
#     del matches[k]
#     k = min(matches, key=matches.get)
#     v = matches[k]

# # Re-iterate
# matches = {i: 0 for i in matches.keys()}
# print(f"\nRe-iterate..")
# for pair in pairs:
#     k = pair[0]
#     v = pair[1]
#     # Tally matches
#     if k in matches and v in matches:
#         matches[k] += 1

# print(f"..done!  {len(matches)} remaining")
# # TODO - retally..
# if len(matches) > min(matches.values()):
#     break

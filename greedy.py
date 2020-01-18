#!/usr/bin/env python3

import sys
import csv
import time

import numpy as np


def main(args):

    # Get pairs and singles
    nums = set()
    pairs = set()

    if len(args) > 0:
        input_file = args[0]
        if len(args) > 1:
            o_index = int(args[1])
            d_index = int(args[2])
        else:
            o_index = 0
            d_index = 1
    else:
        input_file = "resources/5-0.1.csv"
        o_index = 0
        d_index = 1

    # Read in
    print("Read in CSV")
    with open(input_file) as f:
        reader = csv.reader(f)
        for row in reader:
            i = int(row[o_index])
            j = int(row[d_index])
            pairs.add((i, j))
            nums.add(i)
            nums.add(j)

    # Find max
    n = len(nums)
    m = max(nums)
    print(
        f"""Pre-pruning
    Span:  {n}
    Max:   {m}
    Miss:  {[x for x in range(0, m) if not x in nums]}
    Pairs: {len(pairs)}
    """
    )
    print(f"Num stops: {n}\n")

    # Remove compliments
    print("Prune compliments")
    for i in nums:
        for j in nums:
            pair = (i, j)
            anti_pair = (j, i)
            if not pair in pairs and anti_pair in pairs:
                pairs.remove(anti_pair)
    print(f"Post pruning: {len(pairs)} entries")

    # Create the matrix
    matrix = np.zeros((n, n), dtype=np.byte,)
    for p in pairs:
        i = p[0]
        j = p[1]
        # Set cell True
        matrix[i][j] = 1
    del pairs

    print(
        """
--------------------
Begin GREEDY algo
--------------------
    """
    )

    # Init dict
    matches = {i: 0 for i in nums}

    for i in matches.keys():
        row = matrix[i]

        for j in matches.keys():
            if row[j]:
                # Symmetric, so only sum rows
                matches[i] += 1

    # Apply Greedy
    loops = 1
    purged_key = None
    while True:

        # Restart tallies
        print(f"\n\n==> ITERATION #{loops}")

        #
        # Tallies
        if purged_key:
            t0 = time.time()
            for key in matches.keys():
                row = matrix[key]
                if row[purged_key]:
                    # We lost a 1, so detract from the match
                    matches[key] -= 1
            print(f"{time.time() - t0} s")

        #
        # Purged keys
        purged_key = None

        #
        # Break if square
        if all(x == len(matches) for x in matches.values()):
            print(
                f"""
----------------------------------
DONE: all have {len(matches)} matches!
----------------------------------
    """
            )
            break

        #
        # Greedy selection
        print("Prune weakest links")
        purged_key = min(matches, key=matches.get)
        print(f"  del {purged_key}  ({matches[purged_key]} occurances)")
        del matches[purged_key]

        # Continue
        loops += 1

    #
    #
    # Print solution
    solution = set(matches.keys())
    print(solution)

    # Stream output to new CSV
    print("\n==> Streaming new filtered CSV")
    with open(input_file.replace(".csv", ".filtered.csv"), "w+") as csv_out:
        writer = csv.writer(csv_out)

        # Read in
        with open(input_file) as csv_in:
            reader = csv.reader(csv_in)

            for row in reader:
                i = int(row[o_index])
                j = int(row[d_index])
                # Add only members of the square solution
                if i in solution and j in solution and i != j:
                    writer.writerow(row)


# Main script executable
if __name__ == "__main__":
    main(sys.argv[1:])

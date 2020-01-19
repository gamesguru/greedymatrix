#!/usr/bin/env python3
import sys
import csv

file = sys.argv[1]

o_index = 0
d_index = 1

nums = {}

print("Read in CSV")
with open(file) as in_f:
    reader = csv.reader(in_f)
    for row in reader:
        i = int(row[o_index])
        j = int(row[d_index])
        # Add e.g. 100 --> 97, map original index to reduced
        if not i in nums:
            nums[i] = len(nums)

# Print reverse dict
print({v: k for k, v in nums.items()})

print("Read in CSV, again, ugh..")
with open(file.replace(".csv", ".mapped.csv"), "w+") as out_f:
    writer = csv.writer(out_f)

    with open("large.csv") as in_f:

        reader = csv.reader(in_f)
        for row in reader:
            i = int(row[o_index])
            j = int(row[d_index])
            # Set to reduce-mapped value
            row[o_index] = nums[i]
            row[d_index] = nums[j]
            # Write out
            writer.writerow(row)

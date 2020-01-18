#!/usr/bin/env python3

import csv

nums = {}

print("Read in CSV")
with open("large.csv") as in_f:
    reader = csv.reader(in_f)
    for row in reader:
        i = int(row[2])
        j = int(row[3])
        # Add e.g. 100 --> 97, map original index to reduced
        if not i in nums:
            nums[i] = len(nums)

# Print reverse dict
print({v: k for k, v in nums.items()})

print("Read in CSV, again, ugh..")
with open("large.mapped.csv", "w+") as out_f:
    writer = csv.writer(out_f)

    with open("large.csv") as in_f:

        reader = csv.reader(in_f)
        for row in reader:
            i = int(row[2])
            j = int(row[3])
            # Set to reduce-mapped value
            row[2] = nums[i]
            row[3] = nums[j]
            # Write out
            writer.writerow(row)

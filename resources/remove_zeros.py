#!/usr/bin/env python3
import csv
import sys

file = sys.argv[1]
indicies = sys.argv[2].split(",")


with open(file) as source:
    reader = csv.reader(source)

    with open(file.replace(".csv", ".nonzeros.csv"), "w+") as result:
        writer = csv.writer(result)

        for row in reader:
            # Removes zeros
            non_zero = all(float(row[int(i)]) > 0 for i in indicies)
            if non_zero:
                writer.writerow(row)

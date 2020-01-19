#!/usr/bin/env python3
import sys

file = sys.argv[1]
indicies = sys.argv[2].split(",")

import csv

with open(file) as source:
    reader = csv.reader(source)

    with open(file + "-processed", "w+") as result:
        writer = csv.writer(result)

        for row in reader:
            # Removes zeros
            non_zero = all(float(row[int(i)]) > 0 for i in indicies)
            if non_zero:
                writer.writerow(row)

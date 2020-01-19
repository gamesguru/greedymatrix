#!/usr/bin/env python3
import csv
import sys

file = sys.argv[1]
indicies = sys.argv[2].split(",")


with open(file) as source:
    reader = csv.reader(source)

    with open(file.replace(".csv", ".nocolumns.csv"), "w+") as result:
        writer = csv.writer(result)

        for row in reader:
            _row = []

            # Only write desired columns out
            for i in indicies:
                _row.append(row[int(i)])
            writer.writerow(_row)

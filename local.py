#!/usr/bin/env python3
import sys

from libgreedy.greedy import solve
from libgreedy.utils import matrix_from_rel_csv


def main(args):

    if args:
        input_file = args[0]
    else:
        input_file = "resources/problems/CE.csv"

    # Make matrix and solution
    matrix = matrix_from_rel_csv(input_file)
    solution = solve(matrix)

    print(solution)

    # Stream output to new CSV

    # print("\n==> Streaming new filtered CSV")
    # with open(input_file.replace(".csv", ".filtered.csv"), "w+") as csv_out:
    #     writer = csv.writer(csv_out)

    #     # Read in
    #     with open(input_file) as csv_in:
    #         reader = csv.reader(csv_in)

    #         for row in reader:
    #             i = int(row[o_index])
    #             j = int(row[d_index])
    #             # Add only members of the square solution
    #             if i in solution and j in solution and i != j:
    #                 writer.writerow(row)


# Make script executable
if __name__ == "__main__":
    main(sys.argv[1:])

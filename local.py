#!/usr/bin/env python3
import sys

from .test_greedy import test_rel_csv

def main(args):
    input_file = args[0]
    test_rel_csv(input_file)

# Make script executable
if __name__ == '__main__':
    main(sys.argv[1:])
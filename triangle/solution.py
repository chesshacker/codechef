#! /usr/bin/env python3
import sys

# Timelimit exceeded in CodeChef.  But I looked, and no one had a Python
# program fast enough to pass whatever time limit they have set.  I'm
# beginning to think CodeChef is anti-Python

def gets():
    return sys.stdin.buffer.readline()

num_problems = int(gets())
for problem_number in range(num_problems):
    num_rows = int(gets())
    # assuming num_rows is greater than zero
    row_totals = []
    for row_number in range(num_rows):
        # Transform the previous row_totals into a list that can be added to
        # the current row... basically pair values up and determine their max
        # but the start and end must be handled with care since they don't have
        # a pair to max with.  I just insert zeros so they can be paired
        row_totals.append(0)
        row_totals.insert(0,0)
        row_totals = list(map(max,zip(row_totals[1:],row_totals[:-1])))
        row = map(int,gets().split())
        row_totals = list(map(sum,zip(row_totals,row)))
    print(max(row_totals))

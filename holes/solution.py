#! /usr/bin/env python3
import sys

holes_in_letter = [0 for x in range(256)]
letters_with_holes = {'A':1, 'B':2, 'D':1,'O':1,'P':1,'Q':1,'R':1}
for key,value in letters_with_holes.items():
    holes_in_letter[ord(key)] = value

def count_holes(line):
    return sum(holes_in_letter[ord(c)] for c in line)

sys.stdin.readline() # ignore first line
for line in sys.stdin:
    print(count_holes(line))

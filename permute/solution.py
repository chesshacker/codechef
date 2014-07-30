#! /usr/bin/env python3
import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    permutation = list(map(int,sys.stdin.readline().split()))
    for index, value in enumerate(permutation):
        if permutation[value - 1] != index + 1:
            result = "not ambiguous"
            break
    else:
        result = "ambiguous"
    print(result)

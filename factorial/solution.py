#! /usr/bin/env python3
import sys

def z_function(n):
    result = 0
    while n >= 5:
        n //= 5
        result += n
    return result

input() # ignore first line
for line in sys.stdin:
    print(z_function(int(line)))

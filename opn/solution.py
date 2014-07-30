#! /usr/bin/env python3
import sys

sys.stdin.readline() # ignore first line
operator = []
for line in sys.stdin:
    answer = ''
    level = 0
    for c in line:
        if c.isalpha():
            answer += c
        elif c in '+-*/^':
            operator.append(c)
        elif c == ')':
            answer += operator.pop()
    print(answer)

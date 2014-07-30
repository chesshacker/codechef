#! /usr/bin/env python3
words = input().split()
withdrawl = int(words[0])
final = initial = float(words[1])
if withdrawl % 5 == 0:
    final = initial - withdrawl - 0.5
if final < 0:
    final = initial
print('{0:.2f}'.format(final))

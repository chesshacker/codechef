#! /usr/bin/env python3

# I have timed this and many other methods.  On my old laptop, it processes
# 10MB in 2.062s, which is 4.85 MB/s, almost twice as fast as the required
# 2.5 MB/s.  But it fails on CodeChef for exceeding the timelimit.

import sys

n, k = map(int,sys.stdin.buffer.readline().split())
count = sum(1 for x in map(int,sys.stdin.buffer) if x % k == 0)
print(count)

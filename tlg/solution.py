#! /usr/bin/env python3
import sys

sys.stdin.buffer.readline() # ignore
max_lead = 0
leader = None
s1 = s2 = 0
for line in sys.stdin.buffer:
    s1,s2 = list(map(sum,zip(map(int,line.split()),(s1,s2))))
    lead = abs(s1 - s2)
    if lead > max_lead:
        max_lead = lead
        leader = 1 if s1 > s2 else 2
print(leader, max_lead)

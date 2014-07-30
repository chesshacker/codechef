#! /usr/bin/env python3
import random

f = open("sample.txt","w")
lineno=3495537
divisor=random.randint(0,107)
f.write(str(lineno) + " " + str(divisor) + "\n")
for i in range(0,lineno):
    f.write(str(random.randint(0,109)) + "\n")
f.close()

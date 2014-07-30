#! /usr/bin/env python3
import random

f = open("sample.txt","w")
lineno=1000000
f.write("{}\n".format(lineno))
for i in range(0,lineno):
    f.write("{}\n".format(random.randint(0,100)))
f.close()

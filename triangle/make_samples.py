#! /usr/bin/env python3
import os
import random

with open("sample.txt","w") as f:
    testcase=random.randint(999,1001)
    f.write(str(testcase) + "\n")
    while (testcase):
        rownum=random.randint(1,99)
        f.write(str(rownum) + "\n")
        for i in range(1,rownum+1):
            for j in range(0,i):
                f.write(str(random.randint(0,99)) + " ")
            f.write("\n")
        testcase=testcase-1

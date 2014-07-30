#! /usr/bin/env python3
import io

class Factorial():
    """Factorial"""
    def __init__(self):
        self.lookup = [1]
    def get(self, n):
        biggest = len(self.lookup) - 1
        if n > biggest:
            for x in range(biggest+1,n+1):
                self.lookup.append(x * self.lookup[x-1])
        return self.lookup[n]

reader = io.open(0)
reader.readline() # ignore first line

factorial = Factorial()

for x in map(lambda line: factorial.get(int(line)),reader):
    print(x)

# math.factorial  =>   6.922s
# brute force, calculate every time  =>  14.504s
# memoize calculated result  =>  6.146s

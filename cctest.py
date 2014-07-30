#! /usr/bin/env python3
import sys
import os
import re

class Tester():
    reading_first, reading_input, reading_output = range(3)
    title_re = re.compile(r"Example[ -]*(.+)")
    def __init__(self):
        self.state = Tester.reading_first
        self.example_file = open('examples.txt','r')
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.example_file.close()
        # may close these file twice, but that's okay
        self.input_file.close()
        self.output_file.close()
    def test(self):
        while True:
            line = self.get_line()
            if line == '':
                self.done()
                break
            if self.am(Tester.reading_first) or (self.am(Tester.reading_output) and line[0:7] == "Example"):
                if self.am_not(Tester.reading_first):
                    self.done()
                title_match = Tester.title_re.findall(line)
                self.title = title_match.pop() if len(title_match) else 'Example'
                self.get_line() # empty line
                self.get_line() # Input:
                sys.stdout.write(self.title + ': ')
                self.input_file = open('in.txt', 'w')
                self.state = Tester.reading_input
            elif self.am(Tester.reading_input):
                if line != '\n':
                    self.input_file.write(line)
                else:
                    self.get_line() # Output:
                    self.output_file = open('out.txt','w')
                    self.state = Tester.reading_output
            elif self.am(Tester.reading_output):
                self.output_file.write(line)
            else:
                raise Error('unexpected state')
    def get_line(self):
        return self.example_file.readline()
    def am(self, state):
        return self.state == state
    def am_not(self, state):
        return self.state != state
    def done(self):
        self.input_file.close()
        self.output_file.close()
        os.system('./solution.py < in.txt > mine.txt')
        diff = os.system('diff mine.txt out.txt > diff.txt')
        if diff != 0:
            print('FAIL\n',diff)
            os.system('cat diff.txt')
            sys.exit()
        else:
            print('PASS')
            os.system('rm in.txt out.txt mine.txt diff.txt')
        
# main
with Tester() as tester:
    tester.test()

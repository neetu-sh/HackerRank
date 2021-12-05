'''
A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
Function Description

Complete the marsExploration function in the editor below.

marsExploration has the following parameter(s):

string s: the string as received on Earth
Returns

int: the number of letters changed during transmission
Input Format

There is one line of input: a single string, s.
'''

import math
import os
import random
import re
import sys

def marsExploration(s):
    
    counter_changed  = 0
   
    for letter in range(0,len(s),3):
        if (s[letter]!= 'S'):
            counter_changed += 1
        if s[letter + 1] != 'O':
            counter_changed += 1
        if s[letter + 2] != 'S':
            counter_changed += 1
        
    return counter_changed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()

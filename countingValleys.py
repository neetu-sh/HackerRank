'''
ountingValleys has the following parameter(s):

int steps: the number of steps on the hike
string path: a string describing the path
Returns

int: the number of valleys traversed
https://www.hackerrank.com/challenges/three-month-preparation-kit-counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

'''

import math
import os
import random
import sys
import re

def countingValleys(steps:int, path:str) -> int:
    valleys = sea_level = 0

    for step in path:
        sea_level += -(step=='D') + (step == 'U')
        valleys += (sea_level == 0) and (step =='U')
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    steps = int(input().rstrip())

    path = input()

    result = countingValleys(steps,path)
    print(result)

    fptr.write(str(result) + '\n')
    fptr.close()


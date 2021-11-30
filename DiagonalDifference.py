'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return
int: the absolute diagonal difference
'''

import math
import sys
import re
import random
import os

def diagonalDifference(arr) -> int:
    d1 = d2 = 0

    for i in range(n):
        d1 += arr[i][i]
        d2 += arr[i][n-i-1]
    return abs(d1-d2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')

    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        
    result = diagonalDifference(arr)

    print(result)

    fptr.write(str(result) + '\n')
    fptr.close()


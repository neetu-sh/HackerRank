'''
Given an array of integers and a positive integer k , determine the number of (i,j) pairs where i < j and ar[i] + ar[j] is divisible by k. 
divisibleSumPairs has the following parameter(s):
    int n: the length of array 
    int ar[n]: an array of integers
    int k: the integer divisor
Returns
- int: the number of pairs 
'''
import math
import os
import random
import re
import sys

def divisibleSumPairs(n:int, k:int, ar:list) -> int:
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i] +ar[j]) % k == 0:
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    ar = list(map(int,input().rstrip().split()))

    result = divisibleSumPairs(n,k,ar)

    print(result)
   

    fptr.write(str(result) + '\n')
    fptr.close()


'''
Given an array of integers, where all elements but one occur twice, find the unique element. 
parameter(s):

    int a[n]: an array of integers
Returns
    int: the element that occurs only once
'''

import math
import random
import re
import sys
import os

def lonelyInteger(a:list) -> int:
    '''Logic: Create a dictionary with array elements as key and their frequency as value.
        Return the key with value 1 - which means the element occurred only once in the array'''
    
    d = {}
    for item in a:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    
    for k, v in d.items():
        if v == 1:
            return k
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')

    n = int(input().strip())

    a = list(map(int,input().rstrip().split()))

    result = lonelyInteger(a)

    print(result)

    fptr.write(str(result)+ '\n')
    fptr.close()




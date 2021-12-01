'''
Alternative Sorting
Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. 
At the end, run through your counting array, printing the value of each non-zero valued index that number of times.
Challenge
Given a list of integers, count and return the number of times each value appears as an array of integers.

Function Description

Complete the countingSort function in the editor below.

countingSort has the following parameter(s):

arr[n]: an array of integers
Returns

int[100]: a frequency array
'''

import math
import os
import sys
import re
import random

def countingSort(arr: list) -> list:
    results = [0] * 100
    for item in arr:
        results[item] += 1
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')

    n = int(input().strip())
    arr = list(map(int,input().rstrip().split()))
    
    result = countingSort(arr)
    print(result)
    
    fptr.write(str(result) + "\n")
    fptr.close()

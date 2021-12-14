'''
minimumAbsoluteDifference has the following parameter(s):
int arr[n]: an array of integers

Returns
int: the minimum absolute difference found
'''

import os
import sys


def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = sys.maxsize #assign max possible value
    
    for i in range(len(arr) - 1):
        temp_min = abs(arr[i+1] - arr[i])
        if temp_min < min_diff:
            min_diff = temp_min
    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()

'''
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

Example
a = [1,1,2,2,4,4,5,5,5]

There are two subarrays meeting the criterion:[1,2,2,2]  and [4,4,5,5,5] . The maximum length subarray has 5 elements.

pickingNumbers has the following parameter(s):

int a[n]: an array of integers
Returns
int: the length of the longest subarray that meets the criterion

Constraints:
2 <= n <= 100
'''

import os

def pickingNumbers(a:list) -> int:
    max_len = 0
    counter = [0] * 101
    for i in range(len(a)):
        counter[a[i]] += 1
    
    for j in range(len(counter) - 1):
        length = counter[j] + counter[j+1]
        if max_len < length:
            max_len = length
    return max_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)
    
    fptr.write(str(result) + '\n')

    fptr.close()

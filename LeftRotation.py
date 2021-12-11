'''
rotateLeft has the following parameters:

int d: the amount to rotate by
int arr[n]: the array to rotate
Returns

int[n]: the rotated array

Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4
'''

import os

def rotateLeft(d:int, arr :list) -> list:
    left = arr[:d]
    right = arr[d:]
    return right + left

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)
    print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
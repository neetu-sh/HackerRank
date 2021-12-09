'''Given an array of stick lengths, use 3 of them to construct a non-degenerate triangle with the maximum possible perimeter. 
Return an array of the lengths of its sides as 3 integers in non-decreasing order.

If there are several valid triangles having the maximum perimeter:

Choose the one with the longest maximum side.
If more than one has that maximum, choose from them the one with the longest minimum side.
If more than one has that maximum as well, print any one them.
If no non-degenerate triangle exists, return [-1].

maximumPerimeterTriangle has the following parameter(s):

int sticks[n]: the lengths of sticks available
Returns

int[3] or int[1]: the side lengths of the chosen triangle in non-decreasing order or -1
'''

import os

def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True)
    for stick_len in range(0,len(sticks)-2):
        if sticks[stick_len] < sticks[stick_len + 1] + sticks[stick_len + 2]:
            return [sticks[stick_len + 2],sticks[stick_len + 1],sticks[stick_len]]
    return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)
    print(result)
    
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

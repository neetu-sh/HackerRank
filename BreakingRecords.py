'''breakingRecords has the following parameter(s):

    int scores[n]: points scored per game

Returns

    int[2]: An array with the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1

    is for breaking least points records.


'''

import math
import os
import random
import re
import sys

def breakingRecords(scores:list) -> list:
    min_score = max_score = scores[0]
    count = [0,0]

    for item in range(len(scores)):
        if scores[item] < min_score:
            min_score = scores[item]
            count[1] += 1
        elif scores[item] > max_score:
            max_score = scores[item]
            count[0] += 1
    return count
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

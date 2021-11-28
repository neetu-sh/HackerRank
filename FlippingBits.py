'''
You will be given a list of 32 bit unsigned integers. Flip all the bits (1-> 0 and 0 ->1) and return the result as an unsigned integer. 
Sample Input
2 
2147483647 
1 

Sample Output
2147483648 
4294967294 

Explanation
Take 1 for example, as unsigned 32-bits is 00000000000000000000000000000001 and doing the flipping 
we get 11111111111111111111111111111110 which in turn is 4294967294.
'''

import math
import os
import sys
import re
import random

def flippingBits(n:int) -> int:
    return (2**32-1)^n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        print(result)
        fptr.write(str(result) + '\n')
    fptr.close()


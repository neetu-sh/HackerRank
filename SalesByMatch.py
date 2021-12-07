'''
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example:
n = 7
ar = [1,2,1,2,1,3,2]
One pair of color 1 and 1 pair of color 2. Total pair: 2

sockMerchant has the following parameter(s):
int n: the number of socks in the pile
int ar[n]: the colors of each sock

Returns
int: the number of pairs
'''

import os

def sockMerchant(n:int,ar:list) -> int:
    d = {}
    for i in ar:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    count_pairs = 0
    for key,value in d.items():
        count_pairs += (value//2)
    
    return count_pairs

if __name__ == '__main__':
    fptr = open(os.environ['output'],'w')

    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n,ar)

    print(result)
    fptr.write(str(result)+'\n')
    fptr.close()
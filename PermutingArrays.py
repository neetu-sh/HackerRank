'''
There are two n-element arrays of integers, A and B. Permute them into some A' and B' such that the relation A'[i] + B'[i] >= k holds for all i where 0 < i < n.
TwoArrays has the following parameter(s):

int k: an integer
int A[n]: an array of integers
int B[n]: an array of integers
Returns
- string: either YES or NO
'''
import os
import sys

def twoArrays(k:int,A:list,B:list) -> None:
    A.sort()
    B.sort(reverse=True)

    for index,value in enumerate(A):
        if value + B[index] < k:
            return 'NO'
    return 'YES'

if __name__ =='__main__':
    fptr = open(os.environ['OUTPUT'],'w')

    q = int(input().strip())
    for q_itr in range(q):
        first_multi_input = input().rstrip().split()

        n = int(first_multi_input[0])
        k = int(first_multi_input[1])

        A = list(map(int,input().rstrip().split()))
        B = list(map(int,input().rstrip().split()))
        
        result = twoArrays(k,A,B)
        print(result)
        fptr.write(result+'\n')
    fptr.close()

        

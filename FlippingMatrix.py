'''
Sean invented a game involving a  2n X 2n matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times. 
The goal of the game is to maximize the sum of the elements in the  submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for  matrices, help Sean reverse the rows and columns of each matrix in the best possible way
 so that the sum of the elements in the matrix's upper-left quadrant is maximal.
 Complete the flippingMatrix function in the editor below.

flippingMatrix has the following parameters:
- int matrix[2n][2n]: a 2-dimensional array of integers

Returns
- int: the maximum sum possible.
'''

import math
import os
import random
import re
import sys

def flippingMatrix(matrix):
    result = m1 = m2 = m3 = m4 = 0
    q = len(matrix)//2

    for i in range(q):
        for j in range(q):
            
            m1 = matrix[i][2*q-j-1]
            m2 = matrix[i][j]
            m3 = matrix[2*q-i-1][j]
            m4 = matrix[2*q-i-1][2*q-j-1]

            result += max(m1,m2,m3,m4)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')

    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        matrix = []
        
        for _ in range(2*n):
            matrix.append(list(map(int,input().rstrip().split())))

        result = flippingMatrix(matrix)
        print(result)

        fptr.write(str(result) + '\n')
    fptr.close()


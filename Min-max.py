'''Problem: Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers. 
miniMaxSum has the following parameter(s):

arr: an array of 5 integers

Print two space-separated integers on one line: the minimum sum and the maximum sum of
of elements. '''

import math
import os
import random
import re
import sys


def miniMaxSum(arr:int):
   print (sum(arr)- max(arr),sum(arr) - min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

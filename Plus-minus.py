'''Problem: "Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with places after the decimal."'''

import math
import os
import random
import re
import sys


def print_ratio(count: int, length: int) -> None:
    if count == 0:
        print("{:.6f".format(count))
    else:
        print("{:.6f}".format(count/length))


def plusMinus(arr:int) -> None:
    length = len(arr)

    #initialize counters for positive, negative and zero ratios
    count_pos = count_neg = count_zero = 0

    for i in range(length):
        if arr[i] > 0:
            count_pos += 1
        elif arr[i] < 0:
            count_neg += 1
        else:
            count_zero += 1
    
    #print positive numbers ratio
    print_ratio(count_pos, length)

    #print positive numbers ratio
    print_ratio(count_neg, length)

    #print positive numbers ratio
    print_ratio(count_zero, length)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

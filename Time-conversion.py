''' Given a time in 12-hour AM/PM format, convert it to military (24-hour) time. 
TimeConversion has the following parameter(s):

    string s: a time in 12 hour format

Returns
    string: the time in 24 hour format.'''

import math
import os
import random
import re
import sys


def timeConversion(s:str) -> str:
    #get hour
    hh = int(s[:2])

    #check if AM or PM:
    if s[8:] == 'AM':
        if hh == 12:
            hh = '0'
        else:
            hh = str(hh)
    elif s[8:] == 'PM':
        if hh == 12:
            hh = '12'
        else:
            hh = str(hh + 12)
    
    return hh.zfill(2) + s[2:8]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print (result)

    fptr.write(result + '\n')

    fptr.close()

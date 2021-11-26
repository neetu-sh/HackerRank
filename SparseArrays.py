'''
Given a collection of input strings and a collection of query strings.
For each query string, determine how many times it occurs in the list of input strings.
Parameters:
    string strings[n]: array of input strings
    string queries[q]: array of query strings
Return:
    int[q]: Array of results for each query
Example:
    Input: 
    3
    aba
    baba
    aba
    2
    aba
    ab
    Output:
    2
    0
'''
import math
import os
import random
import re
import sys

def matchingStrings(strings: list, queries: list) -> list:
    '''Logic: First store the items from strings in dictionary with their frequency, then search the query items in the dictionary.
    If found, then append the result array for the query string, else assign 0.'''
    
    d = {}
    result = []

    for s in strings:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    
    for q in queries:
        if q in d:
            result.append(d[q])
        else:
            result.append(0)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)
    
    result = matchingStrings(strings, queries)

    print(result)

    fptr.write('\n'.join(map(str,result)))
    fptr.write('\n')

    fptr.close()
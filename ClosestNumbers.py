'''
Given a list of unsorted integers, arr, find the pair of elements that have the smallest absolute difference between them. 
If there are multiple pairs, find them all.
closestNumbers has the following parameter(s):

int arr[n]: an array of integers
Returns
- int[]: an array of integers as described

Sample Input 0

10
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 
Sample Output 0

-20 30
Explanation 0
(30) - (-20) = 50, which is the smallest difference.
'''

import os


def closestNumbers(arr: list) -> list:
    # sort array
    arr.sort()
    #initialize results dict
    results = {}
    # loop through arr to len(arr) -1
    for i in range(len(arr) - 1):
        #find abs difference
        diff = abs(arr[i] - arr[i+1])
        #check if diff is present in results as key
        if diff in results:
            results[diff] += [arr[i],arr[i+1]]
        else:
            results[diff] = [arr[i],arr[i+1]]
            
        
    #find min key
    min_abs = min(results.keys())
    #return value of min key
    return results[min_abs]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)
    print(result)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
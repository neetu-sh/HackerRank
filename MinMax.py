'''
Create an array arr_new of length k from arr such that:
max(arr_new) - min(arr_new) = minimum difference between the elements.
Eg:
arr = [1,4,7,2]
k = 2
minimum diff is 1 between [1,2] here.
maxMin has the following parameter(s):

int k: the number of elements to select
int arr[n]:: an array of integers
Returns

int: the minimum possible unfairness

'''
import os


def maxMin(k, arr):
    arr.sort()

    arr_new = []

    for i in range(len(arr) -k + 1):
        arr_new.append(arr[i+k-1] - arr[i])
    return min(arr_new)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()

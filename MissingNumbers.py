'''
arr =[7,2,3,4]
brr = [7,2,4,5,6,3]
missing res = [5,6]

Notes:
1)If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. 
If that is not the case, then it is also a missing number.
2)Return the missing numbers sorted ascending.
3)Only include a missing number once, even if it is missing multiple times.
4)The difference between the maximum and minimum numbers in the original list is less than or equal to 100.

missingNumbers has the following parameter(s):

int arr[n]: the array with missing numbers
int brr[m]: the original array of numbers
Returns

int[]: an array of integers
'''
import os

def missingNumbers(arr, brr):
   
    for i in arr:
        brr.remove(i)
    return sorted(list(set(brr)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)
    print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

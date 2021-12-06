'''
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

Example
s = [2,2,1,3,2]
d = 4
m = 2

Lily wants to find segments summing to Ron's birth day d=4,  with a length equal to his birth month, m=2 . 
In this case, there are two segments meeting her criteria:  [2,2] and [1,3] . 

Birthday has the following parameter(s):

int s[n]: the numbers on each of the squares of chocolate
int d: Ron's birth day
int m: Ron's birth month
Returns

int: the number of ways the bar can be divided
'''
import os

def birthday(s:list,d:int,m:int) -> int:
    count = 0
    for i in range(0,len(s)):
        if sum(s[i:m+i]) == d:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['output'],'w')

    n = int(input().strip())
    s = list(map(int,input().rstrip().split()))
    firs_multi_input = input().rstrip().split()
    d = int(firs_multi_input[0])
    m = int(firs_multi_input[1])
    result = birthday(s,d,m)
    print(result)

    fptr.write(str(result) + '\n')
    fptr.close()
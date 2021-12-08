'''Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. 
If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

Example
arr = [1,1,2,2,3]
There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.


migratoryBirds has the following parameter(s):

int arr[n]: the types of birds sighted
Returns

int: the lowest type id of the most frequently sighted birds. 
It is guaranteed that each type is 1,2,3,4, or 5.
'''
import os

def migratoryBirds(arr:list) -> int:
    count = [0] * 6
    for item in arr:
        count[item] += 1
    return count.index(max(count))
        
        

if __name__ == '__main__':
    fptr = open(os.environ['output'],'w')
    arr_count = int(input().strip())

    arr = list(map(int,input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

    fptr.write(str(result) + '\n')
    fptr.close()
'''
A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book.
 They always turn pages one at a time. When they open the book, page 1 is always on the right side:
 Example:
 n = 5, p = 3
 Given n and p, find and print the minimum number of pages that must be turned in order to arrive at page p.

 pageCount has the following parameter(s):

int n: the number of pages in the book
int p: the page number to turn to
Returns
int: the minimum number of pages to turn
'''
import os

def pageCount(n, p):
    
    return min((n//2 - p//2),p//2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
'''
A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet.
Ignore case. Return either pangram or not pangram as appropriate.
pangrams has the following parameter(s):

string s: a string to test
Returns

string: either pangram or not pangram
'''

import os
import string

def pangrams(s: str) -> str:
    alphabets = string.ascii_lowercase

    if set(alphabets) <= set(s.lower()):
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')

    s = input()

    result = pangrams(s)
    print(result)
    fptr.write(result + '\n')

    fptr.close()
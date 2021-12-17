'''
The website considers a password to be strong if it satisfies the following criteria:

Its length is at least 6 .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length n in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
int n: the length of the password
string password: the password to test
Returns

int: the minimum number of characters to add
'''

import os


def minimumNumber(n, password):
 
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    pwd_len = 6
    num = l_case = up_case = spl_char = 1
    
    for i in password:
       
        if i in numbers:
            num = 0
        if i in lower_case:
            l_case = 0
        if i in upper_case:
            up_case = 0
        if i in special_characters:
            spl_char = 0
    temp = num + l_case + up_case + spl_char
    
    return temp if temp + n > pwd_len else pwd_len - (n + temp) + temp
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)
    print(answer)
    fptr.write(str(answer) + '\n')

    fptr.close()

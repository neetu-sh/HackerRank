'''
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3 (k):    defghijklmnopqrstuvwxyzabc

caesarCipher has the following parameter(s):
string s: cleartext
int k: the alphabet rotation factor

Returns
string: the encrypted string
'''

import os
import string



def caesarCipher(s, k):
    # Write your code here
    if k == 0:
        return s
    # start with empty ciphered list
    encrypted_s = []
    #loop through the string s to get characters
    for i in range(len(s)):
        char1 = s[i]
        #check if it is alphabet:
        if char1.isalpha():
            #call rotate_char function
            char1 = rotate_char(char1,k)
            print("char1: ",char1,"type inside cipher function ",type(char1))
        #append to ciphered list
        encrypted_s.append(char1)
    return ''.join(encrypted_s)
    
def rotate_char(char1,k):
    if char1.islower():
        char1 = (ord(char1) + k - 97) % 26 + 97
    else:
        char1 = (ord(char1) + k - 65) % 26 + 65
    print("char1 inside rotate:",char1, "type is ",type(char1))
    return chr(char1)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)
    fptr.write(result + '\n')

    fptr.close()

'''
Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.
Input Format

The input consists of two lines. The first line of the input contains the first string, s, and the second line contains the second string, t .
Output Format

Print the string obtained by the XOR of the two input strings in a single line.
'''

def strings_XOR(s,t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'
    return res

s = input()
t = input()

print(strings_XOR(s,t))
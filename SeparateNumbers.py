'''
separateNumbers has the following parameter:

s: an integer value represented as a string
Prints
- string: Print a string as described above. Return nothing.
'''



def separateNumbers(s):
   
    response = 'NO'
    for i in range(len(s)):
        start = int(s[:i+1])
        new_s = str(start)
        
        if len(new_s)!= len(s):
            dig = start
            while len(new_s) < len(s):
                dig += 1
                new_s += str(dig)
            if new_s == s:
                response = f"YES {start}"
                break
    print(response)

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

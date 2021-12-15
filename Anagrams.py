import os

def anagram(s):
    #check if string size is not even, then return -1
    if len(s) % 2 != 0:
        return -1
    
    #proceed otherwise
    mid = len(s)//2
    left = s[:mid]
    right = s[mid:]

    left_st = store(left)
    right_st = store(right)

    count_diff = 0

    for key in right_st.keys():
        if key not in left_st:
            count_diff += right_st[key]
        else:
            count_diff += max (0,right_st[key]-left_st[key])
    return count_diff


def store(st):
    store_dict = {}
    for char in st:
        if char not in store_dict:
            store_dict[char] = 1
        else:
            store_dict[char] += 1
    return store

if __name__ == '__main__':
    fp = open(os.environ['output'],'w')

    q = int(input().strip())

    for itr_q in range(q):
        s = input()
        result = anagram(s)

        print(result)
        fp.write(str(result) + '\n')

    fp.close()
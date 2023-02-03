import sys

n = int(sys.stdin.readline())
pattern = sys.stdin.readline().rstrip()
pattern_len=len(pattern)
pattern_lst = pattern.split("*")
left = len(pattern_lst[0])
right = len(pattern_lst[1])


for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= pattern_len-1 and word[:left] == pattern_lst[0] and word[-right:] == pattern_lst[1]:
        print("DA")
    else:
        print("NE")
    


    

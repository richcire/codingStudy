import sys

word = sys.stdin.readline().rstrip()

cnt = 0

while word:
    cnt += 1
    cnt_str = str(cnt)
    cnt_len = len(cnt_str)
    for i in range(cnt_len):
        if word[0] == cnt_str[i]:
            if len(word) == 1:
                word = ""
                break
            word = word[1:]

print(cnt)
    

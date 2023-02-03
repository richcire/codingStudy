import sys
from collections import Counter

word = sorted(list(sys.stdin.readline().rstrip()))

word_dict = Counter(word)


one = 0
answer = ""
cache = ""
for c in word_dict:
    if word_dict[c]%2 == 1:
        one +=1
        cache = c
        answer += c*(word_dict[c]//2)
        if one == 2:
            print("I'm Sorry Hansoo")
            exit(0)
    else:
        answer += c*(word_dict[c]//2)

answer = answer + cache + answer[::-1]

print(answer)




    

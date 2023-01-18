import sys

input = sys.stdin.readline
N, M = map(int,input().split())
voca = []
dict = {}
for _ in range(N):
  word = input()
  word = word[:-1]
  if len(word) >= M:
    voca.append(word)
    dict[word] = 0
    
for i in voca:
  dict[i] += 1
  
ans = sorted(dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in ans:
  print(i[0])
import sys

n, m = map(int, input().split())
memo = {}
for _ in range(n):
  voca = sys.stdin.readline().strip()
  memo[voca] = 1
  
for _ in range(m):
  text = sys.stdin.readline().strip()
  text = text.split(',')
  for i in text:
    if i in memo and memo[i] == 1:
      memo[i] = 0
      n-=1
  print(n)
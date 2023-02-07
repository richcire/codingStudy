import sys

input = sys.stdin.readline
in_n = list(input().rstrip())

names = []
sig = False
ans = ''

for i in in_n:
  if i == '<':
    sig = True
    while names:
      ans += names.pop()
    ans += i
  elif i == '>':
    sig = False
    ans += i
  elif sig:
    ans += i
  elif i == ' ':
    while names:
      ans += names.pop()
    ans += i
  else:
    names.append(i)

while names:
  ans += names.pop()
  
print(ans)
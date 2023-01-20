import sys

input = sys.stdin.readline
stack = []
ans = 0

for _ in range(int(input())):
  word = list(input())
  word = word[:-1]
  word.sort()
  if len(stack) == 0:
    stack.append(word)
  elif stack[-1] != word:
    temp = []
    for i in stack[-1]:
      if i in word:
        word.remove(i)
      else:
        temp.append(i)
    a = len(word)
    b = len(temp)
    if (a == 0 and b == 0) or (a==1 and b==0) or (b==1 and a == 0) or (a==1 and b==1): 
      ans +=1
  else:
    ans += 1    
print(ans)
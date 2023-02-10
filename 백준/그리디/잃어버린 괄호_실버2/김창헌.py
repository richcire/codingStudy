import sys


input = sys.stdin.readline().rstrip()
math_input = input

nums = []
num = ''

for i in math_input:
  if i != '-' and i != '+':
    num += i
  elif i == '-':
    nums.append(int(num))
    nums.append(i)
    num = ''
  else:
    nums.append(int(num))
    num = ''
nums.append(int(num))

ans = 0
sig = 0

for i in nums:
  if '-' == i:
    sig = 1
  if i != '-' and sig == 1:
    ans -= i
  elif i != '-' and sig == 0:
    ans += i

print(ans)
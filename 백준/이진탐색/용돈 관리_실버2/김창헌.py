import sys

input = sys.stdin.readline
N,M = map(int,input().split())

buys = []
for _ in range(N):
  buys.append(int(input()))

s = min(buys)
e = sum(buys)

while s <= e:
  mid = (s+e)//2
  money = mid
  nums = 1
  for i in buys:
    if i > money:
      money = mid
      nums += 1
    money -= i
  
  if nums > M or mid < max(buys):
    s = mid+1
  else:
    e = mid-1
    k = mid
    
print(k)

import sys

input = sys.stdin.readline

N,M = map(int, input().split())
trees = list(map(int, input().split()))

s = 1
e = max(trees)
while s<=e:
  ans = 0
  mid = (s+e)//2
  for i in trees:
    if mid < i:
      ans += i - mid
  if ans > M:
    s = mid +1
  elif ans == M:
    e = mid
    break
  else:
    e = mid -1
    
print(e)
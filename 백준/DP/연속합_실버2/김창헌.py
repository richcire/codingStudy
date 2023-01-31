import sys


input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in arr:
  if i < 0:
    cnt+=1

if cnt == n:
  print(max(arr))
else:
  for i in range(n-1):
    if arr[i] + arr[i+1] > 0:
      arr[i+1] = arr[i]+arr[i+1]
    else:
      arr[i+1] = max(arr[i]+arr[i+1], arr[i+1], 0)
      
  print(max(arr))
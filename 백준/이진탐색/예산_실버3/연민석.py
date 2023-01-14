import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

if sum(num) <= m:
  print(max(num))
  exit(0)

start, end = 1, m
# mid = 0

while start <= end:
  mid = (start + end) // 2
  yesan = 0
  for i in num:
    if i > mid:
      yesan += mid
    else:
      yesan += i

  if yesan == m:
    print(mid)
    exit(0)
  elif yesan < m:
    start = mid + 1
  else:
    end = mid - 1

print(end)

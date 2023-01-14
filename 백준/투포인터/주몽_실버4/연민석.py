import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
num.sort()

num_reverse = num[::-1]

start = 0
end = 0

answer = 0

while start + end + 2 <= n:
  a = num[start]
  b = num_reverse[end]
  if a + b == m:
    answer += 1
    start += 1
    end += 1
  elif a + b < m:
    start += 1
  else:
    end += 1


print(answer)

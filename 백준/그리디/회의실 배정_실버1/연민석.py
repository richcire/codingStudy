import sys

a = int(sys.stdin.readline())

m = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]


m.sort(key=lambda x: (x[1], x[0]))

start = 0
end = 0

answer = 0

for i in m:
  if i[0] >= end:
    answer += 1
    start = i[0]
    end = i[1]

print(answer)

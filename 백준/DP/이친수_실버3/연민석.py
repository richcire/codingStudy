import sys

a = int(sys.stdin.readline())

pinary = [(0,0),(1,0),(0,1)]

if a < 3:
  print(sum(pinary[a]))
  exit(0)

for i in range(3,a+1):
  pinary.append((pinary[-1][1], sum(pinary[-1])))

print(sum(pinary[-1]))

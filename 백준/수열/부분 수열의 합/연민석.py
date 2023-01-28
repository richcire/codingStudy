import sys
from itertools import combinations

n, target = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(1, n+1):
    for j in combinations(lst, i):
        if sum(j) == target:
            answer += 1

print(answer)

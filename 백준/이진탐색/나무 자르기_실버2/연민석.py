import sys
from bisect import bisect_left

n, a = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    get = 0
    for t in trees:
        if t > mid:
            get += t - mid
    if get < a:
        end = mid - 1
    else:
        start = mid + 1

print(end)

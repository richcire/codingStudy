import sys

k, n = map(int, sys.stdin.readline().split())

lansuns = []

for _ in range(k):
    lansuns.append(int(sys.stdin.readline()))

end = max(lansuns)
start = 1

while start <= end:
    mid = (start + end) // 2
    get = 0
    for i in lansuns:
        get += i // mid
    if get < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)

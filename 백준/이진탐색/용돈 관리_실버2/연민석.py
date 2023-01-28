import sys

n, m = map(int, sys.stdin.readline().split())

plan = []

for _ in range(n):
    plan.append(int(sys.stdin.readline()))

min_val = max(plan)
start = min_val
end = sum(plan)


while start < end:
    mid = (start+end)//2

    cnt = 1
    leftover = mid
    for p in plan:
        if leftover >= p:
            leftover -= p
        else:
            cnt += 1
            leftover = mid - p

    if cnt <= m:
        end = mid
    else:
        start = mid + 1
        

print(end)

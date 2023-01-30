import sys

n = int(sys.stdin.readline())

line = [n]*n

seq = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    cnt = 0
    target = seq[i-1]
    for idx,j in enumerate(line):
        if j > i:
            if target == cnt:
                line[idx] = i
                break
            else:
                cnt += 1

print(' '.join(map(str, line)))

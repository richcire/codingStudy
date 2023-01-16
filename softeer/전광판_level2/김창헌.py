import sys

memo = [[1,1,1,0,1,1,1],[0,0,1,0,0,1,0],[1,0,1,1,1,0,1],[1,0,1,1,0,1,1],[0,1,1,1,0,1,0],[1,1,0,1,0,1,1],[1,1,0,1,1,1,1],[1,1,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1],[0,0,0,0,0,0,0]]
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    A, B = input().split()
    A=list(A)
    B=list(B)

    ans = 0
    if len(A)>len(B):
        n = len(A)-len(B)
        B = ['-1']*n+B
    elif len(B)>len(A):
        n = len(B)-len(A)
        A = ['-1']*n+A
    for a,b in zip(A,B):
        for ai, bi in zip(memo[int(a)], memo[int(b)]):
            if ai != bi:
                ans += 1
    print(ans)
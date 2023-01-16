import sys
N, K = map(int, input().split())
score = list(map(int,input().split()))

for _ in range(K):
    A,B = map(int,input().split())
    ans = round(sum(score[A-1:B])/len(score[A-1:B]), 2)
    print(ans)
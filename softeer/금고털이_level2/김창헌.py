import sys

W, N = map(int, input().split())
List = []

for _ in range(N):
    M, P = map(int, input().split())
    List.append([M,P])

List.sort(key=lambda x: x[1], reverse=True)
ans = 0

for i in List:
    if i[0] < W:
        ans+=i[1]*i[0]
        W = W-i[0]
    elif i[0] >= W:
        ans += i[1]*W
        break

print(ans)
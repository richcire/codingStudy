import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    starr = []
    for _ in range(2):
        temp = list(map(int, input().split()))
        starr.append(temp)

    for i in range(1, n):
      if i == 1:
        starr[0][i] += starr[1][i-1]
        starr[1][i] += starr[0][i-1]
      else:
        starr[0][i] += max(starr[1][i-1], starr[1][i-2])
        starr[1][i] += max(starr[0][i-1], starr[0][i-2])
  
    print(max(starr[0][-1],starr[1][-1]))
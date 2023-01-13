import sys

input = sys.stdin.readline
H, W = map(int,input().split())

sky = [list(input()) for _ in range(H)]
maps = [[-1]*W for _ in range(H)]

for i in range(H):
  sig = -1
  for j in range(W):
    if sky[i][j] == 'c':
      print(0, end=' ')
      sig = j
    elif sig > -1:
      print(j-sig, end=' ')
    else:
      print(-1, end=' ')
  print()
A, B = map(int, input().split())
ans = 1

while True:
  if B == A or B == 1:
    if B == A:
      print(ans)
    else:
      print(-1)
    break
  if B % 10 == 1:
    B = B // 10
    ans +=1
  elif B % 2 == 0:
    B = B // 2
    ans +=1
  else:
    print(-1)
    break


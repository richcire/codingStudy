N, K = map(int, input().split())

ele = []
for _ in range(N):
  ele.append(int(input()))

s = 1
e = max(ele)

while s <= e:
  m = (s+e)//2
  cnt = 0
  for i in ele:
    cnt += i//m
  
  if cnt < K:
    e = m - 1
  else:
    s = m + 1
    
print(e)


  
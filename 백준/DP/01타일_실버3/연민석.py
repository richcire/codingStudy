a = int(input())

dp=[0,1,2]


if a == 1:
  print(1)
  exit(0)
if a == 2:
  print(2)
  exit(0)

for i in range(3,a+1):
  dp.append((dp[-1]+dp[-2]) % 15746)

print(dp[-1])

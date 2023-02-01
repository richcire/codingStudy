import sys

n = int(input())

in_car = {}
for i in range(n):
    num = sys.stdin.readline().strip()
    in_car[num] = i

out_car = []
for i in range(n):
    num = sys.stdin.readline().strip()
    out_car.append(num)
  
ans = 0
for i in range(n-1):
  for j in range(i+1, n):
    if in_car[out_car[i]] > in_car[out_car[j]]:
      ans += 1
      break
      
print(ans)

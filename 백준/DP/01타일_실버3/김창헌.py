fibo = [0] * 1000000

fibo[0] = 1
fibo[1] = 2

N = int(input())
if N == 1:
  print(1)
elif N == 2:
  print(2)
else:
  for i in range(2, N):
    fibo[i] = (fibo[i-2] + fibo[i-1])%15746
  
  print(fibo[N-1])
  
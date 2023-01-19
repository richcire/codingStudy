def change(idx):
  if state[idx] == 0:
    state[idx] = 1
  else:
    state[idx] = 0

N = int(input())
state = [-1] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    sig, num = map(int, input().split())
    if sig == 1:
      for i in range(num, N+1, num):
        change(i)
    else:
      for i in range(1, N//2):
        if num-i<0 or num+i>N:
          break
        if state[num-i] != state[num+i]:
          break
        change(num-i)
        change(num+i)
      change(num)
        
cnt = 0
for i in state[1:]:
  print(i, end=' ')
  cnt += 1
  if cnt == 20:
    cnt = 0
    print()
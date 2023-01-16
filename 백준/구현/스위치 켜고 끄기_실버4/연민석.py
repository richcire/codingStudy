import sys

switch_num = int(sys.stdin.readline())
switch = [0] + list(map(int, sys.stdin.readline().split()))
people_num = int(sys.stdin.readline())
people = []

for _ in range(people_num):
  people.append(list(map(int, sys.stdin.readline().split())))

for person in people:
  
  idx = person[1]
  if person[0] == 1:
    while idx <= switch_num:
      if switch[idx] == 0:
        switch[idx] = 1
      else:
        switch[idx] = 0
      idx += person[1]
  else:
    limit = min(idx-1, switch_num-idx)
    for j in range(0, limit+1):
      if switch[idx-j] == switch[idx+j]:
        if switch[idx-j] == 0:
          switch[idx-j] = 1
          switch[idx+j] = 1
        else:
          switch[idx-j] = 0
          switch[idx+j] = 0

      else:
        break

for i, num in enumerate(switch):
  if i == 0:
    continue
  print(num, end=" ")
  if i % 20 == 0:
    print()


import sys


input = sys.stdin.readline
for _ in range(int(input())):
  people = []
  for _ in range(int(input())):
    s1, s2 = map(int, input().split())
    people.append([s1,s2])
  people.sort(key = lambda x : x[0])
  man = people[0][1]
  ans = 1
  for i in range(1, len(people)):
    if man > people[i][1]:      
      man = people[i][1]
      ans += 1
  print(ans)
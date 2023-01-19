import sys

input = sys.stdin.readline
P, M = map(int,input().split())
rooms = []

for _ in range(P):
  player, nick = input().split()
  rooms.append([player, nick])

level = 0
ans = []
x = 0

while rooms:
  room = []
  na = []
  for idx, i in enumerate(rooms):
    player, nick = i[0], i[1]
    if len(room) == 0:
      room.append([player, nick])
      level = int(player)
    elif len(room) < M and level-10 <= int(player) and int(player)<= level+10:
        room.append([player, nick])
    else:
      na.append(rooms[idx])

  room.sort(key=lambda x : x[1])
  ans.append(room)
  rooms = na

  
for i in ans:
  if len(i) == M:
    print("Started!")
  else:
    print("Waiting!")
  for j in i:
    print(j[0], j[1])
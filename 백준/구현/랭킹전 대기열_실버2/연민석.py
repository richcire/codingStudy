
import sys

p, m = map(int, sys.stdin.readline().split())

rooms = []

for _ in range(p):
    level, name = sys.stdin.readline().split()
    level = int(level)
    entered = False
    for i in rooms:
        if -10 <= i[0][0] - level <= 10 and len(i) < m:
            i.append((level, name))
            entered = True
            break
    if entered == False:
        rooms.append([(level, name)])


for room in rooms:
    if len(room) == m:
        print("Started!")
        for name in sorted(room, key= lambda x:x[1]):
            print(name[0], name[1])
    else:
        print("Waiting!")
        for name in sorted(room, key= lambda x:x[1]):
            print(name[0], name[1])


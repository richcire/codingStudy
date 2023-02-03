import sys

n = int(sys.stdin.readline())

cars = {}

for i in range(n):
    cars[sys.stdin.readline().rstrip()] = i

checklist = []
answr = 0

for i in range(n):
    checklist.append(sys.stdin.readline().rstrip())

for idx, car in enumerate(checklist):
    for j in range(idx+1, n):
        if cars[car] > cars[checklist[j]]:
            answr += 1
            break
print(answr)

    

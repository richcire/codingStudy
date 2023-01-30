import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

A = deque(map(int, sys.stdin.readline().split()))

length = 2*N
robot = deque([0]*length)

stage = 0

while A.count(0) < K:

    stage += 1

    A.appendleft(A.pop())
    robot.appendleft(robot.pop())
    robot[N-1] = 0
    

    for i in range(N-2,-1,-1):
        if robot[i] == 1 and A[i+1] > 0 and robot[i+1]==0:
            if i == N-2:
                robot[i] = 0
                A[i+1] -= 1
            else:
                robot[i] = 0
                robot[i+1] = 1
                A[i+1] -= 1

    
    
    if A[0] > 0:
        robot[0] = 1
        A[0] -= 1

print(stage)
    
    
    

        

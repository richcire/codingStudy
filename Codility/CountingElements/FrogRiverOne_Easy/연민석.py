def solution(X, A):
    # Implement your solution here
    road = 0
    visited = {key:0 for key in range(1,X+1)}
    for i in range(len(A)):
      pos = A[i]
      if visited[pos] == 1:
        continue
      visited[pos] = 1
      road += 1
      if road == X:
        return i
    
    return -1
    

    pass

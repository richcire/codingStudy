def solution(A):
    # Implement your solution here
    a_len = len(A)
    result = [0] + [0]*a_len

    for i in A:
      if result[i] == 1:
        return 0
      result[i] = 1
    
    for i in result:
      if i == 0:
        return 0
      
    return 1

    pass

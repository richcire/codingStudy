def solution(X, A):
    sig = [0] * X
    s = 0

    for i in range(len(A)):
        if sig[A[i]-1] == 0:
            sig[A[i]-1] = 1
            s += 1
            if s == X:
                return i
    return -1
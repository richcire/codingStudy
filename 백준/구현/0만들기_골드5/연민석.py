import sys
from itertools import product

sets = [" ", "+", "-"]

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    numbers = list(map(str, range(1,num+1)))
    hubo = product(sets, repeat = num-1)
    
    
    for i in hubo:
        evaluation = ""
        for j in range(num-1):
            evaluation += numbers[j]
            evaluation += i[j]
        evaluation += numbers[-1]
        eval_nospace = evaluation.replace(" ", "")
        if eval(eval_nospace) == 0:
            print(evaluation)
    print()

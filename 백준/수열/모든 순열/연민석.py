import sys
from itertools import permutations

n = int(sys.stdin.readline())

for i in permutations(range(1,n+1)):
    print(' '.join(map(str, i)))

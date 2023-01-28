import sys


input = sys.stdin.readline
n = int(input())
sig = input()
sig = sig[:-1]
sig = sig.split('*')
s, e = len(sig[0]), len(sig[1])

for _ in range(n):
  name = list(input())
  name = name[:-1]
  f = ''.join(name[:s])
  b = ''.join(name[len(name)-e:])
  
  if sig[0] == f and b == sig[1] and len(name) >= s+e:
    print('DA')
  else:
    print('NE')
  
        
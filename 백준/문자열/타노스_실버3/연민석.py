import sys

word = list(sys.stdin.readline().rstrip())

zero = word.count("0")//2
one = word.count("1")//2

for _ in range(zero):
    word.pop(-word[::-1].index("0")-1)
for _ in range(one):
    word.pop(word.index("1"))

print(''.join(word))

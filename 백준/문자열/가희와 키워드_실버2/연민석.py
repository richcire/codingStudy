import sys

N, M = map(int, sys.stdin.readline().split())

keywords = set([])

for _ in range(N):
    keywords.add(sys.stdin.readline().rstrip())

for _ in range(M):
    notes = set(sys.stdin.readline().rstrip().split(","))
    keywords -= notes
    print(len(keywords))

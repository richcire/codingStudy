import sys

input = sys.stdin.readline
n, m = map(int, input().split())
lecture = list(map(int, input().split()))

ans = 0
s = max(lecture)
e = sum(lecture)
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    temp = 0
  
    for i in lecture:
      if temp+i > mid:
        temp = 0
        cnt+=1
      temp += i
    
    if temp != 0:
      cnt+=1
    
    if cnt > m:
        s = mid + 1
    else:
        e = mid - 1
      
print(s)

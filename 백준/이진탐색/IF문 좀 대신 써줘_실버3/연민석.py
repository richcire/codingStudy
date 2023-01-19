import sys

n, m = map(int,sys.stdin.readline().split())

standard_num = [-1]
standard_name = ["none"]

for _ in range(n):
    name, num = sys.stdin.readline().rstrip().split()
    standard_name.append(name)
    standard_num.append(int(num))

for _ in range(m):
    a = int(sys.stdin.readline())
    start = 1
    end = n
    
    while start <= end:
        mid = (end + start) // 2
        if standard_num[mid-1] < a <= standard_num[mid]:
            end = mid
            break
        elif standard_num[mid-1] >= a:
            end = mid - 1
        else:
            start = mid + 1
    print(standard_name[end])


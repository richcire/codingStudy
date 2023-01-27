import sys
import difflib

n = int(sys.stdin.readline())
target = sys.stdin.readline().rstrip()
target = ''.join(sorted(target, key=str.lower))
answer = 0



for _ in range(n-1):
    word = sys.stdin.readline().rstrip()
    word = ''.join(sorted(word, key=str.lower))

    difference = 0
    use = 0
    
    for i,s in enumerate(difflib.ndiff(target, word)):
        if s[0]==' ': continue
        elif s[0]=='-':
            difference -= 1
            use += 1
            if use == 3:
                break
        elif s[0]=='+':
            difference += 1
            use += 1
            if use == 3:
                break
            
        if difference < -1 or difference > 1:
            break
    
    if -1 <= difference <= 1 and use < 3:
        answer+=1

print(answer)


            





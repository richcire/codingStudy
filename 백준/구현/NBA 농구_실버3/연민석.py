import sys

n = int(sys.stdin.readline())

a_score = 0
b_score = 0
last_time = 0
a_result = 0
b_result = 0

for _ in range(n):
    team, time = sys.stdin.readline().rstrip().split()
    min, sec = map(int, time.split(":"))
    curr_time = min*60 + sec

    if int(team) == 1:
        a_score += 1

        if a_score > b_score:
            if a_score - b_score == 1:
                last_time = curr_time
        if a_score == b_score:
            b_result += curr_time - last_time
            last_time = curr_time
    
    else:
        b_score += 1

        if a_score < b_score:
            if b_score - a_score == 1:
                last_time = curr_time
        if a_score == b_score:
            a_result += curr_time - last_time
            last_time = curr_time

if a_score > b_score:
    a_result += 48*60 - last_time
elif a_score < b_score:
    b_result += 48*60 - last_time

print(f"{str(a_result // 60).zfill(2)}:{str(a_result % 60).zfill(2)}")
print(f"{str(b_result // 60).zfill(2)}:{str(b_result % 60).zfill(2)}")


import sys

n, m = map(int,sys.stdin.readline().split())

note = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) < m:
        continue
    if word in note:
        note[word] += 1
    else:
        note[word] = 0
    
sorted_note = sorted(note.items(), key=lambda x: (x[1], len(x[0]), x[0]), reverse=True)

result = []
val = sorted_note[0][1]
length = len(sorted_note[0][0])
temp = []


for item in sorted_note:
    if val == item[1]:
        if length == len(item[0]):
            temp.append(item[0])
        else:
            result.extend(sorted(temp))
            val = item[1]
            length = len(item[0])
            temp = [item[0]]
    else:
        result.extend(sorted(temp))
        val = item[1]
        length = len(item[0])
        temp = [item[0]]

result.extend(sorted(temp))


for i in result:
    print(i)




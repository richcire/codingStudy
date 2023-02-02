import sys

vowels = ["a", "e", "i", "o", "u"]

while True:
    word = sys.stdin.readline().rstrip()
    if word == "end":
        break
    isVowel = False
    isTripleVowel = False
    tripleCnt = 0
    isDouble = False
    lastChar = ""

    for i in word:
        if i in vowels:
            isVowel = True
            if isTripleVowel:
                tripleCnt += 1
                if tripleCnt == 3:
                    break
            else:
                isTripleVowel = True
                tripleCnt = 1
            if lastChar == i:
                if i == "e" or i == "o":
                    continue
                isDouble = True
                break
        else:
            if isTripleVowel:
                isTripleVowel = False
                tripleCnt = 1
            else:
                tripleCnt += 1
                if tripleCnt == 3:
                    break
            
            if lastChar == i:
                isDouble = True
                break
        
        lastChar = i
    
    if not isVowel or tripleCnt == 3 or isDouble == True:
        print(f"<{word}> is not acceptable.")
    else:
        print(f"<{word}> is acceptable.")

import sys
sys.stdin = open('input_8958.txt')

T = int(input())

for tc in range(1, T + 1):
    OX = list(input())
    cnt = 0
    words = []

    for i in range(len(OX)):
        if OX[i] == "O":
            cnt += 1
            words.append(cnt)
        
        if OX[i] == "X":
            cnt = 0

    ans = sum(words)
    print(ans)

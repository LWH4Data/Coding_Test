import sys, time
sys.stdin = open("input.txt")
start = time.time()

#======================================

T = int(sys.stdin.readline())

for tc in range(1, T + 1):
    # 입력값을 받는다.
    S, P = map(int, sys.stdin.readline().split())
    chars = sys.stdin.readline()
    # A, C, G, T
    numbers = list(map(int, sys.stdin.readline().split()))
    ans = 0

    # 슬라이딩 윈도우 알고리즘
    # 윈도우 지정
    left = 0
    right = left + P

    # 처음 알파벳을 저장.
    temp = chars[left:right]
    window = [0, 0, 0, 0]
    for i in temp:
        if i == 'A':
            window[0] += 1
        elif i == 'C':
            window[1] += 1
        elif i == 'G':
            window[2] += 1
        elif i == 'T':
            window[3] += 1

    while right != S + 1:
        # 윈도우 만족하면 우선 += 1
        if window[0] >= numbers[0] and \
            window[1] >= numbers[1] and \
            window[2] >= numbers[2] and\
            window[3] >= numbers[3]:

            ans += 1
            left += 1
            right += 1
            if chars[left - 1] == 'A':
                window[0] -= 1
            elif chars[left - 1] == 'C':
                window[1] -= 1
            elif chars[left - 1] == 'G':
                window[2] -= 1
            elif chars[left - 1] == 'T':
                window[3] -= 1

            if chars[right - 1] == 'A':
                window[0] += 1
            elif chars[right - 1] == 'C':
                window[1] += 1
            elif chars[right - 1] == 'G':
                window[2] += 1
            elif chars[right - 1] == 'T':
                window[3] += 1
        
        # 아니라면 알고리즘 시작.
        else:
            left += 1
            right += 1
            if chars[left - 1] == 'A':
                window[0] -= 1
            elif chars[left - 1] == 'C':
                window[1] -= 1
            elif chars[left - 1] == 'G':
                window[2] -= 1
            elif chars[left - 1] == 'T':
                window[3] -= 1

            if chars[right - 1] == 'A':
                window[0] += 1
            elif chars[right - 1] == 'C':
                window[1] += 1
            elif chars[right - 1] == 'G':
                window[2] += 1
            elif chars[right - 1] == 'T':
                window[3] += 1

    print(ans)
#======================================

end = time.time()
print("time:", end - start)
import sys, time
sys.stdin = open('input_2810.txt')
start_time = time.time()

#=====================================================
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    words = list(input().strip())
    word_cnt = 0
    ans = 0

    # 찾아야 하는 패턴은 LL
    word = "L"

    # 한 칸씩 슬라이딩 윈도우로 비교 
    # 전체 L의 수를 세로 2로 나누면 된다.
    for i in range(N):
        if words[i] == word:
            word_cnt += 1

    # 나누기.
    word_cnt /= 2

    # 첫 번째 커플은 모두 놓을 수 있으니 그대로,
    # 나머지는 커플 수 - 1
    if word_cnt != 0:
        word_cnt = int(word_cnt) - 1
    else:
        word_cnt = int(word_cnt)

    ans = N - word_cnt
    print(ans)
#=====================================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 1 >

'''

'''
< 시간 복잡도 >
- 결국 최대 시간은 O(N)

- 현재 N은 최대 50 이므로 O(50)이며 완탐가능.
'''

'''
< 문제 정의 >
- 규칙을 찾아야 할 듯?

- *S*LL*LL*LL*S*LL*

- 커플 수 -1 만큼 컵을 놓을 수 없음.
'''
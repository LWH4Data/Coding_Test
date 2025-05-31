import sys, time
sys.stdin = open('sample_in.txt')
start_time = time.time()

#===================================================================
def is_adjacent(i, j, N):
    return (i - j) % N == 1 or (j - i) % N == 1

def in_between(x, y, z):  # z가 x와 y 사이에 있는가?
    return (x < z < y)

def is_cross(a, b, c, d, N):
    # 두 선분 (a,b) 와 (c,d)가 원형상에서 교차하는지 판단
    # a < b, c < d로 정렬
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    
    # 원형 순환 고려
    return (in_between(a, b, c) != in_between(a, b, d)) and (in_between(c, d, a) != in_between(c, d, b))

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    max_score = 0
    # 가능한 모든 쌍의 직통 노선 (i, j)
    for i in range(N):
        for j in range(i + 1, N):
            if is_adjacent(i, j, N): continue
            used = [False] * N
            used[i] = used[j] = True

            for k in range(N):
                for l in range(k + 1, N):
                    if is_adjacent(k, l, N): continue
                    if used[k] or used[l]: continue
                    if is_cross(i, j, k, l, N): continue
                    if is_adjacent(i, k, N) or is_adjacent(i, l, N): continue
                    if is_adjacent(j, k, N) or is_adjacent(j, l, N): continue

                    score = (nums[i] + nums[j]) ** 2 + (nums[k] + nums[l]) ** 2
                    max_score = max(max_score, score)
    
    print(f'#{tc} {max_score}')
#================================================================

end_time = time.time()
print('time :', end_time - start_time)
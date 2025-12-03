import sys, time
sys.stdin = open("input.txt")
start = time.time()

#===================================================
# 입력 받기
N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

# 상태를 저장할 변수 초기화
flag = 0
flag0 = True
num = 1
S = []
ans = []

while flag < N:
    # 숫자 추가.
    S.append(num)
    ans.append('+')

    # 만약 S[-1]이 numbers[flag] 보다 크다면 중지.
    if S[-1] > numbers[flag]:
        print("NO")
        flag0 = False
        break

    # 추가된 수가 일치한다면 일치하지 않을 때까지 pop
    while S[-1] == numbers[flag]:
        ans.append('-')
        S.pop()
        flag += 1

        if len(S) == 0:
            break

    # 일치하지 않는다면 다음 숫자 추가.
    num += 1


if flag0:
    for i in range(len(ans)):
        print(ans[i])
#===================================================

end = time.time()
print("time:", end - start)
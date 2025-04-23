import sys
sys.stdin = open('input_2231.txt')

N = int(input())

# 가장 작은 생성자를 찾기 위해 1부터 N까지 탐색
for num in range(1, N):
    base = num
    # map과 sum을 통해 바로 각 자리 수의 합을 구할 수 있다.
    # map 객체도 결국 iterator이기에 sum 적용이 된다는 듯.
    digit_sum = sum(map(int, str(num)))  # 각 자리수의 합

    if base + digit_sum == N:
        print(num)
        break
else:
    print(0)  # 생성자가 없는 경우 0 출력

# 숫자를 문자열로

# 생성자는 N보다는 작아야 함.

# 생성자 + 각 자리수 = N
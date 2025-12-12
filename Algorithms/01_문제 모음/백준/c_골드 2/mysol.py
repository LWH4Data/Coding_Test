import sys, time
sys.stdin = open("input.txt")
start = time.time()

#================================================
# 입력값 받기
N = int(sys.stdin.readline())
numbers = []
ans = 1

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

# 버블 정렬 구현
for i in range(N):
    for j in range(1, N - i - 1):
        if numbers[j] > numbers[j + 1]:
            ans += 1
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print(ans)
#================================================

end = time.time()
print("time:", start - end)
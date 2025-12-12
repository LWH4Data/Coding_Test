import sys, time
sys.stdin = open("input.txt")
start = time.time()

#============================================
# 입력값 받기
number = sys.stdin.readline().strip()
numbers = []
for i in range(len(number)):
    numbers.append(int(number[i]))
ans = ''

# 선택 정렬 구현
for i in range(len(numbers)):

    # 배열의 끝 원소라면 중단
    if i == len(numbers) -1:
        break

    # 남은 부분에서 최댓값과 인덱스 저장
    temp_val = max(numbers[i:])
    temp_index = numbers[i:].index(temp_val) + i
    # print(numbers)
    # print('i', i, "temp_val", temp_val, "temp_index", temp_index)
    numbers[temp_index] = numbers[i]
    numbers[i] = temp_val

# 출력부 생성
for i in range(len(numbers)):
    ans += str(numbers[i])

# 정답 출력
print(ans)
#============================================

end = time.time()
print("time:", start - end)
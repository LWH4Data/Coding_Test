import sys, time
sys.stdin = open("input.txt")
start = time.time()

#==================================================
# X % 제곱수 != 0 -> 제곱 ㄴㄴ 수
# 브루트포스는 시간 복잡도상 불가.
# 메모리는 512로 10**7이상 까지 가능.

# 에라토스테네스의 체를 구현할 때 배수로 구현하는데 이를 곱으로?
# 10**10 까지가 메모리 한계.

# 입력값 받기
min, max = map(int, sys.stdin.readline().split())
print(min, max)
#==================================================

end = time.time()
print("time: ", end - start)
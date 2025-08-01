import sys
sys.stdin = open("input_2739.txt")

N = int(input())

for i in range(1, 10):
    print(f"{N} * {i} =", N * i)
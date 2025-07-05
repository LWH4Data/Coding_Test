import sys
sys.stdin = open('input_10818.txt')

N = int(input())
num = list(map(int, input().split()))

min_val = min(num)
max_val = max(num)

print(min_val, max_val)
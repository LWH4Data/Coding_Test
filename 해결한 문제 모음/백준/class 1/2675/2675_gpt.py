import sys
sys.stdin = open('input_2675.txt')

T=int(input())

for _ in range(T):
    n,s=input().split()
    for i in s:
        print(i*int(n),end="")
    print()
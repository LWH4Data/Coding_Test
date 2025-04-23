import sys
sys.stdin = open('input_10951.txt')

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break
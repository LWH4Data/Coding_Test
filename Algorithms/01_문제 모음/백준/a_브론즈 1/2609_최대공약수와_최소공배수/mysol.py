import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=====================================================================
"""
유클리드 호제법을 활용하여 해결한다.
"""
A, B = map(int, sys.stdin.readline().split())

min_val = sys.maxsize
gong_list = []
max_ans = 0

while min_val != 0:
    if A > B:
        min_val = A % B
        if min_val == 0:
            max_ans = B
        else:
            gong_list.append(min_val)
    else:
        min_val = B % A
        if min_val == 0:
            max_ans = A
        else:
            gong_list.append(min_val)

print(max_ans)
print(A * B // max_ans)
#=====================================================================

e_t = time.time()
print("time: ", e_t - s_t)
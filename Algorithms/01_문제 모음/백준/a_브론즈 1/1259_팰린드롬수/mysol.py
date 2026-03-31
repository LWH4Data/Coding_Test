import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==========================================================
"""
투포인터로 펠린드롬 검사
"""

is_next = True

while is_next:

    target = sys.stdin.readline().strip()
    if target == '0':
        break

    start = 0
    end = len(target) - 1
    is_true = True

    while start < end:

        if target[start] != target[end]:
            is_true = False
            break

        start += 1
        end -= 1

    if is_true:
        print("yes")
    else:
        print("no")
#==========================================================

e_t = time.time()
print("time: ", e_t - s_t)
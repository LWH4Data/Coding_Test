import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#================================================================================
A, B, V = map(int, sys.stdin.readline().split())

now = 0

if V % A == 0:
    now = int(V / A)
else:
    now = int(V // A + 1)

temp = now * B

if temp % A == 0:
    now_one = int(temp / A)
else:
    now_one = int(temp // A + 1)

print(now_one + now)
#================================================================================

e_t = time.time()
print("time: ", e_t - s_t)
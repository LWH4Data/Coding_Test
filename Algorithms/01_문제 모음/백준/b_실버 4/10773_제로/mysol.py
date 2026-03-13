import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=====================================================================
K = int(sys.stdin.readline())
stack = []
for i in range(K):
    val = int(sys.stdin.readline())

    if val != 0:
        stack.append(val)
    else:
        stack.pop(-1)

print(sum(stack))
#=====================================================================

e_t = time.time()
print("time: ", e_t - s_t)
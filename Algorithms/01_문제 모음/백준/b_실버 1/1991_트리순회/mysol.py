import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==========================================================
# 입력값 받기
N = int(sys.stdin.readline())

# Tree 생성.
tree = [0] * (N * 2 + 2)
for i in range(1, N + 1):
    p, cl, cr = sys.stdin.readline().split()
    print(p, cl, cr)

    if i >= 2:
        tree[tree.index(p) * 2] = cl
        tree[tree.index(p) * 2 + 1] = cr 
    else:
        tree[i] = p
        tree[2 * i] = cl
        tree[2 * i + 1] = cr
    print(tree)

print(tree)
#==========================================================

e_t = time.time()
print("time: ", e_t - s_t)
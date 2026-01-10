import sys, time
sys.stdin = open("input.txt")
start = time.time()

#==============================================
A, B = map(int, sys.stdin.readline().split())

def sol(A, B):
    while B % A != 0:
        temp = A
        A = B % A
        B = temp
    
    return A

# # 자료구조 시간 최적화.
# A_num = ''
# B_num = ''
# for i in range(A):
#     A_num += '1'
# for i in range(B):
#     B_num += '1'

# A_num = int(A_num)
# B_num = int(B_num)

if A <= B:
    ans = sol(A, B)
else:
    ans = sol(B, A)

ans1 = 0

for i in range(ans):
    print(1)
    ans1 += 10**i
    
print(ans1)
#==============================================

end = time.time()
print("time: ", end - start)
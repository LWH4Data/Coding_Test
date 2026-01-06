import sys, time
sys.stdin = open("input.txt")
start = time.time()

#=========================================
# 입력값 받기
M, N = map(int, sys.stdin.readline().split())

# 필요한 변수 초기화
ans = []
for i in range(2, N + 1):
    ans.append(i)
 
# 1은 제외
if 1 in ans:
    ans.remove(1)

# 에라토스테네스의 체
for i in ans:
    # print(ans)
    # print('i:', i)
    for j in range(2, ans[-1] // 2 + 1):
        # print('j:', j)
        
        if i * j > ans[-1]:
            break

        if i * j in ans:
            ans.remove(i * j)

for i in range(len(ans)):
    if ans[i] < 3:
        ans.remove(ans[i])
    else:
        break

for i in ans:
    print(i)
#=========================================

end = time.time()
print("time: ", end - start)
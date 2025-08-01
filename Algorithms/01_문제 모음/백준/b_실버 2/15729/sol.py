import sys, time
sys.stdin = open('input.txt')
start_time = time.time()

#===============================================
N = int(input())
nums = list(map(int, input().split()))
start = [False] * N

cnt = 0
for i in range(N):
    if nums[i] != start[i]:
        cnt += 1
        start[i] = not start[i]

        if i + 1 < N:
            start[i + 1] = not start[i + 1]
        
        if i + 2 < N:
            start[i + 2] = not start[i + 2]

print(cnt)
#===============================================

end_time = time.time()
print('time :', end_time - start_time)

'''
< 로직 >

'''

'''
< 시간 복잡도 >

'''

'''
< 문제 정리 >
0 0 0 0 0 0 0

0 0 1 1 1 0 0 

0 0 1 0 0 1 0
'''
import sys
sys.stdin = open('input_30802.txt')

N = int(input()) # 전체 인원수
Tn = list(map(int, input().split())) # 티셔츠 묶음 수.
T, P = map(int, input().split()) # 티셔츠 묶음, 팬 묶음 수.
T_ans = 0 # 티셔트 T 최소 몇 묶음 답.
P_set = 0 # 팬 묶음 수
P_ans = 0 # 팬 낱개 수

for i in range(6):
    if Tn[i] % T == 0:
        T_ans += (Tn[i] // T) 

    if Tn[i] % T != 0:
        T_ans += (Tn[i] // T + 1)

P_set = N // P
P_ans = N % P

print(T_ans)
print(P_set, P_ans)

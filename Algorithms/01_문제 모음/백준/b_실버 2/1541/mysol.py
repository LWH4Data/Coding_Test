import sys, time
sys.stdin = open("input.txt")
start = time.time()

#===============================================
# 문자열로 받기
data = sys.stdin.readline()

# 필요한 변수 선언
pos_sum = 0
neg_sum = 0
flag = True
num = ''

# 전체 데이터 순회
for i in data:

    if i == '+' and flag:
        pos_sum += int(num)
        # print("pos_num: ", pos_sum)
        num = ''
        continue
    
    if i == '+' and not flag:
        neg_sum += int(num)
        # print("neg_sum: ", neg_sum)
        num = ''
        continue

    if i == "-":
        if flag:
            pos_sum += int(num)
            num = ''
        if not flag:
            neg_sum += int(num)
            num = ''
        flag = False
        continue

    if i not in ['-', '+']:
        num = num + i
        # print("num: ", num)

if flag:
    pos_sum += int(num)
else:
    neg_sum += int(num)

print(pos_sum - neg_sum)
#===============================================

end = time.time()
print("time: ", start - end)
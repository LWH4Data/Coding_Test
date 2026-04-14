import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#=============================================================
"""
- stack을 활용한 풀이.
- (와 [ 두 개의 리스트를 만들고 관리한다.
- ( 혹은 [이 들어오면 쌓고, ) 혹은 ]이 들어오면 제거한다.
  - 이때 제거할 게 없다면 균형 문자가 아니다.
"""
while(True):

    target = sys.stdin.readline().strip()
    print(target)
    if target == ".":
        break

    print(1)
#=============================================================

e_t = time.time()
print("time: ", e_t - s_t)
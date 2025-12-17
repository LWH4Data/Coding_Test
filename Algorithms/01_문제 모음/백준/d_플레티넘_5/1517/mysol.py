import sys, time
sys.stdin = open("input.txt")
start = time.time()

#==================================================
# 병합 정렬 함수
# 시작값 start와 끝값 end를 입력으로 받는다.
def merge_sort(s, e):
    # 시작값과 끝값이 같다면 정렬을 종료한다.
    if e - s < 1:
        return
    
    # 같지 않은 경우 중앙값을 찾는다.
    m = int(s + (e - s) / 2)

    # 
#==================================================

end = time.time()
print("time:", end - start)

print(2**27)
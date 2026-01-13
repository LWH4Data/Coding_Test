import sys, time
sys.stdin = open("input.txt")
start = time.time()

#===========================================================
N, M = map(int, sys.stdin.readline().split())
jinsil = list(map(int, sys.stdin.readline().split()))
print(jinsil)

# 진실을 아는 사람이 없다면 예외 처리.
if len(jinsil) == 1:
    # 정답은 파티 수임.
    print(M)

# jinsil의 상태를 관리할 check 리스트 초기화
check = [False] * (N + 1)
for i in range(1, len(jinsil)):
    check[jinsil[i]] = True
print(check)

# 파티 정보를 각 원소로 구현
parties = []
for _ in range(M):
    parties.append(list(map(int, sys.stdin.readline().split())))
# print(parties)

# 파티의 각 원소를 순회하면서 진실을 아는 사람이 포함 된다면 check 업데이트
for party in parties:
    for person in party:
        if person in jinsil:
            for i in party:
                check[i] = True
                jinsil.append(i)

print(jinsil)
check()

#===========================================================

end = time.time()
print("time: ", end - start)
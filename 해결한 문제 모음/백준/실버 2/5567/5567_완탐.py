import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input()) # 동기의 수
m = int(input()) # 리스트의 길이

# 친구 관계
"""
상근이의 학번은 1
상근이의 친구
상근이의 친구의 친구
"""
friends = set()
ffriends = set()

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

# 친구 정리
for edge in graph:
    a, b = edge
    if a == 1:
        friends.add(b)
    elif b == 1:
        friends.add(a)

# 친구의 친구 정리
for edge in graph:
    a, b = edge

    if a == 1 or b == 1:
        continue

    if a in friends:
        ffriends.add(b)
    elif b in friends:
        ffriends.add(a)

print(len(friends | ffriends))
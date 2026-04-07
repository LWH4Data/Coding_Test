import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#======================================================================
"""
나이, 가입한 순서
"""
N = int(sys.stdin.readline())
people = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    people.append((age, i + 1, name))

people.sort(key = lambda x: (x[0], x[1]))

for i in range(N):
    print(people[i][0], people[i][2])
#======================================================================

e_t = time.time()
print("time: ", e_t - s_t)
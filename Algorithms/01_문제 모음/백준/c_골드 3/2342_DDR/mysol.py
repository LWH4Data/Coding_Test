import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#==================================================================
numbers = list(map(int, sys.stdin.readline().split()))
result = 0
i_copy = 0

for i in range(len(numbers)):

    if numbers[i] == 0:
        break

    if i == 0 or i == 1:
        result += 2
    else:
        if i_copy == numbers[i]:
            result += 1
        else:
            result += 3

    i_copy = numbers[i]

print(result)
#==================================================================

e_t = time.time()
print("time: ", e_t - s_t)
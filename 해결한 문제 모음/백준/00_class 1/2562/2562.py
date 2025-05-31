import sys 
sys.stdin = open('input_2562.txt')

nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break

max_val = max(nums)
max_idx = nums.index(max(nums))
print(max_val)
print(max_idx + 1)
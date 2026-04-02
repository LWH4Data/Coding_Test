import sys, time
sys.stdin = open("input.txt")
s_t = time.time()

#================================================================================
import math

A, B, V = map(int, sys.stdin.readline().split())
print(math.ceil((V - A) / (A - B)) + 1)
#================================================================================

e_t = time.time()
print("time: ", e_t - s_t)
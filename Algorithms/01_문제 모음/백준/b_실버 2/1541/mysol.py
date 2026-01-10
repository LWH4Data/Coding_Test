import sys, time
sys.stdin = open("input.txt")
start = time.time()

#================================================
data = sys.stdin.readline()
print(data)
#================================================

end = time.time()
print("time: ", end - start)
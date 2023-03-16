import sys

n = int(sys.stdin.readline())
num = int(sys.stdin.readline())
numList = list(map(int, str(num)))

result = sum(numList)

print(result)

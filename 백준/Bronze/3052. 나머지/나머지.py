import sys

numlist = []
count = 0
index = 0

for i in range(10):
    n = int(sys.stdin.readline())
    numlist.append(n % 42)

s = set(numlist)
print(len(s))
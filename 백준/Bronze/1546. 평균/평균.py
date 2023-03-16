import sys

n = int(sys.stdin.readline())
score = list((map(int, sys.stdin.readline().split())))
M = max(score)
result = 0

for i in score:
    total = (i/M) * 100
    result += total

print(result/n)
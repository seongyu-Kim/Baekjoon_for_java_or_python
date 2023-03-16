import sys

t = int(sys.stdin.readline())

for _ in range(t):
    cnt, word = sys.stdin.readline().split()

    for i in word:
       print(i * int(cnt), end = "")

    print()

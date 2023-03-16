import sys

s = str(sys.stdin.readline())
alpa = []

for i in range(97, 123):
    alpa.append(chr(i))

for j in range(26):
    if alpa[j] in s:
        for k in range(len(s)):
            if s[k] == alpa[j]:
                print(k, end = ' ')
                break
    else:
        print(-1, end = ' ')


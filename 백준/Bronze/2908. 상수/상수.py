import sys

a, b = list(sys.stdin.readline().split())

reverseA = a[::-1]
reverseB = b[::-1]

if reverseA > reverseB:
    print(reverseA)
else:
    print(reverseB)
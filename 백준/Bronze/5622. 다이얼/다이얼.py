import sys

word = sys.stdin.readline() #WA
numList = ["ABC", "DEF", " GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
unit = []
result = []

for unit in numList:
    for i in unit:
        for x in word:
            if i == x:
                result.append(numList.index(unit)+3)

print(sum(result))

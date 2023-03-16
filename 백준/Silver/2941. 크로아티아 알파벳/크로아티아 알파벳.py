import sys

word = sys.stdin.readline().rstrip()   #lj e s= nj a k
alpaList = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

for i in alpaList:
    if i in word:
        word = word.replace(i, "@")

for j in word:
    if j == "@":
        count += 1
    else:
        count += 1

print(count)

import sys

c = int(sys.stdin.readline())

for i in range(c):
    sum = 0
    avg = 0
    count = 0
    pct = 0
    nScore = list(map(int, sys.stdin.readline().split()))
    for j in range(len(nScore)):
        sum += nScore[j]
    sum -= nScore[0]
    avg = sum / nScore[0]

    for k in range(1, len(nScore)):
        if nScore[k] > avg:
            count += 1
        else:
            pass
        pct = (count/nScore[0]) * 100



    print("%0.3f%s" % (pct, "%"))
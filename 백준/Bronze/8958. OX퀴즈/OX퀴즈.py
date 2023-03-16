import sys
N = int(sys.stdin.readline())
answer = 0

for i in range(N):
    list1 = list(sys.stdin.readline().split('X'))
    for j in range(len(list1)):
        count = list1[j].count('O')
        while count != 0:
            answer += count
            count -= 1
    print(answer)
    answer = 0
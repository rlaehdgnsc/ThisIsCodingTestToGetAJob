import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    temp = list(input().split())
    temp[1] = int(temp[1])
    arr.append(temp)

ans = sorted(arr,key = lambda x : x[1])
for i in ans:
    print(i[0], end=' ')
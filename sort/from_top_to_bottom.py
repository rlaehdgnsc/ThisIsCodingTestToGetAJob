import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for i in range(N)], reverse=True)
for i in arr:
    print(i,end=' ')
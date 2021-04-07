import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
coins = [int(input()) for i in range(n)]

d = [m]*(m+1)
d[0] = 0

for i in range(n):
    for j in range(coins[i],m+1):
        if d[j-coins[i]]!=m:
            d[j] = min(d[j],d[j-coins[i]]+1)

print(d[m] if d[m]!=m else -1)
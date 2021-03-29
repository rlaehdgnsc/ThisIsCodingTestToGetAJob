import sys 
input = sys.stdin.readline

N = int(input())
wareHouse = list(map(int,input().split()))
s = [0]*N

s[0] = wareHouse[0]
s[1] = max(wareHouse[0],wareHouse[1])

for i in range(2,N):
    s[i] = max(s[i-1],s[i-2]+wareHouse[i])

print(s[-1])
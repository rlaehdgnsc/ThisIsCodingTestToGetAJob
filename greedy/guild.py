import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))
numbers.sort()

ans = 0
count = 0
for i in numbers:
    count+=1
    if count>=i:
        ans+=1
        count = 0

print(ans)
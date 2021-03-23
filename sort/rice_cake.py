import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))
cake = sorted(list(map(int,input().split())))

l,r = 0, cake[-1]

while l<=r:
    i = (l+r)//2
    temp = 0
    for j in cake:
        if j-i>0:
            temp+=j-i
    if temp == M:
        print(i)
        break

    if temp>M:
        l = i+1
    else:
        r = i-1
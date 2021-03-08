import sys
import time

input = sys.stdin.readline

N,M = map(int,input().split())
x, y, d = map(int,input().split())
Map = [list(map(int,input().split())) for i in range(N)]
direction = { 0 : [-1,0],1:[0,1],2:[1,0],3:[0,-1]}
ans = 0

def changeDirection():
    global d
    d = 3 if d-1 == -1 else d-1

def move(dx, dy):
    global ans
    if Map[dy][dx] == 0:
        Map[dy][dx] = 1
        ans += 1
    
    for i in range(4):
        changeDirection()
        n_x = direction[d][1]+dx
        n_y = direction[d][0]+dy

        if Map[n_y][n_x] == 0:
            move(n_x,n_y)

move(x,y)
print(ans)
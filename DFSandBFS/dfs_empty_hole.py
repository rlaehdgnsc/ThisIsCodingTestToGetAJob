import sys
input = sys.stdin.readline

N,M = map(int,input().split())
d = {0 : [1,0], 1:[0,1],2:[-1,0],3:[0,-1]}
board = [list(input()[0:M]) for i in range(N)]
ans = 0

def dfs(x,y):
    board[y][x] = '1'
    for i in d.values():
        dx = x+i[1]
        dy = y+i[0]
        if dx>=0 and dx<M and dy>=0 and dy<N:
            if board[dy][dx] == '0':
                dfs(dx,dy)

c = True
while c:
    c = False
    for idx, i in enumerate(board):
        if '0' in i:
            ans+=1
            dy, dx = idx, i.index('0')
            dfs(dx,dy)
            c = True
    
print(ans)

"""
15 14
000001111000000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

8
"""
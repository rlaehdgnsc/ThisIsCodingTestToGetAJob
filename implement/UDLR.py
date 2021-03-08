import sys
input = sys.stdin.readline
N = int(input())
plan = list(input().split())

print(N, plan)

pos = [1,1]
direction = { "L" :[0,-1], "R" : [0,1], "D"  :[ 1,0], "U" : [-1,0]}

for i in plan:
    n = direction[i]
    y_n = pos[0] + n[0]
    x_n = pos[1] + n[1]
    
    print(i, n, x_n, y_n)
    
    if x_n>=1 and x_n<=N and y_n>=1 and y_n<=N:
        pos[0] = y_n
        pos[1] = x_n
        
print(pos[0], pos[1])

'''
N X N 크기의 정사각형 공간에서 여행가는 (1,1)에서 출발하여 계획에 따라 움직인다.
계획이 공간을 벗어나면 그 계획은 무시한다.
최종적으로 도달하는 곳의 좌표는?
'''
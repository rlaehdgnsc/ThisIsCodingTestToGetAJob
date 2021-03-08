import sys
input = sys.stdin.readline

## 8*8
N = input()
pos = [int(N[1])-1,ord(N[0])-97]

print(pos)

direction = { "ul" : [-2,-1], "ur" : [-2,1], "rd" : [1,2],"ru":[-1,2],
        "dl":[2,-1],"dr":[2,1],"ld":[1,-2],"lu":[-1,-2]}

ans = 0
for v in direction.values():
    x_n = pos[1] + v[1]
    y_n = pos[0] + v[0]
    
    if x_n>=0 and x_n<=7 and y_n>=0 and y_n<=7:
       ans += 1
        
print(ans)

'''
기사가 주어진 위치에서 움직일 때 갈 수 있는 모든 경로의 수를 구하라
단, 기사는 반드시 수평으로 두 칸 이동한 후에 수직으로 한 칸 이동하거나 
수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동한다.
'''
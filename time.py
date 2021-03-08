import sys
input = sys.stdin.readline
N = int(input())

ans = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                    ans+=1
print(ans) 

'''
00시 00분 00초부터 N시 59분 59초까지 숫자 N이 포함되는 시각의 경우를 모두 구하라
'''
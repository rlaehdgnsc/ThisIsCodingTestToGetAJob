import sys
input = sys.stdin.readline

N, M = list(map(int,input().split()))
ans = 0
for i in range(N):
    ans = max(ans, min(list(map(int,input().split()))))
    
print(ans)

'''
N X M 형태로 놓여진 숫자 카드들 중에서 각 행 중에 가장 작은 수를 고를 때
가장 큰 수를 구하시오...
'''
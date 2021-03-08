import sys
input = sys.stdin.readline

N,M,K = list(map(int,input().split()))
n_list = list(map(int,input().split()))

n_list.sort()

cnt = int(M/(K+1))
cnt2 = M%(K+1)

ans = cnt*(n_list[-1]*K+n_list[-2])+cnt2*n_list[-1]
print(ans)

'''
어떠한 수 N이 1이 될 때까지 1을 빼거나 K로 나누는 연산을 한다.
이때 연산의 최소 횟수를 구하라
'''
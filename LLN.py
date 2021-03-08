import sys
input = sys.stdin.readline()

user_input = list(map(int,input.split()))
N = user_input[0]
M = user_input[1]
K = user_input[2]

n_list = list(map(int,input.split()))
n_list.sort()

maximum = 0
for i in range(1,M+1)
    if i%K !=0:
        maximum += n_list[N-1]
    else:
        maximum += n_list[N-2]
    
print(maximum)

'''
큰 수의 법칙(수정)

숫자 배열이 주어질 때 수들을 M번 더하여 가장 큰 수를 만드는 법칙
숫자의 수 N, 한 번에 같은 수를 연속해서 더할 수 있는 횟수 K, 총 더하는 횟수 M
일 때, 가장 큰 수를 구하라
'''
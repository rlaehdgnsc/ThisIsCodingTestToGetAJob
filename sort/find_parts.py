import sys
input = sys.stdin.readline

N = int(input())
N_arr = set(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

ans = []
for i in M_arr:
    if i in N_arr:
        ans.append("yes")
    else:
        ans.append("no")
for i in ans:
    print(i, end=" ")
print()


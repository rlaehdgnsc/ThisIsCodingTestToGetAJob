import sys
input = sys.stdin.readline

N, target = input().split()
arr = list(input().split())
flag = False

for idx,val in enumerate(arr):
    if val == target:
        print(target,"is located in",idx)
        flag = True
        break

if not flag:
    print('No data Found')
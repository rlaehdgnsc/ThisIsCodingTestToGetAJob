import sys
input = sys.stdin.readline

N,K = list(map(int,input().split()))
arr1 = sorted(list(map(int,input().split())))
arr2 = sorted(list(map(int,input().split())),reverse = True)

for i in range(K):
    if arr1[i]<arr2[i]:
        arr1[i],arr2[i] = arr2[i],arr1[i]
print(sum(arr1))        
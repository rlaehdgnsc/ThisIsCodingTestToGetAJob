import sys
input = sys.stdin.readline

N, target = list(map(int,input().split()))
arr = list(map(int,input().split()))

def binary_search(l,r):
    m = (l+r)//2
    if l>r:
        print('No data found')
        return None

    if arr[m] == target:
        print(target,"is located in",m)
        return True
    
    if target>arr[m]:
        binary_search(m+1,r)
    else:
        binary_search(l,m-1)

binary_search(0,N-1)

    

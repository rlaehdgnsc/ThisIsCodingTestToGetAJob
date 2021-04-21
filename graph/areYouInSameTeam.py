import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]

def findParent(parent,a):
    if parent[a] != a:
        parent[a] = findParent(parent,parent[a])
    return parent[a]

def unionParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)
    if a>b:
        parent[b] = a
    else:
        parent[a] = b

def checkParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)

    if a == b:
        return True
    else:
        return False

for i in range(m):
    c,a,b = map(int,input().split())
    if c == 0:
        unionParent(parent,a,b)
    else:
        ans = "YES" if checkParent(parent,a,b) else "NO"
        print(ans)
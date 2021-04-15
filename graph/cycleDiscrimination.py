import sys
input = sys.stdin.readline

def find_parent(parent,a):
    if parent[a] !=a:
        return find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

n,e = map(int,input().split())
parent = [i for i in range(n+1)]


for i in range(e):
    a,b = map(int, input().split())
    if find_parent(parent,a) == find_parent(parent,b):
        print("there is cycle")
    else:
        union_parent(parent,a,b)
        if i == e-1:
            print("no cycle")

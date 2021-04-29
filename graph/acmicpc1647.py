import sys
input = sys.stdin.readline

def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a
        
def initialize():
    v,e = map(int,input().split())
    parent = [i for i in range(v+1)]
    
    edges = []
    for _ in range(e):
        a,b,c = map(int,input().split())
        edges.append((c,a,b))
    edges.sort()
    return [v,e,parent,edges]

def kruskal(edges,parent):
    ans,last = 0,0
    for e in edges:
        cost,a,b = e
        if find_parent(parent,a)!=find_parent(parent,b):
            union_parent(parent,a,b)
            ans+=cost
            last = cost
            
    ans -= last 
    return ans

v,e,parent,edges = initialize()
print(kruskal(edges,parent))
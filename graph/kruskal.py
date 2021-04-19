import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

def get_data():
    global v,e,edges,parent
    
    v,e = map(int, input().split())
    parent = [i for i in range(v+1)]

    for _ in range(e):
        f,t,dis = map(int, input().split())
        edges.append((dis,f,t))
    
    edges.sort()

def kruskal_minimum_cost(edges,parent):
    result = 0
    for dis,f,t in edges:
        if find_parent(parent,f)!=find_parent(parent,t):
            union_parent(parent,f,t)
            result+=dis

    return result


v,e = 0,0
edges, parent = [],0

get_data()
ans = kruskal_minimum_cost(edges,parent)
print(ans)
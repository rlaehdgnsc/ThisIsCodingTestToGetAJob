g = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visit1 = [False]*len(g)
visit2 = [False]*len(g)

def dfs(t,v):
    v[t] = True
    print(t,end=' ')
    for i in g[t]:
        if v[i] == False:
            dfs(i,v)

def bfs(t,v):
    q = [t]
    v[t] = True
    while len(q)!=0:
        p = q.pop(0)
        print(p, end=' ')
        for i in g[p]:
            if v[i] == False:
                v[i] = True
                q.append(i)

dfs(1,visit1)
print()
bfs(1,visit2)
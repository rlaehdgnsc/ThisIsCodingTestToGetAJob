import sys
input = sys.stdin.readline

node,edge = map(int,input().split())
INF = int(1e9)

def make_graph(n,e):
    g = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                g[i][j] = 0

    for i in range(e):
        f,t = map(int,input().split())
        g[f][t] = 1
        g[t][f] = 1

    return g

def floyd_warshall(g,n):
    for k in range(1,n+1): #by
        for i in range(1,n+1): #from
            for j in range(1,n+1): #to
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

graph = make_graph(node,edge)
floyd_warshall(graph,node)
x,k = map(int,input().split())
ans = graph[1][k]+graph[k][x]

if ans<INF:
    print(ans)
else:
    print(-1)
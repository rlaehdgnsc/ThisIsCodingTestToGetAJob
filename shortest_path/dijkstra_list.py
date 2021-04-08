import sys
input = sys.stdin.readline

n,e = map(int,input().split())
start = int(input())

INF = int(1e9)
# index 1~n
graph = [[] for _ in range(n+1)]
v = [False]*(n+1)
dis = [INF]*(n+1)

def get_shortest_dis():
    m = INF
    node = 0
    for i in range(1,n+1):
        if dis[i]<m and not v[i]:
            m = dis[i]
            node = i
    return node

def dijkstra(s):
    dis[s] = 0
    v[s] = True

    for j in graph[s]:
        dis[j[0]] = j[1]

    for i in range(n-1):
        cur = get_shortest_dis()
        v[cur] = True

        for j in graph[cur]:
            next_dis = dis[cur]+j[1]
            if next_dis<dis[j[0]]:
                dis[j[0]] = next_dis

#initialize edges
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

dijkstra(start)
for i in range(1,n+1):
    if dis[i] == INF:
        print("there is no path to get")
    else:
        print(dis[i])
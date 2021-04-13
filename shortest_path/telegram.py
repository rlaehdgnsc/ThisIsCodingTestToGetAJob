import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

def make_graph(n,m):
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y,d = map(int,input().split())
        g[x].append((y,d))

    return g

def dijstra(start, graph,dis):
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0
    while q:
        cur_dis, cur = heapq.heappop(q)
        if dis[cur] < cur_dis:
            continue
        for i in graph[cur]:
            cost = cur_dis+i[1]
            if cost<dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

n,m,c = map(int,input().split())
graph = make_graph(n,m)
distance = [INF]*(n+1)
dijstra(c,graph,distance)

cnt = 0
m_dis = 0
for i in distance:
    if i!=INF:
        cnt+=1
        m_dis = max(m_dis,i)
print(cnt-1,m_dis)
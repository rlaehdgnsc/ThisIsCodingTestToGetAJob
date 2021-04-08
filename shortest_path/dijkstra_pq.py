import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,e = map(int,input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
dis = [INF]*(n+1)

def dijkstraWithPQ():
    global start
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0

    while q:
        distance,now = heapq.heappop(q)
        if dis[now]<distance:
            continue

        for i in graph[now]:
            cost = distance+i[1]
            if cost<dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


for _ in range(e):
    f,t,d = map(int,input().split())
    graph[f].append((t,d))

dijkstraWithPQ()
for i in range(1,n+1):
    if dis[i] == INF:
        print("there is no path to get")
    else:
        print(dis[i])
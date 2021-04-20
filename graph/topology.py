import sys
from collections import deque
input = sys.stdin.readline

def initialize():
    global v,e,indegree,graph

    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    indegree = [0]*(v+1)

    for _ in range(e):
        f,t = map(int,input().split())
        graph[f].append(t)
        indegree[t]+=1

def topology_sort(indegree,graph,vertex):
    result = []
    q = deque()

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        cur = q.popleft()
        result.append(cur)

        for i in graph[cur]:
            indegree[i]-=1
            if indegree[i] == 0:
                q.append(i)
    return result

def printResult(result):
    for i in result:
        print(i,end=" ")
    print()

v,e = 0,0 # vertext, edge
indegree = []
graph = []

initialize()
result = topology_sort(indegree,graph,v)
printResult(result)
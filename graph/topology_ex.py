from collections import deque
import copy

# 인수 초기화
def initialize():
    v = int(input())
    
    indegree = [0]*(v+1)
    graph = [[] for _ in range(v+1)]
    cost = [0]*(v+1)
    
    for i in range(1,v+1):
        data = list(map(int,input().split()))
        cost[i] = data[0]
        for j in data[1:-1]:
            indegree[i]+=1
            graph[j].append(i)
    
    return [v,indegree,graph,cost]

# 위상정렬
def topology(v,indgree,graph,cost):
    ans = copy.deepcopy(cost)
    
    q = deque()
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            ans[i] = max(ans[i],ans[now]+cost[i])
            indegree[i]-=1
            if indegree[i] == 0:
                q.append(i)
    
    return ans

# 결과물 출력
def printResult(ans):
    for i in range(1,len(ans)):
        print(ans[i])
    
v,indegree,graph,cost = initialize()
ans = topology(v,indegree,graph,cost)
printResult(ans)

    
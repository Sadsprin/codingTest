# Bellman Ford Algorithm
    # 음수 간선이 포함된 상황에서의 최단 거리 문제 해결
    
    # 1. 모든 간선이 양수인 경우
    # 2. 음수 간선이 있는 경우
    #     2-1. 음수 간선 순환은 없는 경우
    #     2-2. 음수 간선 순환이 있는 경우
    
    # 벨만 포드 최단 경로 알고리즘은 음의 간선이 포함된 상황에서도 사용할 수 있습니다.
    #    * 또한 음수 간선의 순환을 감지할 수 있습니다
    #    * 벨만 포드의 기본 시간 복잡도는 O(VE)로 다익스트라 알고리즘에 비해 느립니다.

    # 동작 원리
    # 1. 출발 노드를 설정합니다,
    # 2. 최단 거리 테이블을 초기화합니다.
    # 3. 다음의 과정을 N - 1번 반복합니다.
    #     3-1. 전체 간선 E개를 하나씩 확인합니다.
    #     3-2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신합니다.
    # 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한번 더 수행합니다.
    #     이때 최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재하는 것 입니다.

import sys
input = sys.stdin.readline
INF = int(1e9)
n, m =  map(int, input().split())
edges = []
dist = [INF] * (n+1)

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost 
                if i == n - 1:
                    return True
    return False




for i in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))
negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])

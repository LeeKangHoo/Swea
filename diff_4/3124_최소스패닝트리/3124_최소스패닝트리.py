#
# 정점과 정점을 이동하는데에 드는 비용을 가중치라고 하고, 모든 정점을 돌았을 때 그 가격이 최소인 경우를 구하는 문제.
# 어쨋던 가능한 경우를 전부 돌고, 모든 경로를 방문 했을 때 (return해버림) min_val을 조정하면 될 것 같다. 
# min_val의 초기화 값은 가중치가 절댓값 1,000,000을 넘지 않고 정점의 최대 갯수는 100,000이니까 10의 10승으로 주면될 것 같다.
# 가중치까지 같이 저장해두는 법은 tuple을 이용해서 가중치까지 적어두면 되겠다 (양방향으로)
# dfs 백트래킹으로 구현해서 visited에 여태까지 온 가중치의 합을 누적합 시키고 모두 돌았을 때 min_val과 비교
# visited 관리하기 복잡해서 따로 인자값에 cnt로 넘기기

def find(parent,x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    root_a = find(parent,a)
    root_b = find(parent,b)

    if root_a != root_b:
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b


T = int(input())

for i in range(T):
    V,E = map(int,input().split())
    parent = [j for j in range(V+1)]
    edges = []
    min_val = 0
    cnt = 0
    for j in range(E):
        A,B,C = map(int,input().split())
        edges.append((A,B,C))
    
    edges.sort(key=lambda x: x[2])

    for a,b, cost in edges:
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
            min_val += cost
            cnt += 1

            if cnt == V-1:
                break

    print(f"#{i+1} {min_val}")
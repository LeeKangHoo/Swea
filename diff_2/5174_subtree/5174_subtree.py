#60
def solve(graph,cur):
    cnt = 1
    for next in graph[cur]:
        cnt += solve(graph,next)
    return cnt



T = int(input())

for i in range(T):
    E, N = map(int,input().split())
    graph = [[] for _ in range(E+2)]
    tmp = list(map(int,input().split()))
    for j in range(0,len(tmp),2):
        graph[tmp[j]].append(tmp[j+1])
    print(f"#{i+1} {solve(graph,N)}")

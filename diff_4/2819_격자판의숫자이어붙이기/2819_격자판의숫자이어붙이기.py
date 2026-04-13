#23
# python 제한시간 8초에 한 번 거쳤던 격자칸을 다시 거쳐도 된다는 제한이 있다. 그냥 냅다 dfs 백트래킹 박아봐야하나?
# set을 사용해야한다. 저번에 사용했던 합집합 연산을 사용해야하나?
# join으로 str로 만들어서 넣는게 오버헤드가 더심할까? 아니면 리스트를 그대로 넣는게 메모리 낭비가 심할까? 
# 근데 메모리 신경안쓰고 일단 리스트로 넣어봐야겠다. -> 리스트는 set의 요소로 넣을 수 없다. 근데 str은 불변객체라 중간중간 추가가 안되는데 join써도 되려나?
# 덮어씌우면 그게 더 오버헤드 심할텐데
# recusion오류가 난다. 재귀를 들어가는 양이 너무 많다는건데 그럼 bfs로 해봐야겠다.
# bfs로 해보니까 무한루프를 돈다. popleft하는 것 보다 무조건 4방향을 더 추가해버리기 때문에 무한대로 늘어난다.
# 디버깅 해보니까 내가 pop을 까먹고 안적어서 그랬다. 그러니까 바로 풀리네 뭐지?

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(x,y):
    global tmp
    tmp.append(mapp[x][y])
    if len(tmp) == 7:
        r.add(''.join(tmp))
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx,ny)
            tmp.pop()
    return

# def bfs(x,y):
#     q = deque()
#     q.append((x,y))
#     tmp = []
#     tmp.append(mapp[x][y])
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]
#     while q:
#         cx,cy = q.popleft()
#         if len(tmp) == 7:
#             r.add(''.join(tmp))
#             tmp = []
#             continue
#         for i in range(4):
#             nx = cx + dx[i]
#             ny = cy + dy[i]
#             if 0 <= nx < 4 and 0 <= ny < 4:
#                 q.append((nx,ny))
#     return

T = int(input())

for tc in range(T):
    mapp = [list(input().split()) for _ in range(4)]
    r = set()
    for i in range(4):
        for j in range(4):
            tmp = []
            dfs(i,j)


    print(f'#{tc+1} {len(r)}')
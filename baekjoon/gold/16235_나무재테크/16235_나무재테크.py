# 80
# r과 c는 1부터 시작. (인덱싱이 필요하다는 뜻)
# 봄 : 나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가. 나이가 어린 나무부터 양분을 먹음. 양분을 먹을 수 없으면 그 나무는 즉시 죽는다.
# 여름 : 죽은 나무가 양분으로 변한다. 각 죽은 나무마다 나이 // 2 가 양분으로 추가된다.
# 가을 : 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야한다. 인접한 8칸에 나이가 1인 나무가 생긴다.
# 겨울 : S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 
# K년이 지난 후 땅에 살아있는 나무의 개수를 구하라.
# 왜 42% 시간초과지? sort때문에 그런가? heapq를 써야하나
# 일단 반복문 안에 sort를 쓴게 문제같은데 뒤의 인덱스가 무조건 더 작으니까 반대로 for문을 굴려볼까? sort안쓰고?
# 오히려 12%에서 시간초과가 떠버리네?

def spring():
    dead_tree = []
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort()
                for a in range(len(tree[i][j])):
                    cur = tree[i][j][a]
                    if mapp[i][j] >= cur:
                        mapp[i][j] -= cur
                        tree[i][j][a] += 1
                    else:
                        dead_tree.append((i,j,cur))
                        dead[i][j] += 1

    for i in range(N):
        for j in range(N):
            if dead[i][j] != 0:
                for a in range(dead[i][j]):
                    tree[i][j].pop()
                    dead[i][j] -= 1
    return dead_tree

def summer(dead_tree):
    for cx,cy,age in dead_tree:
        mapp[cx][cy] += age//2
    return

def fall():
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    for i in range(N):
        for j in range(N):
            for a in range(len(tree[i][j])):
                cur = tree[i][j][a]
                if cur >= 5 and cur % 5 == 0:
                    for b in range(8):
                        nx = i + dx[b]
                        ny = j + dy[b]
                        if 0 <= nx < N and 0 <= ny < N:
                            tree[nx][ny].append(1)
    return

def winter():
    for i in range(N):
        for j in range(N):
            mapp[i][j] += A[i][j]
    return




N, M, K = map(int,input().split())

mapp = [[5] * N for _ in range(N)]
A = [list(map(int,input().split())) for _ in range(N)]
tree = [[[]for _ in range(N) ]for _ in range(N)]
dead = [[0]*N for _ in range(N)]

for i in range(M):
    cx,cy,ca = map(int,input().split())
    tree[cx-1][cy-1].append(ca)

for year in range(K):
    # spring()
    summer(spring())
    fall()
    winter()


cnt = 0
for i in range(N):
    for j in range(N):
        if tree[i][j]:
            cnt += len(tree[i][j])
print(cnt)
#X
# 최솟값의 초기화는 10**4 로 하면 될듯(20 * 100이 최대인 것 같음)
# 값 받을때도 나중에 편하려면 인덱스 맞추게 초반 정리를 좀 해야할 것 같다. 필요없나? 차라리 append를 해서 기본 dfs bfs했던 것 처럼?
# 아니 그냥 귀찮아지니까 나중에 처리

# 결국 다 해봐야 하는거라 dfs인듯
# dfs 백트래킹?
# 팀을 두 개 를 넣는걸 다 따로 visited해야한다. 그러니까 visited도 2차원 배열 사용
# 두 번 돌리는게 맞나? 어느팀이던 점수는 어차피 똑같은데? 그냥 리스트 2차원 써서 두 개의 팀으로 두고 나중에 연산
# calc에서 두 명이 아니라 3명 이상일 경우도 생각해야함.
# 1차 시도는 타임 아웃. 왜?? 처음에 굳이 for문을 돌릴 필요가 없는 것 같다. 순서가 중요하지 않음 (이건 맞았음)
# 2차 시도도 타임 아웃. 왜일까?????? 근본적인 로직이 잘못되어있을 확률이 높다. 굳이 리스트에 담고 따로 로직을 돌려서 나중에 계산하지 말고 한번에 해보자.
# 아니면 조기종료? 각 팀별로 점수를 인자로 계속넘겨서 해보자
# 기존의 2차시도 코드를 재활용해서 조기 종료만 달아봤는데  3차 시도 실패.
# 아예 새로 풀어보는게 나을듯
# 아 혹시 백트래킹으로 False를 다시 해주면 안되나? 중복이되네?



def calc(teams):
    t1,t2 = 0,0
    for i in teams[0]:
        for j in teams[0]:
            t1 += team[i][j]
    for i in teams[1]:
        for j in teams[1]:
            t2 += team[i][j]
    return t1,t2

def dfs(idx,visited,t):
    global min_val
    if len(t) == N//2:
            tl = [t,[]]
            for i in range(N):
                if not visited[i]:
                    tl[1].append(i)
            tmp1,tmp2 = calc(tl)
            min_val = min(min_val,abs(tmp1-tmp2))
            return
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            t.append(i)
            dfs(i+1,visited,t)
            t.pop()
            visited[i] = False
    return
            

N = int(input())
team = [list(map(int,input().split())) for _ in range(N)]
min_val = 10**4

t = []
visited = [False] * N
dfs(0,visited,t)


print(min_val)
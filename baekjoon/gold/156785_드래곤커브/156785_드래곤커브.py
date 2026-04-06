# 1시간 30분 초과
# 까먹을 것 같은 것 : 0 <= x <= 100 and 0 <= y <= 100
# 핵심 로직은 어떻게 드래곤 커브를 그릴 것인가.
# 커브의 로직 : K세대 커브는 K-1세대 커브를 끝점을 기준으로 90도 "시계 방향" 회전 시킨다음 끝점에 붙인 것.
# 이번 dx dy는 기존에 내가 쓰던거랑 방향과 시작점이 다름 주의
# 일단 처음은 0세대는 직접 그려주고 인자로 그 끝점을 x,y로 넘기기
# zip을 써써 붙여 넣어버릴까? -> 그러면 다른 커브랑 겹쳐지지 않고 덮어씌워진다( for문을 직접 돌리면 되긴함 ). 그리고 연산이 너무 많아짐
# 아니면 그렸던 기록을 가지고 연산을 하면? 꽤 괜찮은데
# 그냥 처음에 그려주지도 말고 재귀함수로 벽에 닿을때까지 계속 그리게? 아니면 while 써도 되고
# 커브 핵심 로직 : (d(원래 방향) + 1(한 번 그으면 시계방향으로 돌아야함, 그런데 그리는건 반대니 반시계로)) % 4?
# 이런 수 계산은 아닌 것 같다. 혹시 history를 반대로 그리나?
# 찾았다. 먼저 드래곤 커브의 끝점을 미리 찾아서 history처음부터 (d + 4 ) % 4이거다. 근데 이러면 처음부터도 되는거 아닌가?
# 맞다. hostory의 반대로 ((d+2)%4 + 3) % 4 이거다
# x랑 y는 반대로 써야한다 내 편의상. (안해도됨)
# 중간에 멈출게 필요하네. 같은게 반복되면 멈추는 로직 필요 스택 활용?

dx = [0,-1,0,1]
dy = [1,0,-1,0]
# > ^ < v
def draw(g,history):
    f = True
    global cx, cy 

    for z in range(g):
        for i in range(len(history)-1,-1,-1):
            d = history[i]
            nd = ((d+2)%4 + 3) % 4
            cx += dx[nd]
            cy += dy[nd]
            
            if 0 <= cx <= 100 and 0 <= cy <= 100:
                mapp[cx][cy] = True
                history.append((nd))

N = int(input())

curves = [list(map(int,input().split())) for _ in range(N)]
mapp = [[False] * 101 for _ in range(101)]

# 일단 드래곤 커브를 다 그리기
for y,x,d,g in curves:
    history = [(d)]
    
    cx = x + dx[d]
    cy = y + dy[d]
    mapp[x][y]  = True
    mapp[cx][cy] = True
    draw(g,history)
cnt = 0
for i in range(100):
    for j in range(100):
        # 정사각형이 겹쳐도 되는지 안되는지 몰라서 일단 겹치는걸로 구현.
        if mapp[i][j] and mapp[i+1][j] and mapp[i][j+1] and mapp[i+1][j+1]:
            cnt +=1

print(cnt)
            
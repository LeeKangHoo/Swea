#1시간 20분 초과 
# 구현 문제 같고 zip으로 돌려서 가로 새로 for문 굴려서 하면 될 것 같다.
# 밑에서 올라가는것도 할 수 있어야한다.
# for로 구현하기 힘들다. while로 해서 움직이는게 편할듯
# index error가 왜뜨지 자꾸? out of bound일텐데

def solve():
    cnt = 0
    r_mapp = list(map(list,zip(*mapp)))
    visited = [[False]*N for _ in range(N)]
    visited2 = [[False]*N for _ in range(N)]
    
    for i in range(N):
        c = 0
        f = True
        while c < N and f:
            f = True
            if c == N-1:
                cnt += 1
                break
            if mapp[i][c] == mapp[i][c+1]:
                c += 1
                continue
            elif mapp[i][c] - mapp[i][c+1] == 1:
                nc = mapp[i][c+1]
                for j in range(1,L+1):
                    if not(0 <= c+j < N and mapp[i][c+j] == nc) or visited[i][c+j]:
                        f = False

                if f:
                    visited[i][c+1:c+1+L] = [True] * L
                    c += L

            elif mapp[i][c] - mapp[i][c+1] == -1:
                for j in range(L):
                    if not(0 <= c-j < N and mapp[i][c-j] == mapp[i][c]) or visited[i][c-j]:
                        f = False
                if f:
                    visited[i][c-L+1:c+1] = [True] * L
                    c += 1
            else:
                f = False
        # 뒤집어서
        c = 0
        f = True
        while c < N and f:
            f = True
            if c == N-1:
                cnt += 1
                break
            if r_mapp[i][c] == r_mapp[i][c+1]:
                c += 1
                continue
            elif r_mapp[i][c] - r_mapp[i][c+1] == 1:
                nc = r_mapp[i][c+1]
                for j in range(1,L+1):
                    if not(0 <= c+j < N and r_mapp[i][c+j] == nc) or visited2[i][c+j]:
                        f = False
                
                if f:
                    visited2[i][c+1:c+1+L] = [True] * L
                    c += L
                else:
                    f = False

            elif r_mapp[i][c] - r_mapp[i][c+1] == -1:
                for j in range(L):
                    if not(0 <= c-j < N and r_mapp[i][c-j] == r_mapp[i][c]) or visited2[i][c-j]:
                        f = False
                if f:
                    visited2[i][c-L+1:c+1] = [True] * L
                    c += 1
                else:
                    f = False
            else:
                f = False

                        
    
    return cnt


N,L = map(int,input().split())

mapp = [list(map(int,input().split())) for _ in range(N)]

print(solve())
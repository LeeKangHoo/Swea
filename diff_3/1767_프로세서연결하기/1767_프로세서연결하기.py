import sys

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solve():
    T = int(sys.stdin.readline())
    for tc in range(1, T + 1):
        N = int(sys.stdin.readline())
        board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
        
        cores = []
        for r in range(1, N - 1): # 가장자리는 제외
            for c in range(1, N - 1):
                if board[r][c] == 1:
                    cores.append((r, c))
        
        max_core = 0
        min_dist = float('inf')
        num_cores = len(cores)

        def dfs(idx, core_cnt, dist_sum):
            nonlocal max_core, min_dist
            
            # 남은 코어를 다 합쳐도 현재 max_core보다 작으면 가지치기
            if core_cnt + (num_cores - idx) < max_core:
                return

            if idx == num_cores:
                if core_cnt > max_core:
                    max_core = core_cnt
                    min_dist = dist_sum
                elif core_cnt == max_core:
                    min_dist = min(min_dist, dist_sum)
                return

            r, c = cores[idx]
            
            # 4방향 시도
            for i in range(4):
                can_go = True
                nr, nc = r, c
                length = 0
                
                # 끝까지 갈 수 있는지 확인
                while True:
                    nr += dr[i]
                    nc += dc[i]
                    if not (0 <= nr < N and 0 <= nc < N):
                        break
                    if board[nr][nc] != 0:
                        can_go = False
                        break
                    length += 1
                
                if can_go:
                    # 전선 채우기
                    nr, nc = r, c
                    for _ in range(length):
                        nr += dr[i]
                        nc += dc[i]
                        board[nr][nc] = 2
                    
                    dfs(idx + 1, core_cnt + 1, dist_sum + length)
                    
                    # 전선 지우기 (백트래킹)
                    nr, nc = r, c
                    for _ in range(length):
                        nr += dr[i]
                        nc += dc[i]
                        board[nr][nc] = 0
            
            # 이 코어를 연결하지 않고 넘어가는 경우
            dfs(idx + 1, core_cnt, dist_sum)

        dfs(0, 0, 0)
        print(f"#{tc} {min_dist}")

solve()
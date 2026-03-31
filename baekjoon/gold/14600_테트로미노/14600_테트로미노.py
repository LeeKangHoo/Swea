#55
# 막대랑 정사각형은 그대로 하고 나머지 3개는 2X3 블럭값을 다 더하고 각 블럭들에서 비어있는 곳의 값을 빼면?
# 가로 한 번 세로 한 번으로 해서 for문 돌려보기
# 나머지 블럭 계산에서 리스트를 만들어서 일단 복사해서 담고 거기서 값을 빼면?

def solve(paper):
    global max_val
    r_paper = list(map(list,zip(*paper)))
    another = [[0]*3 for _ in range(2)]
    
    # 막대
    if 4 <= M: 
        for row in range(N):
            for col in range(M-3):
                max_val = max(max_val,sum(paper[row][col:col+4]))
    for row in range(M):
        for col in range(N-3):
            max_val = max(max_val,sum(r_paper[row][col:col+4]))

    # 상자
    if 2 <= M: 
        for row in range(N-1):
            for col in range(M-1):
                max_val = max(max_val,sum(paper[row][col:col+2])+sum(paper[row+1][col:col+2]))

    # 나머지(가로)
    if 3 <= M: 
        for row in range(N-1):
            for col in range(M-2):
                # another 리스트에 복사
                for a in range(2):
                    for b in range(3):
                        another[a][b] = paper[row+a][col+b]
                tmp_sum = sum(another[0]) + sum(another[1])

                # L
                for x in range(2):
                    for y in range(2):
                        tmp_minus = sum(another[x][y:y+2])
                        max_val = max(max_val,tmp_sum-tmp_minus)
                # Z
                max_val = max(max_val,tmp_sum - (another[0][0]+another[1][2]))
                max_val = max(max_val,tmp_sum - (another[1][0]+another[0][2]))
                # ㅜ
                max_val = max(max_val,tmp_sum - (another[0][0]+another[0][2]))
                max_val = max(max_val,tmp_sum - (another[1][0]+another[1][2]))
    # 나머지(세로)
    for row in range(M-1):
        for col in range(N-2):
            # another 리스트에 복사
            for a in range(2):
                for b in range(3):
                    another[a][b] = r_paper[row+a][col+b]
            tmp_sum = sum(another[0]) + sum(another[1])
            
            # L
            for x in range(2):
                for y in range(2):
                    tmp_minus = sum(another[x][y:y+2])
                    max_val = max(max_val,tmp_sum-tmp_minus)
            # Z
            max_val = max(max_val,tmp_sum - (another[0][0]+another[1][2]))
            max_val = max(max_val,tmp_sum - (another[1][0]+another[0][2]))
            # ㅜ
            max_val = max(max_val,tmp_sum - (another[0][0]+another[0][2]))
            max_val = max(max_val,tmp_sum - (another[1][0]+another[1][2]))


N, M = map(int,input().split())

paper = [list(map(int,input().split())) for _ in range(N)]
max_val = 0
solve(paper)
print(max_val)
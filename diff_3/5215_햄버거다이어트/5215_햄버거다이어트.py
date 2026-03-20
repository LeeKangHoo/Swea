def solve(idx, current_cal, current_score):
    global max_val
    
    if current_cal > L:
        return
        
    if current_score > max_val:
        max_val = current_score
        
    if idx == N:
        return
        
    solve(idx + 1, current_cal + info[idx][1], current_score + info[idx][0])
    
    solve(idx + 1, current_cal, current_score)

T = int(input())

for i in range(T):
    N, L = map(int, input().split())
    info = [tuple(map(int, input().split())) for _ in range(N)]
    
    max_val = 0
    solve(0, 0, 0)
    
    print(f'#{i+1} {max_val}')
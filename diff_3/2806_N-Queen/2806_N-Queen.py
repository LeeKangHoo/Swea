def check(current_row):
    for i in range(current_row):
        if row[current_row] == row[i] or abs(row[current_row] - row[i]) == abs(current_row - i):
            return False
    return True

def dfs(current_row):
    global count
    
    if current_row == N:
        count += 1
        return

    for col in range(N):
        row[current_row] = col
        
        if check(current_row):
            dfs(current_row + 1)
            
T = int(input())
for tc in range(T):
    N = int(input())
    row = [0] * N
    count = 0

    dfs(0)
    print(f"#{tc+1} {count}")
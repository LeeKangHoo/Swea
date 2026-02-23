#42
def count_space(N,K,v1):
    cnt = 0
    for r in range(N):
        row = [0] + v1[r] + [0]
        for i in range(len(row) - (K+1)):
            if 0 not in row[i+1 : i+K+1] and row[i] == 0 and row[i+K+1] == 0:
                cnt += 1

    for c in range(N):
        column = [0] + [v1[r][c] for r in range(N)] + [0]
        for i in range(len(column) - (K+1)):
            if 0 not in column[i+1 : i+K+1] and column[i] == 0 and column[i+K+1] == 0:
                cnt += 1

    return cnt



def solve():
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        v1 = []
        for j in range(N):
            v1.append(list(map(int, input().split()))) 

            
        result = count_space(N,K,v1)
        print(f"#{i+1} {result}")
        


if __name__ == "__main__":
    solve()
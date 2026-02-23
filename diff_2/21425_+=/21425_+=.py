#17
T = int(input())

def solve(A,B,N):
    cnt = 0
    while A <= N and B <= N:
        if A < B:
            A += B
        else:
            B += A
        cnt += 1
    return cnt
        
        
        

for i in range(T):
    A,B,N = map(int,input().split())
    print(solve(A,B,N))

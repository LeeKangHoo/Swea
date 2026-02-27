#
T = int(input())

memo = [0]*31

memo[1] = 1
memo[2] = 3

for i in range(T):
    N = int(input()) // 10
    for j in range(3,N+1):
        memo[j] = memo[j-1] + 2*memo[j-2]
    print(f"#{i+1} {memo[N]}")
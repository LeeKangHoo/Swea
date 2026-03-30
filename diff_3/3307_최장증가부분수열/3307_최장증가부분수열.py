#X
def lis_dp(arr):
    n = len(arr)
    if n == 0:
        return 0
        
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

T = int(input())

for tc in range(T):
    N = int(input())
    numbers = list(map(int,input().split()))
    print(f"#{tc+1} {lis_dp(numbers)}")

# 23
# DP문제.
# 이걸 어떻게 하면 DP로 풀 수 있을까?
# 거꾸로 100만원 부터 해서 50,000으로 나누고, 10,000으로 나누고, 5,000으로 나누고, 1,000으로 나누고 이런식으로 하면 되려나?
T = int(input())
dp = [[0] * 8 for _ in range(10 ** 6 + 1)]
for i in range(10**6,0,-1):
        cnt = 0
        c = i
        while i >= 10:
            if i >= 50000:
                i -= 50000
                dp[c][0] += 1
            elif i >= 10000:    
                i -= 10000
                dp[c][1] += 1
            elif i >= 5000:    
                i -= 5000
                dp[c][2] += 1
            elif i >= 1000:    
                i -= 1000
                dp[c][3] += 1
            elif i >= 500:    
                i -= 500
                dp[c][4] += 1
            elif i >= 100:    
                i -= 100
                dp[c][5] += 1
            elif i >= 50:    
                i -= 50
                dp[c][6] += 1
            elif i >= 10:    
                i -= 10
                dp[c][7] += 1

for tc in range(T):
    N = int(input())
    
    
    print(f'#{tc+1}')
    print(*dp[N])
        

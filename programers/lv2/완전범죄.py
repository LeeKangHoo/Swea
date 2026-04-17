def solution(info, n, m):
    dp = [float('inf')] * m
    
    dp[0] = 0

    for a_cost, b_cost in info:
        next_dp = [float('inf')] * m
        
        for cur_b in range(m):
            if dp[cur_b] == float('inf'):
                continue
            
            cur_a = dp[cur_b]
            
            if cur_b + b_cost < m:
                new_b = cur_b + b_cost
                if next_dp[new_b] > cur_a:
                    next_dp[new_b] = cur_a
            
            if cur_a + a_cost < n:
                new_a = cur_a + a_cost
                if next_dp[cur_b] > new_a:
                    next_dp[cur_b] = new_a
        
        dp = next_dp
        if all(val == float('inf') for val in dp):
            return -1

    ans = min(dp)
    return ans if ans != float('inf') else -1
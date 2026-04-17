# X
# 문제의 핵심 내용은 기억난다. 다음 인덱스의 값은 현재보다 무조건 커야하는 상황에서 이게 유지되는 마지막 수를 얻는 것.
# DP로 어떻게 풀 수 있을까?
# 내가 문제를 완전히 이해한게 아니다. 뭔가 이상하다
# 그 값에 해당하는 인덱스? 근데 문제 예시에 7?

T = int(input())

for tc in range(T):
    N = int(input())
    dp = [1] * (N)
    nums = list(map(int,input().split()))
    
    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1


    print(f'#{tc+1} {max(dp)}')  


#

T = int(input())

for i in range(T):
    N,M = map(int,input().split())
    
    nums = list(map(int,input().split()))

    for j in range(M%N):
        nums.append(nums.pop(0))

    print(f'#{i+1} {nums[0]}')



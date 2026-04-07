#11
# 가장 큰 수, 가장 작은 수를 넣고 그 수를 pop시키면 될 것 같은데? 아니면 범위를 정해주던가

def solve():
    r = []
    while nums:
        if len(nums) == 1:
            r.append(nums[0])
            break
        r.append(nums.pop(-1))
        r.append(nums.pop(0))
    
    return ' '.join(list(map(str,r[:10])))



T = int(input())

for tc in range(T):
    N = int(input())
    nums = list(map(int,input().split()))
    nums.sort()

    print(f'#{tc+1} {solve()}')
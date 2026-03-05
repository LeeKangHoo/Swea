#19

def solve(mapp):
    for i in range(dump):
        max_idx = mapp.index(max(mapp))
        min_idx = mapp.index(min(mapp))
        if mapp[max_idx] - mapp[min_idx] < 1:
            return mapp[max_idx] - mapp[min_idx]
        mapp[max_idx] = mapp[max_idx] - 1
        mapp[min_idx] = mapp[min_idx] + 1
    max_idx = mapp.index(max(mapp))
    min_idx = mapp.index(min(mapp))
    return mapp[max_idx] - mapp[min_idx]



for i in range(10):
    dump = int(input())
    mapp = list(map(int,input().split()))

    print(f"#{i+1} {solve(mapp)}")
    
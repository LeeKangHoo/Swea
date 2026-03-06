# 30
def solve(mapp):
    row_val = [sum(mapp[row]) for row in range(100)]
    col_val = [sum(col) for col in zip(*mapp)]
    d_val = 0
    r_d_val = 0
    for i in range(100):
        d_val += mapp[i][i]
        r_d_val += mapp[99-i][99-i]
    return max(max(row_val), max(col_val), d_val, r_d_val)




for i in range(10):
    T = int(input())
    mapp = []
    for j in range(100):
        mapp.append(list(map(int,input().split())))
    print(f"#{T} {solve(mapp)}")

    
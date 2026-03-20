#28
def solve(mapp):
    mapp_r = list(map(list,zip(*mapp)))
    global max_val
    
    for row in range(100):
        for i in range(99,0,-1):
            if i < max_val:
                    break
            for col in range(100-i):
                if mapp[row][col:col+i+1] == mapp[row][col:col+i+1][::-1]:
                    max_val = i+1
                    break
    for row in range(100):
        for i in range(99,0,-1):
            if i < max_val:
                    break
            for col in range(100-i):
                if mapp_r[row][col:col+i+1] == mapp_r[row][col:col+i+1][::-1]:
                    max_val = i+1
                    break

    


for i in range(10):
    n = int(input())
    mapp = [input() for _ in range(100)]
    max_val = 0
    solve(mapp)
    print(f"#{n} {max_val}")

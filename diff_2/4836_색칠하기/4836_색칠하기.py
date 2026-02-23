#18
T = int(input())

for i in range(T):
    N = int(input())
    cnt = 0
    red = [[False for _ in range(10)]for _ in range(10)]
    blue = [[False for _ in range(10)]for _ in range(10)]

    for j in range(N):
        tmp = list(map(int,input().split()))
        x1, y1, x2, y2, color = tmp

        for z in range(x1,x2+1):
            for x in range(y1,y2+1):
                if(color == 1):
                    red[z][x] = True
                else:
                    blue[z][x] = True
    
    for z in range(10):
        for x in range(10):
            if red[z][x] and blue[z][x]:
                cnt += 1
    print(f"#{i+1} {cnt}")
        

    
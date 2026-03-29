#20

for tc in range(10):
    N = int(input())

    result = list(map(int,input().split()))
    c_len = int(input())
    r = input().split('I')[1:]
    
    for command in r:
        cur = list(map(int, command.split()))
        
        x = cur[0]
        y = cur[1]
        s = cur[2:]

        result[x:x] = s
    result = " ".join(map(str,result[:10]))
    print(f"#{tc+1} {result}")


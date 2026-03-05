#
T = int(input())

for i in range(T):
    N = int(input())
    graph = [0] + list(map(int,input().split()))
    check = False
    while not check:
        for a in range(1,N+1):
                    if a * 2 > N:
                        break
                    if graph[a*2] < graph[a]:
                        graph[a*2], graph[a] = graph[a], graph[a*2]
                    if a * 2 + 1 > N:
                        break
                    if graph[a*2+1] < graph[a]:
                        graph[a*2+1], graph[a] = graph[a], graph[a*2+1]
        flag = True
        for x in range(1,N+1):
            if x * 2 > N:
                break
            if graph[x*2] < graph[x]:
                flag = False

            if x * 2 + 1 > N:
                break
            if graph[x*2+1] < graph[x]:
                flag = False
        if flag:
            check = True
    r = 0
    number = N
    while number > 1:
        if number % 2 == 0:
            number = number//2
            r += graph[number]
            continue
        
        if number % 2 == 1:
            number = (number - 1)//2
            r += graph[number]
            
        

    print(f"#{i+1} {r}")
#18
def dfs(cur,P,numbers,visited):
    
    if cur in visited:
        return visited.index(cur)
    else:
        visited.append(cur)
        num = 0
        for i in range(len(cur)):
            num += int(cur[i]) ** P
        return dfs(str(num),P,numbers,visited)



A, P = input().split()
P = int(P)


numbers = [A]
visited = []

print(dfs(A,P,numbers,visited))

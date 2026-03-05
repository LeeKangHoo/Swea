#21
T = int(input())

r = []
for i in range(T):
    X,Y,Z = map(int,input().split())
    max_val = max(X,Y,Z)
    min_val = min(X,Y,Z)

    if X == Y and Y == Z:
        print(f"{X} {Y} {Z}")
    elif X == Y and max_val == X:
        print(f"{min_val} {max_val} {min_val}")   
    elif X == Z and max_val == X:
        print(f"{max_val} {min_val} {min_val}")
    elif Y == Z and max_val == Y:
        print(f"{min_val} {min_val} {max_val}")
    else:
        print(f"-1 -1 -1")
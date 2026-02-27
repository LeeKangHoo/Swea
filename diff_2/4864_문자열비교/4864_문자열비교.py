#2
T = int(input())

for i in range(T):
    v1 = input()
    v2 = input()
    if v1 in v2:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")
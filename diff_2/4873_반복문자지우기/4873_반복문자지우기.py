#9
T = int(input())
for i in range(T):
    v1 = input()
    cnt = 0
    s1 = []
    for a in v1:
        if s1 and s1[-1] == a:
            s1.pop()
            cnt += 1
        else:
            s1.append(a)
    print(f"#{i+1} {len(s1)}")
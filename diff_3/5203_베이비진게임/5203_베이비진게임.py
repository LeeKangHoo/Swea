#21
def judge(p1,p2):
    c1 = sorted(set(p1))
    c2 = sorted(set(p2))
    # p1
    for i in c1:
        if p1.count(i) >= 3:
            return 1
    for i in range(len(p1)-3):
        if c1[i] + 1 == c1[i+1] and c1[i+1] + 1 == c1[i+2]:
            return 1
    # p2
    for i in c2:
        if p2.count(i) >= 3:
            return 2
    for i in range(len(p2)-3):
        if c2[i] + 1 == c2[i+1] and c2[i+1] + 1 == c2[i+2]:
            return 2
    return 0


def solve(cards):
    p1 = []
    p2 = []
    for turn in range(0,12,2):
        p1.append(cards[turn])
        p2.append(cards[turn+1])
        c = judge(p1,p2)
        if c != 0:
            return c
    return 0


T = int(input())

for tc in range(T):
    cards = list(map(int,input().split()))

    print(f'#{tc+1} {solve(cards)}')
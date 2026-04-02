#12

def solve(cards):
    mid = int((len(cards) / 2) + 0.5)
    shuffle1 = cards[:mid]
    shuffle2 = cards[mid:]
    r = []

    for i in range(mid):
        r.append(shuffle1[i])
        if len(shuffle2) > i:
            r.append(shuffle2[i])
    return ' '.join(r)



T = int(input())

for tc in range(T):
    N = int(input())

    cards = list(input().split())
    
    print(f"#{tc+1} {solve(cards)}")
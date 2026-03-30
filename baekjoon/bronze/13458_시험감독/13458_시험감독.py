#13

N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())
cnt = 0
for i in A:
    if i-B <= 0:
        cnt += 1
        continue
    if (i-B)%C == 0:
        cnt += 1 + (i-B)//C
    else:
        cnt += 2 + (i-B)//C

print(cnt)

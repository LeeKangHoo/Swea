#17
T = int(input())

def solve(num):
    r = ""
    cnt = 0
    while num > 0:
        num *= 2
        bit = int(num)
        r += str(bit)

        cnt += 1
        num -= bit
        if cnt > 12:
            return "overflow"

    return r
     

for i in range(T):
    num = float(input())
    print(f"#{i+1} {solve(num)}")
     
#11
T = int(input())

def solve(time):
    h = (time[0] + time[2]) % 12
    h += int((time[1] + time[3]) / 60)
    m = (time[1] + time[3]) % 60
    r = [h,m]
    return r



for i in range(T):
    time = list(map(int,input().split()))
    print(f"#{i+1}",*solve(time))

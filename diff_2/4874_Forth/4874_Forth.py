#29
def solve(n):
    stack = []
    for cur in n:

        if cur == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return "error"
        elif cur.isdigit():
            stack.append(int(cur))
        elif cur in ['+','-','*','/','%']:
            if len(stack) < 2:
                return "error"               
            v2 = stack.pop()
            v1 = stack.pop()

            if cur == '+':
                 stack.append(v1 + v2)
            elif cur == '-':
                stack.append(v1 - v2)
            elif cur == '*':
                stack.append(v1 * v2)
            elif cur == '/':
                stack.append(v1 // v2)
            elif cur == '%':
                stack.append(v1 % v2)
        else:
            return "error"
            
    return "error"


        

T = int(input())

for i in range(T):
    n = list(input().split())
    print(f"#{i+1} {solve(n)}")
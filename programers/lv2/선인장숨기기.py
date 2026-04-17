# X
from collections import deque

def solution(m, n, h, w, drops):
    inf = float('inf')
    desert = [[inf] * n for _ in range(m)]
    for i, (x, y) in enumerate(drops):
        desert[x][y] = i + 1

    def get_sliding_min(arr, k):
        res = []
        dq = deque()
        for i in range(len(arr)):
            if dq and dq[0] <= i - k:
                dq.popleft()
            while dq and arr[dq[-1]] >= arr[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(arr[dq[0]])
        return res

    row_min = []
    for r in range(m):
        row_min.append(get_sliding_min(desert[r], w))

    final_ans = [0, 0]
    max_min_val = -1
    
    for c in range(n - w + 1):
        col_data = [row_min[r][c] for r in range(m)]
        col_min_list = get_sliding_min(col_data, h)
        
        for r, current_min in enumerate(col_min_list):
            if current_min == inf:
                return [r, c]
            
            if current_min > max_min_val:
                max_min_val = current_min
                final_ans = [r, c]

    return final_ans
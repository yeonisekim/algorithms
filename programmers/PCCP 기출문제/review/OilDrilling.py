from collections import deque

def solution(land):
    rows, cols = len(land), len(land[0])
    visited = [[False] * cols for _ in range(rows)]
    col_sum = [0] * cols

    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    for sr in range(rows):
        for sc in range(cols):
            if land[sr][sc] == 1 and not visited[sr][sc]:
                q = deque([(sr, sc)])
                visited[sr][sc] = True

                size = 0
                touched_cols = set()

                while q:
                    r, c = q.popleft()
                    size += 1
                    touched_cols.add(c)

                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if land[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))

                for c in touched_cols:
                    col_sum[c] += size

    return max(col_sum) if col_sum else 0

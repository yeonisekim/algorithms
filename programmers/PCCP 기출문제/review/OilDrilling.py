from collections import deque

def solution(land):
    rows = len(land)
    cols = len(land[0])

    label = 0
    labels = [[0] * cols for _ in range(rows)]
    oils = [0] * (rows * cols + 1)

    nx = [1, -1, 0, 0]
    ny = [0, 0, 1, -1]

    for r in range(rows):
        for c in range(cols):
            if land[r][c] == 1 and labels[r][c] == 0:
                q = deque()
                q.append((r, c))

                label += 1
                labels[r][c] = label

                size = 0

                while q:
                    dx, dy = q.popleft()
                    size += 1

                    for i in range(4):
                        cx = dx + nx[i]
                        cy = dy + ny[i]

                        if (0 <= cx < rows and 0 <= cy < cols and
                            land[cx][cy] == 1 and labels[cx][cy] == 0):
                            q.append((cx, cy))
                            labels[cx][cy] = label

                oils[label] = size

    answer = 0

    for c in range(cols):
        total = 0
        net = set()

        for r in range(rows):
            l = labels[r][c]
            if l > 0 and l not in net:
                net.add(l)
                total += oils[l]

        answer = max(answer, total)

    return answer

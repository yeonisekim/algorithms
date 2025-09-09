// 2번 석유 시추
// 2025-09-06 Sat

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

class OilDrilling {
    public int solution(int[][] land) {
        int rows = land.length;
        int cols = land[0].length;

        int label = 0;
        int[][] labels = new int[rows][cols];
        int[] oils = new int[rows * cols + 1];

        int[] nx = {1, -1, 0, 0};
        int[] ny = {0, 0, 1, -1};

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (land[r][c] == 1 && labels[r][c] == 0) {
                    Deque<int[]> deque = new ArrayDeque<>();
                    deque.add(new int[]{r, c});

                    label++;
                    labels[r][c] = label;

                    int size = 0;

                    while (!deque.isEmpty()) {
                        int[] d = deque.poll();
                        int dx = d[0];
                        int dy = d[1];
                        size++;

                        for (int i = 0; i < 4; i++) {
                            int cx = nx[i] + dx;
                            int cy = ny[i] + dy;

                            if (0 <= cx && cx < rows && 0 <= cy && cy < cols && land[cx][cy] == 1 && labels[cx][cy] == 0) {
                                deque.add(new int[]{cx, cy});
                                labels[cx][cy] = label;
                            }
                        }
                    }

                    oils[label] = size;
                }
            }
        }

        int answer = 0;

        for (int c = 0; c < cols; c++) {
            int total = 0;
            Set<Integer> net = new HashSet<>();

            for (int r = 0; r < rows; r++) {
                int l = labels[r][c];
                if (l > 0 && net.add(l)) {
                    total += oils[l];
                }
            }

            answer = Math.max(answer, total);
        }

        return answer;
    }

    public static void main(String[] args) {
        OilDrilling solution = new OilDrilling();

        // int answer = solution.solution(new int[][]{{0, 0, 0, 1, 1, 1, 0, 0}, {0, 0, 0, 0, 1, 1, 0, 0}, {1, 1, 0, 0, 0, 1, 1, 0}, {1, 1, 1, 0, 0, 0, 0, 0}, {1, 1, 1, 0, 0, 0, 1, 1}});
        int answer = solution.solution(new int[][]{{1, 0, 1, 0, 1, 1}, {1, 0, 1, 0, 0, 0}, {1, 0, 1, 0, 0, 1}, {1, 0, 0, 1, 0, 0}, {1, 0, 0, 1, 0, 1}, {1, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 1}});

        System.out.println(answer);
    }
}

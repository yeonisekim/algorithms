// 2번 퍼즐 게임 챌린지
// 2025-09-06 Sat
class PuzzleGameChallenge {
    public int solution(int[] diffs, int[] times, long limit) {
        int lo = 1;
        int hi = 100_000;

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            
            if (canSolve(diffs, times, limit, mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        } 

        return lo;
    }

    private boolean canSolve(int[] diffs, int[] times, long limit, int level) {
        for (int i = 0; i < diffs.length; i++) {
            if (diffs[i] <= level) {
                limit -= times[i];
            } else {
                long failure = diffs[i] - level;
                long prevTime = i == 0 ? 0 : times[i - 1];
                long usedTime = (failure * (times[i] + prevTime)) + times[i];
                limit -= usedTime;
            }

            if (limit < 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        PuzzleGameChallenge solution = new PuzzleGameChallenge();

        // int answer = solution.solution(new int[]{1, 4, 4, 2}, new int[]{6, 3, 8, 2}, 59);
        int answer = solution.solution(new int[]{1, 5, 3}, new int[]{2, 4, 7}, 30);

        System.out.println(answer);
    }
}

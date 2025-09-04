// 1번 붕대 감기
// 2025-09-01 Mon
class BandageWrapping {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int castTime = bandage[0];
        int healPerSecond = bandage[1];
        int extraHeal = bandage[2];
        int maxHealth = health;
        int lastAttackTime = 0;

        int timeGap;
        int extraHealCount;
        for (int[] attack : attacks) {
            timeGap = attack[0] - lastAttackTime - 1;
            extraHealCount = timeGap / castTime;
            lastAttackTime = attack[0];
            
            health = Math.min(maxHealth, health + (timeGap * healPerSecond));
            health = Math.min(maxHealth, health + (extraHealCount * extraHeal));

            health -= attack[1];

            if (health <= 0) {
                return -1;
            }
        }

        return health;
    }

    public static void main(String[] args) {
        BandageWrapping solution = new BandageWrapping();

        int answer = solution.solution(new int[]{5, 1, 5}, 30, new int[][]{{2, 10}, {9, 15}, {10, 5}, {11, 5}});

        System.out.println(answer);
    }
}

// 1번 붕대 감기
// 2025-09-01 Mon

import java.util.HashMap;
import java.util.Map;

class BandageWrapping {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int castTime = bandage[0];
        int healPerSecond = bandage[1];
        int extraHeal = bandage[2];
        int maxHealth = health;

        Map<Integer, Integer> attacksMap = new HashMap<>();
        for (int[] attack : attacks) {
            attacksMap.put(attack[0], attack[1]);
        }

        int consecutiveSuccess = 0;
        for (int i = 1; i <= attacks[attacks.length - 1][0]; i++) {
            if (attacksMap.containsKey(i)) {
                consecutiveSuccess = 0;
                health -= attacksMap.get(i);

                if (health <= 0) {
                    return -1;
                }

                continue;
            }

            consecutiveSuccess++;
            health = Math.min(health + healPerSecond, maxHealth);

            if (consecutiveSuccess == castTime) {
                health = Math.min(health + extraHeal, maxHealth);
                consecutiveSuccess = 0;
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

def solution(bandage, health, attacks):
    cast_time = bandage[0]
    heal_per_second = bandage[1]
    extra_heal = bandage[2]
    max_health = health
    last_attack_time = 0

    for attack_time, damage in attacks:
        time_gap = attack_time - last_attack_time - 1
        extra_heal_count = time_gap // cast_time
        last_attack_time = attack_time

        health = min(max_health, health + (time_gap * heal_per_second))
        health = min(max_health, health + (extra_heal_count * extra_heal))

        health -= damage

        if health <= 0:
            return -1

    return health

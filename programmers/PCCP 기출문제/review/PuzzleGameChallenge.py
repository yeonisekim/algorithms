def solution(diffs, times, limit):
    lo = 1
    hi = 100_000

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if can_solve(diffs, times, limit, mid):
            hi = mid
        else:
            lo = mid + 1

    return lo

def can_solve(diffs, times, limit, level):
    for idx in range(len(diffs)):
        if diffs[idx] <= level:
            limit -= times[idx]
        else:
            failure = diffs[idx] - level
            prev_time = 0 if idx == 0 else times[idx - 1]
            used_time = failure * (times[idx] + prev_time) + times[idx]
            limit -= used_time
        
        if limit < 0:
            return False
        
    return True

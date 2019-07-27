
def find_best_defence(attack, defense, n):
    max_diff = 0
    max_defense = -1
    for i in xrange(0, n):
        prev_idx = (i-1)%n
        next_idx = (i+1)%n
        diff = defense[i] - attack[prev_idx] - attack[next_idx]
        if diff > max_diff:
            max_defense = defense[i]
            max_diff =  diff
    return max_defense

def run():
    n = int(raw_input())
    for i in xrange(0,n):
        arr_count = int(raw_input())
        attack = raw_input().split()
        attack = [int(x) for x in attack]
        defense = raw_input().split()
        defense = [int(x) for x in defense]
        print find_best_defence(attack, defense, arr_count)
run()

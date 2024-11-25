# Chef is playing a video game, and is now fighting the final boss.

# The boss has H health points. Each attack of Chef reduces the health of the boss by X. Chef also has a special attack that can be used at most once, and will decrease the health of the boss by Y.

# Chef wins when the health of the boss is ≤ 0. What is the minimum number of attacks needed by Chef to win?

# Input Format:
# The first line of input will contain a single integer T, denoting the number of test cases. The first and only line of each test case will contain three space-separated integers H,X,Y — the parameters described in the statement.

# Output Format:
# For each test case, output on a new line the minimum number of attacks needed by Chef to win.


# h = boss health
# x = attack point
# y = special attack point - max 1 time usable
test_case = int(input())
for _ in range(test_case):
    h, x, y = map(int, input().split())
    special_attack_count = 1 # used special health
    health_after_special_attack = h - y
    special_attack_count = 1
    
    # if chef decides to use special attack
    if health_after_special_attack <= 0:
        total_attacks = special_attack_count
    else:
        normal_attack_count = (health_after_special_attack + x - 1) // x
        total_attacks = normal_attack_count + special_attack_count
        
    # if chef don't use special attack and normal attack is sufficient
    normal_attack = (h + x - 1) // x
    print(min(normal_attack, total_attacks))
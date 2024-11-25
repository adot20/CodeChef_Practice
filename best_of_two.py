# Alice and Bob are playing a game. Each player rolls a regular six faced dice 3 times.
# The score of a player is the sum of the values of the highest 2 rolls. The player with the highest score wins, and the game ends in a Tie if both players have the same score.

# Input Format:
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case contains six space-separated integers A1, A2, A3, B1, B2 and B3 — the values Alice gets in her 3 dice rolls, followed by the values which Bob gets in his 3 dice rolls.

# Output Format:
# For each test case, output on a new line Alice if Alice wins, Bob if Bob wins and Tie in case of a tie.

test_case = int(input())
for _ in range(test_case):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    alice_min_dice = min(a1, a2, a3)
    bob_min_dice = min(b1, b2, b3)
    alice_best_two_dice = (a1 + a2 + a3) - alice_min_dice
    bob_best_two_dice = (b1 + b2 + b3) - bob_min_dice
    if alice_best_two_dice > bob_best_two_dice:
        print("Alice")
    elif bob_best_two_dice > alice_best_two_dice:
        print("Bob")
    else:
        print("TIE")
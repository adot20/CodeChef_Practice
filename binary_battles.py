# N teams have come to participate in a competitive coding event called “Binary Battles”. It is a single-elimination tournament consisting of several rounds.
# Note: It is known that N is a power of 2.
# The organizers want to find the total time the event will take to complete. It is given that each round spans A minutes, and that there is a break of B minutes between every two rounds (no break after the last round).

# Input Format:
# The first line of input will contain a single integer T, denoting the number of test cases. Then the test cases follow.
# The first and only line of each test case contains three space-separated integers N, A and B respectively — the number of teams, the duration of each round and the length of the breaks between rounds.

# Output Format:
# For each test case, output on a new line the time taken in minutes for the whole event to finish.

import math

test_case = int(input())
for _ in range(test_case):
    num, a, b = map(int, input().split())
    power = math.log2(num)
    game_round = power
    total_time = (game_round * a) + ((game_round - 1) * b)
    print(int(total_time))
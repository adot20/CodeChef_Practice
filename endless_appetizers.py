# Chef's colleague issued a challenge to Chef: "If you eat more than X mozzarella sticks, I'll give you 30 rupees for each extra one you eat".
# For example, if X=5 and Chef eats 8 sticks, he would receive 90 rupees because he ate 3 extra sticks.
# You know that the restaurant serves Y mozzarella sticks per plate.
# You also know that Chef received R rupees from his colleague as a result of the challenge.
# What's the maximum number of plates of mozzarella sticks that Chef could have ordered?

# Input: Each test case consists of one line of input, containing three space-separated integers X,Y, and R — the lower limit on the number of sticks, the number of sticks on a single plate, and the money received by Chef
# Output: For each test case, output on a new line the answer: the maximum number of plates Chef could have ordered.

# Note: It is guaranteed that R is a multiple of 30.

# y = count of mozzarella sticks per plate
# x = total stics he had
# r = rupees he got for the challenge
# output: the max number of plates chef ordered.
test_case = int(input())

for _ in range(test_case):
    x, y, r = map(int, input().split())
    z = r // 30 # extra sticks he had for the challenge
    total_sticks = x + z
    if total_sticks % y == 0:
        plates_needs = (x+z) // y
    else:
        plates_needs = ((x+z) // y) + 1
    print(plates_needs)
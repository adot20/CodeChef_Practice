# The summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room cool. He has two options available:

# 1. Rent a cooler at the cost of X coins per month.
# 2. Purchase a cooler for Y coins.
#Chef wonders what is the maximum number of months for which he can rent the cooler such that the cost of renting is strictly less than the cost of purchasing it.

# Input Format:
# The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains two integers X and Y, as described in the problem statement.

#Output Format:
# For each test case, output the maximum number of months for which he can rent the cooler such that the cost of renting is strictly less than the cost of purchasing it.

# If Chef should not rent a cooler at all, output 0.

test_case = int(input())
for _ in range(test_case):
    rent, purchase = map(int, input().split())
    if rent >= purchase:
        print(0) # no need to rent if rent >= purchase
    else:
        result = (purchase - 1) // rent # to maintain strict inequality
        print(result)
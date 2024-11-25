# Chef has fallen in love with Cheffina, and wants to buy N gifts for her. On reaching the gift shop, Chef got to know the following two things:

# The cost of each gift is 1 coin.
# On the purchase of every 4th gift, Chef gets the 5th gift free of cost.
# What is the minimum number of coins that Chef will require in order to come out of the shop carrying N gifts?

# Output Format:
# For each test case, output on a new line the minimum number of coins that Chef will require to obtain all N gifts.

test_case = int(input())
for _ in range(test_case):
    n = int(input()) # purchased number of gifts
    if n <= 4:
        total_cost = n
    else:
        z = n // 5 # number of free gifts
        actual_purchased = n - z
        total_cost = actual_purchased * 1 # 1 coin per gift
    print(total_cost)
# Chef gets the following offer:
# If Chef buys 3 items then he gets the item (out of those 3 items) having the lowest price as free.

#For e.g. if Chef bought 3 items with the cost 6, 2 and 4, then he would get the item with cost 2 as free. So he would only have to pay the cost of the other two items which will be 6+4=10.

#Chef buys 3 items having prices A, B and C respectively.
# What is the amount of money Chef needs to pay?

test_case = int(input())
for _ in range(test_case):
    a, b, c = map(int, input().split())
    minimum_amt_product = min(a, b, c)
    total_price = a + b + c
    chef_pays = total_price - minimum_amt_product
    print(chef_pays)


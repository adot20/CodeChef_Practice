# Chef bought N items from a shop. Although it is hard to carry all these items in hand, so Chef has to buy some polybags to store these items.

# 1 polybag can contain at most 10 items. What is the minimum number of polybags needed by Chef?

# Input Format:
# The first line will contain an integer T - number of test cases. Then the test cases follow.
# The first and only line of each test case contains an integer N - the number of items bought by Chef.

# Output Format:
#For each test case, output the minimum number of polybags required.

test_case = int(input())
for _ in range(test_case):
    total_items = int(input())
    per_bag_items = 10
    
    if total_items % 10 == 0:
        polybag_required = total_items // per_bag_items
    else:
        polybag_required = (total_items // per_bag_items) + 1
    print(polybag_required)
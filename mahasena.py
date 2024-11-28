# Kattapa was known to be a very superstitious person. He believed that a soldier is "lucky" if the soldier is holding an even number of weapons, and "unlucky" otherwise. He considered the army as "READY FOR BATTLE" if the count of "lucky" soldiers is strictly greater than the count of "unlucky" soldiers, and "NOT READY" otherwise.
# Given the number of weapons each soldier is holding, your task is to determine whether the army formed by all these soldiers is "READY FOR BATTLE" or "NOT READY".


# Input Format
# The first line of input consists of a single integer N denoting the number of soldiers. The second line of input consists of N space separated integers A1, A2, ..., AN, where Ai denotes the number of weapons that the ith soldier is holding.

# Output Format
# Generate one line output saying "READY FOR BATTLE", if the army satisfies the conditions that Kattapa requires or "NOT READY" otherwise (quotes for clarity).


soldiers = int(input())
weapons = list(map(int, input().split()))
lucky_soldiers = 0
unlucky_soldiers = 0

for w in weapons:
    if w % 2 == 0:
        lucky_soldiers += 1
    else:
        unlucky_soldiers += 1

if lucky_soldiers > unlucky_soldiers:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
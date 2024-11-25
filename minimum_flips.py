# Chef has an array A of length N consisting of 1 and -1 only.

# In one operation, Chef can choose any index i (1≤i≤N) and multiply the element Ai by -1.
# Find the minimum number of operations required to make the sum of the array equal to 0.
# Output -1 if the sum of the array cannot be made.

# Output Format: 
# For each test case, output the minimum number of operations to make the sum of the array equal to 0. Output -1 if it is not possible to make the sum equal to 0.

test_case = int(input())
for _ in range(test_case):
    N = int(input())
    arr = list(map(int, input().split()))
    count_one = arr.count(1)
    count_neg_one = arr.count(-1)
    diff_of_count = abs(count_one - count_neg_one)
    # checking even case, that will be the cases where we can have the sum to 0
    if (count_one + count_neg_one) % 2 == 0:
        print(diff_of_count // 2) # operation req
    else: #if their count are odd
        print(-1) # no operation req since it's not possible to sum to 0 in case of odd 1 and -1
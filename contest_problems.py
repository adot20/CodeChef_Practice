# Given a list of N contest codes, where each contest code is either START38 or LTIME108, help Chef count how many problems were featured in each of the contests.

# Input Format:
# First line will contain T, number of test cases. Then the test cases follow.
# Each test case contains of two lines of input.
# First line of input contains the total count of problems that appeared in the two recent contests - N.
# Second line of input contains the list of N contest codes. Each code is either START38 or LTIME108, to which each problem belongs.

# Output Format: 
#For each test case, output two integers in a single new line - the first integer should be the number of problems in START38, and the second integer should be the number of problems in LTIME108.




test_case = int(input())

for _ in range(test_case):
    number = int(input())
    problem_codes = input().split()
    
    result_one = 0
    result_two = 0
    for codes in problem_codes:
        if codes == "START38":
            result_one += 1
        elif codes == "LTIME108":
            result_two += 1
    print(result_one, result_two)

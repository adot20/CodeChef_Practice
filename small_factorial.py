# Small Factorial
# Write a program to find the factorial value of any number entered by the user.

# Input Format:
# The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains an integer N.

# Output Format:
# For each test case, display the factorial of the given number N in a new line.

def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    print(factorial(n))
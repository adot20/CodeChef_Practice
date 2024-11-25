# Chef is standing at coordinate A while Chefina is standing at coordinate B.
# In one step, Chef can increase or decrease his coordinate by at most K.Determine the minimum number of steps required by Chef to reach Chefina.

# Input Format:
# The first line of input will contain a single integer T, denoting the number of test cases. 
# Each test case consists of three integers A,B, and K, the initial coordinate of Chef, the initial coordinate of Chefina and the maximum number of coordinates Chef can move in one step.

# Output Format: For each test case, output the minimum number of steps required by Chef to reach Chefina.

# a = chef coordinate
# b = chefina coordinate
# k = max number of coordinates Chef can move in one step
test_case = int(input())
for _ in range(test_case):
    a, b, k = map(int, input().split())
    coordination_diff = abs(b - a)
    print(coordination_diff//k if coordination_diff % k == 0 else (coordination_diff//k)+1)
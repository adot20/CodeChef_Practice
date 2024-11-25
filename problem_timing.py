# There are two problems in a contest.
# Problem A is worth 500 points at the start of the contest.
# Problem B is worth 1000 points at the start of the contest.

# Once the contest starts, after each minute: 
# Maximum points of Problem A reduce by 2 points.
# Maximum points of Problem B reduce by 4 points.
# It is known that Chef requires X minutes to solve Problem A correctly and Y minutes to solve Problem B correctly.
# Find the maximum number of points Chef can score if he optimally decides the order of attempting both the problems.

test_problem = int(input())
    
def max_points(x, y):
    p_A = 2 # points reduced each minute while solving A
    p_B = 4 # points reduced each minute while solving B
    points_solving_AtoB = (500 - (x*p_A)) + (1000 - (x+y)*p_B)
    points_solving_BtoA = (1000 - (y*p_B)) + (500 - (x+y)*p_A)
    return max(points_solving_AtoB, points_solving_BtoA)

for _ in range(test_problem):
    x, y = map(int, input().split())
    print(max_points(x, y))
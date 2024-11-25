# Two friends Chef and Chefina are currently on floors A and B respectively. They hear an announcement that prizes are being distributed on the ground floor and so decide to reach the ground floor as soon as possible.

# Chef can climb down X floors per minute while Chefina can climb down Y floors per minute. Determine who will reach the ground floor first (ie. floor number 0). In case both reach the ground floor together, print Both.

# Input Format:
#The first line of input will contain a single integer T, denoting the number of test cases.
#The first line of each test case contains four space-separated integers A, B, X, and Y — the current floor of Chef, the current floor of Chefina, speed of Chef and speed of Chefina in floors per minute respectively.

# Output Format:
# For each test case, output on a new line:
# Chef if Chef reaches the ground floor first.
# Chefina if she reaches the ground floor first.
# Both if both reach the ground floor at the same time.

test_case = int(input())
for _ in range(test_case):
    chef_floor, chefina_floor, chef_speed, chefina_speed = map(int, input().split())
    time_by_chef = chef_floor / chef_speed
    time_by_chefina = chefina_floor / chefina_speed
    if time_by_chef == time_by_chefina:
        print("Both")
    elif time_by_chef < time_by_chefina:
        print("Chef") # Chef taking less time to reach ground floor
    else: # time_by_chefina < time_by_chef
        print("Chefina") # Chefina taking less time ot reach ground floor
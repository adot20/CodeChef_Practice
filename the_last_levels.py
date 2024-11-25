test_case = int(input("Test case: "))
for _ in range(test_case):
    x, y, z = map(int, input("x, y, z: ").split())
    # z min of break in every 3 level of completion
    #let's wrap the game in 3 level for one round
    if x % 3 == 0:
        round_game = x // 3
    else:
        round_game  = (x // 3) + 1
    break_req = (round_game - 1) * z
    time_to_complete_the_game = (x * y) + break_req
    print(time_to_complete_the_game)
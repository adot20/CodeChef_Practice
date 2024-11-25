# Chef and Races
# The National Championships are starting soon. There are 4 race categories, numbered from 1 to 4, that Chef is interested in. Chef is participating in exactly 2 of these categories.

# Chef has an arch-rival who is, unfortunately, the only person participating who is better than Chef, i.e, Chef can't defeat the arch-rival in any of the four race categories but can defeat anyone else. Chef's arch-rival is also participating in exactly 2 of the four categories.

# Chef hopes to not fall into the same categories as that of the arch-rival.

# Given X,Y,A,B where X,Y are the races that Chef participates in and A,B are the races that Chef's arch-rival participates in, find the maximum number of gold medals (first place) that Chef can win.

test_case = int(input())
for _ in range(test_case):
    x, y, a, b = map(int, input().split())
    if (x == a and y == b) or (x == b and y == a):
        print(0) # if they match in both the race
    elif x == a or x == b or y == a or y == b:
        print(1) # if they match in any one
    elif (x != a and y != b) or (x != b and y != a):
        print(2) # if they natch in none
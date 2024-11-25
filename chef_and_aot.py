# Chef is a very big fan of Eren Yeager.

# In the last season of Attack on Titan, there were N episodes numbered from 1 to N. Each even indexed episode was A minutes long and each odd indexed episode was B minutes long.

# Calculate the total duration (in minutes) of the last season.

test_duration = int(input())

for _ in range(test_duration):
    episode_num, even_indexed_min, odd_indexed_min = map(int, input().split())
    if episode_num >= 1:
        even_episodes = episode_num // 2
        odd_episodes = episode_num - even_episodes
        total_duration = (even_episodes * even_indexed_min) + (odd_episodes * odd_indexed_min)
        print(total_duration)
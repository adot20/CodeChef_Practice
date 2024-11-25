# Water Mixing
# Chef is setting up a perfect bath for himself. He has X litres of hot water and Y litres of cold water.

# The initial temperature of water in his bathtub is A degrees. On mixing water, the temperature of the bathtub changes as following:
# The temperature rises by 1 degree on mixing 1 litre of hot water.
# The temperature drops by 1 degree on mixing 1 litre of cold water. 

# Determine whether he can set the temperature to B degrees for a perfect bath.


test_water = int(input())
for i in range(test_water):
    initial_temp, final_temp, hot_water, cold_water = map(int, input().split())
    
    if initial_temp > final_temp: # require cold water
        temp_diff = initial_temp - final_temp
        if cold_water >= temp_diff:
            print("YES")
        else:
            print("NO")
    elif initial_temp == final_temp:
            print("YES")
    else : # final temp > initial temp
        tem_diff = final_temp - initial_temp # require hot water
        if hot_water >= tem_diff:
            print("YES")
        else:
            print("NO")
        
        
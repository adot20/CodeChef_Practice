# Chef and his Apps
# Chef's phone has a total storage of S MB. Also, Chef has 2 apps already installed on his phone which occupy X MB and Y MB respectively.
#He wants to install another app on his phone whose memory requirement is Z MB. For this, he might have to delete the apps already installed on his phone.

# Determine the minimum number of apps he has to delete from his phone so that he has enough memory to install the third app.

test_storage = int(input())
for _ in range(test_storage):
    storage, appOne, appTwo, new_app = map(int, input().split())
    used_storage = appOne + appTwo
    remain_storage = storage - used_storage
    if new_app <= remain_storage:
        print(0) # enough storage available
    elif new_app <= (storage - appOne) or new_app <= (storage - appTwo):
        print(1) # one app needs to be uninstalled
    else:
            print(2) # both the apps need to be uninstalled 
            


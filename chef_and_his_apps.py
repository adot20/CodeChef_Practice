# Chef and his Apps
# Chef's phone has a total storage of S MB. Also, Chef has 2 apps already installed on his phone which occupy X MB and Y MB respectively.


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
            


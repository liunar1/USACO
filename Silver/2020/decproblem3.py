class Cow:
    def __init__(self, direction, x, y, cow_id):
        self.x = x
        self.y = y
        self.cow_id = cow_id
        self.direction = direction
        self.blocked_by = None # we want to know who blocked the cow (id number)
        self.blocked = 0 # number of blocked cows

num_cows = int(input())

all_cows = []
north_cows = []
east_cows = []

# initializing data for cows
for i in range(num_cows):
    cow_info = input().split()
    new_cow = Cow(cow_info[0], int(cow_info[1]), int(cow_info[2]), i)
    if new_cow.direction == 'N':
        north_cows.append(new_cow)
    else:
        east_cows.append(new_cow)
    all_cows.append(new_cow)

# sort cows from closest to farthest (i used insertion sort)
for i in range(1, len(north_cows)):
    arr_idx = i
    while arr_idx > 0 and north_cows[arr_idx].x < north_cows[arr_idx - 1].x:
        temp = north_cows[arr_idx]
        north_cows[arr_idx] = north_cows[arr_idx - 1]
        north_cows[arr_idx - 1] = temp
        arr_idx -= 1
for i in range(1, len(east_cows)):
    arr_idx = i
    while arr_idx > 0 and east_cows[arr_idx].y < east_cows[arr_idx - 1].y:
        temp = east_cows[arr_idx]
        east_cows[arr_idx] = east_cows[arr_idx - 1]
        east_cows[arr_idx - 1] = temp
        arr_idx -= 1

for i in range(len(north_cows)):
    for j in range(len(east_cows)):
        if north_cows[i].y < east_cows[j].y and north_cows[i].x > east_cows[j].x and not east_cows[j].blocked_by:
            intersection = (north_cows[i].x, east_cows[j].y)
            x_distance = intersection[0] - east_cows[j].x
            y_distance = intersection[1] - north_cows[i].y
            if x_distance > y_distance: # north cow will cut off east cow
                east_cows[j].blocked_by = north_cows[i].cow_id
                north_cows[i].blocked += 1
                north_cows[i].blocked += east_cows[j].blocked
            elif y_distance > x_distance: # east cow will cut off north cow and we do not need to consider farther away cows
                east_cows[j].blocked += 1
                east_cows[j].blocked += north_cows[i].blocked
                all_cows[east_cows[j].cow_id].blocked = east_cows[j].blocked
                break
            else: # nothing happens when both cows arrive at the same cell at the same time
                pass
    all_cows[north_cows[i].cow_id].blocked = north_cows[i].blocked

for i in range(len(all_cows)):
    print(all_cows[i].blocked)


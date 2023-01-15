# USACO 2020 Bronze Problem 3
num_cows = int(input())

cows = []
east_cows = []
north_cows = []

class Cow:
    def __init__(self, direction: str, x, y, cow_id):
        self.direction = direction
        self.x = x
        self.y = y
        self.cow_id = cow_id
        self.eaten = "Infinity" # we will use this for max eaten
        self.halted = False # if this statement is true, the cow would've intercepted another cow but it is stopped short so it won't

for i in range(num_cows):
    info = input().split()
    # 0 is direction, 1 is x coord, 2 is y coord, and i is cow id
    cow = Cow(info[0], int(info[1]), int(info[2]), i)
    if info[0] == 'E':
        east_cows.append(cow)
    else:
        north_cows.append(cow)
    cows.append(cow)

# what we do is we sort the cows so that its closest to farthest (I used insertion sort)
for i in range(1, len(north_cows)):
    index = i
    while(index > 0 and north_cows[index].x < north_cows[index - 1].x):
        temp = north_cows[index]
        north_cows[index] = north_cows[index - 1]
        north_cows[index - 1] = temp
        index -= 1
for i in range(1, len(east_cows)):
    index = i
    while(index > 0 and east_cows[index].y < east_cows[index - 1].y):
        temp = east_cows[index]
        east_cows[index] = east_cows[index - 1]
        east_cows[index - 1] = temp
        index -= 1

for i in range(len(north_cows)):
    for j in range(len(east_cows)):
        if north_cows[i].y < east_cows[j].y and north_cows[i].x > east_cows[j].x and not east_cows[j].halted:
        # if north cow higher than east cow or north cow west of east cow, the cows will never intersect
        # meet at north cow's x coordinate and east cow's y coordinate
            intersection = (north_cows[i].x, east_cows[j].y) 
            # if distance between east cow and x coordinate is larger than north cow and y coordinate, east cow will be screwed
            # and north cow has potential to keep moving and vice versa
            # if cows get there at the same time we don't care
            x_distance = intersection[0] - east_cows[j].x
            y_distance = intersection[1] - north_cows[i].y
            if x_distance > y_distance: # north screws east cow (unless north cow is screwed or east cow is long screwed already)
                east_cows[j].halted = True
                east_cows[j].eaten = x_distance
                cows[east_cows[j].cow_id].eaten = x_distance
            elif x_distance < y_distance: # north screwed by east (unless east cow already screwed)
                north_cows[i].eaten = y_distance
                cows[north_cows[i].cow_id].eaten = y_distance
                north_cows[i].halted = True
                break # no point in checking other eastern cows because the north cow is already halted
            else: # nothing happens when two cows arrive at the same cell
                pass

for i in range(len(cows)):
    print(cows[i].eaten)

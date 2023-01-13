# USACO 2020 Bronze Problem 3
num_cows = int(input())
cows = []
graze = []
amount_eaten = []

east_cows = []
north_cows = []

for i in range(num_cows):
    info = input().split()
    info[1] = int(info[1]) # x coordinate
    info[2] = int(info[2]) # y coordinate
    info.append("Infinity") # number of grass cells eaten
    info.append(i) # cow number 
    amount_eaten.append("Infinity")
    if info[0] == 'E':
        east_cows.append(info)
    else:
        north_cows.append(info)

print(east_cows)
print(north_cows)

# fix this for loop: instead of checking who arrives at the intersection first, we need to see if a cow has multiple 
# intersections, and remove the farthest intersection (since the cow will never get there)
for i in range(len(north_cows)):
    for j in range(len(east_cows)):
        # if north cow higher than east cow or north cow west of east cow, the cows will never intersect
        if north_cows[i][2] < east_cows[j][2] and north_cows[i][1] > east_cows[j][1]:
            # meet at north cow's x coordinate and east cow's y coordinate
            intersection = (north_cows[i][1], east_cows[j][2]) 
            # if distance between east cow and x coordinate is larger than north cow and y coordinate, east cow will be screwed
            # and north cow has potential to keep moving and vice versa
            # if cows get there at the same time we don't care
            x_distance = intersection[0] - east_cows[j][1]
            y_distance = intersection[1] - north_cows[i][2]
            if x_distance > y_distance:
                if east_cows[j][3] == "Infinity" or x_distance < east_cows[j][3]:
                    east_cows[j][3] = x_distance
                    amount_eaten[east_cows[j][4]] = east_cows[j][3]
            elif x_distance < y_distance:
                if north_cows[i][3] == "Infinity" or y_distance < north_cows[i][3]:
                    north_cows[i][3] = y_distance
                    amount_eaten[north_cows[i][4]] = north_cows[i][3]
            print(f"north cow starts at {(north_cows[i][1], north_cows[i][2])} and east cow starts at {(east_cows[j][1], east_cows[j][2])}")
            print(f"Intersect at {intersection} and east cow is {x_distance} from it while north cow is {y_distance} from it")
            print(" ")
                
for i in range(len(amount_eaten)):
    print(amount_eaten[i])

#########################################################################

# for i in range(num_cows):
#     info = input().split()
#     info[1] = int(info[1])
#     info[2] = int(info[2])
#     info.append(0)
#     cows.append(info)
#     graze.append(True)
#     amount_eaten.append(0)

# eaten_coords = []

# count = 0
# while any(graze) and count < 1000000000:
#     temp_eaten = []
#     for i in range(len(cows)):
#         cow_coords = (cows[i][1], cows[i][2])
#         if graze[i]:
#             if cow_coords in eaten_coords:
#                 graze[i] = False
#                 amount_eaten[i] = cows[i][3]
#             else:
#                 temp_eaten.append(cow_coords)
#                 cows[i][3] += 1
#                 if cows[i][0] == 'E': # east
#                     cows[i][1] += 1
#                 else: # north
#                     cows[i][2] += 1
#                 if cows[i][3] >= 1000000000:
#                     cows[i][3] = "Infinity"
#                     amount_eaten[i] = cows[i][3]
#     for i in range(len(temp_eaten)):
#         eaten_coords.append(temp_eaten[i])
#     count += 1

# # all we need to add is instead of a 100 limit, we check to see which 

# for i in range(num_cows):
#     print(amount_eaten[i])

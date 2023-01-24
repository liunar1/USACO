num_cows = int(input())
cow_heights = list(map(int, input().split()))
stall_heights = list(map(int, input().split()))
available_stalls = []

combos = 1

# sort cow heights from tallest to shortest 
# because we will then know that the number of different stalls each cow can go to will increase from there
for i in range(1, num_cows):
    current_idx = i
    while current_idx > 0 and cow_heights[current_idx] > cow_heights[current_idx - 1]:
        temp = cow_heights[current_idx]
        cow_heights[current_idx] = cow_heights[current_idx - 1]
        cow_heights[current_idx - 1] = temp
        current_idx -= 1

# check how many different stalls each cow can go to
for i in range(len(cow_heights)):
    available_stall = 0
    for j in range(len(stall_heights)):
        if stall_heights[j] >= cow_heights[i]:
            available_stall += 1
    available_stalls.append(available_stall)

# to find number of combinations, we see how many stalls the tallest cow can go to
# the stall is now occupied and we multiply the number of combinations by available stalls of a certain cow minus occupied stalls
# this works because we can see how many stalls a cow can go to after other taller cows have gone to their available stall
occupied_stalls = 0
for i in range(len(available_stalls)):
    combos *= available_stalls[i] - occupied_stalls
    occupied_stalls += 1

print(combos)

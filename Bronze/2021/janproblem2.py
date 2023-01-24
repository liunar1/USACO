num_cows = int(input())
cow_ids = list(map(int, input().split()))

odd_id_ct = 0
even_id_ct = 0

for i in range(len(cow_ids)): 
    # this will help us because we don't actually care about what the numbers are
    # only whether they are odd or even
    if cow_ids[i] % 2 == 0:
        even_id_ct += 1
    else:
        odd_id_ct += 1

max_groups = 0
even_group = True
while odd_id_ct or even_id_ct:
    if even_group: # check which group we have to form
        if even_id_ct:
            even_id_ct -= 1
            max_groups += 1
        elif odd_id_ct > 1:
            odd_id_ct -= 2
            max_groups += 1
        elif odd_id_ct == 1:
            max_groups -= 1 
            # we subtract a group because if we have an even number of odd numbers and only odd numbers, 
            # the last odd number will have to merge with another odd number to keep the first number even
            odd_id_ct -= 1
    else:
        if odd_id_ct:
            odd_id_ct -= 1
            max_groups += 1
        else:
            break # no more odd numbers, so add all remaining even numbers to an odd number and we're done
    even_group = not even_group
print(max_groups)
    

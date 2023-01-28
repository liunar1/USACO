class Cow:
    def __init__(self, name, zodiac, other_cow, direction):
        self.name = name
        self.zodiac = zodiac
        self.other_cow = other_cow
        self.direction = direction
        # self.years_apart = 0

cows = {
    "Bessie": Cow("Bessie", "Ox", None, None)
}

num_cows = int(input())

for i in range(num_cows):
    row = input().split()
    cow = Cow(row[0], row[4], row[-1], row[3])
    cows[cow.name] = cow

elsie_apart = 0

zodiac_calendar = {
    "Ox": 0,
    "Tiger": 1,
    "Rabbit": 2,
    "Dragon": 3,
    "Snake": 4,
    "Horse": 5,
    "Goat": 6,
    "Monkey": 7,
    "Rooster": 8,
    "Dog": 9,
    "Pig": 10,
    "Rat": 11 
}

# we use recursion and a dictionary to map one cow to another, eventually leading a chain from Elsie to Bessie
# we then see how far they are apart with the cows in between, and print the absolute difference between Elsie and Bessie

def apart(current_cow: Cow, other_cow: Cow,  years_apart):
    # print(current_cow.name, other_cow.name, " ")
    if other_cow.name != "Bessie":
        years_apart += apart(other_cow, cows[other_cow.other_cow], years_apart)
    # print(current_cow.name, other_cow.name, " ")
    if current_cow.direction == "previous":
        if zodiac_calendar[current_cow.zodiac] > zodiac_calendar[other_cow.zodiac]:
            years_apart += zodiac_calendar[other_cow.zodiac] + 12 - zodiac_calendar[current_cow.zodiac]
        elif zodiac_calendar[current_cow.zodiac] == zodiac_calendar[other_cow.zodiac]:
            years_apart += 12
        else:
            years_apart += zodiac_calendar[other_cow.zodiac] - zodiac_calendar[current_cow.zodiac] 
    else:
        if zodiac_calendar[current_cow.zodiac] > zodiac_calendar[other_cow.zodiac]:
            years_apart += zodiac_calendar[other_cow.zodiac] - zodiac_calendar[current_cow.zodiac]
        elif zodiac_calendar[current_cow.zodiac] == zodiac_calendar[other_cow.zodiac]:
            years_apart -= 12
        else:
            years_apart += zodiac_calendar[other_cow.zodiac] - (12 + zodiac_calendar[current_cow.zodiac])
    return years_apart

elsie_apart = abs(apart(cows["Elsie"], cows[cows["Elsie"].other_cow], elsie_apart))

print(elsie_apart)

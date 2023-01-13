# USACO 2020 Bronze Problem 2
from collections import Counter

flowers = input()
petals = list(map(int, input().split()))
avg = len(petals)

for i in range(0, len(petals) - 1):
    total = petals[i]
    for j in range(i + 1, len(petals)):
        total += petals[j]
        if total / (j - i + 1) in petals[i:j+1]:
            avg += 1
print(int(avg))









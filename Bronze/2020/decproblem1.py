# USACO 2020 Bronze Problem 1
numbers = list(map(int, input().split()))

A = min(numbers) # a
largest = max(numbers) # a + b + c

B_C = largest - A # b + c

# the only numbers remaining are B, C, A + B, A + C

for i in range(len(numbers)):
    B = numbers[i]
    C = B_C - B
    if C in numbers:
        if C < B:
            temp = B
            B = C
            C = temp
        break

print(A, B, C)

            









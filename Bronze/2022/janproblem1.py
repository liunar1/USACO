answer = []
guess = []

# i create dictionaries to see how many times each letter occurs
answer_letters = {}
guess_letters = {}

for i in range(6): # create the answer and guessing grids
    row = input()
    if i < 3:
        for j in range(3):
            if row[j] not in answer_letters:
                answer_letters[row[j]] = 1
            else:
                answer_letters[row[j]] += 1
        answer.append(list(row))
    else:
        for j in range(3):
            if row[j] not in guess_letters:
                guess_letters[row[j]] = 1
            else:
                guess_letters[row[j]] += 1
        guess.append(list(row))

correct = 0
wrong_place = 0

for i in range(3):
    for j in range(3):
        if answer[i][j] == guess[i][j]:
            answer_letters[answer[i][j]] -= 1
            guess_letters[answer[i][j]] -= 1 
            correct += 1

# by now we know that no other letter matches up exactly to be correct, so we look for warnings and see if there are any similar letters
# that are in the guesses that are also in the answers even though they are in the wrong spot
for key in guess_letters:
    if key in answer_letters:
        wrong_place += min(answer_letters[key], guess_letters[key])

print(correct)
print(wrong_place)

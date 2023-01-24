alphabet_letters = input()
heard_letters = input()

alphabet = {}

for letter in range(len(alphabet_letters)): # create a dictionary for better time complexity to map a letter to its order in alphabet
    alphabet[alphabet_letters[letter]] = letter

times_sung = 1 # since minimum length of string is 1, the cow must have sang the alphabet at least once
letter = -1

for i in range(len(heard_letters)):
    current_letter = alphabet[heard_letters[i]]
    if current_letter <= letter: 
        # if the next letter that john heard is alphabetically before the previous letter that he heard
        # the cow must've started the alphabet again
        times_sung += 1
    letter = current_letter

print(times_sung)



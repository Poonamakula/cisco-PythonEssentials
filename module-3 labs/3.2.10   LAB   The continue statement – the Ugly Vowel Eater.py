word = input()# Prompt the user to enter a word
user_word = word.upper()# and assign it to the user_word variable.

for letter in user_word:
    if letter == 'A' or letter =='E' or letter == 'I' or letter == 'O' or letter == 'U' :# Complete the body of the for loop.
        continue
    else :
        print(letter)
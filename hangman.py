import random

word_bank = []
def load_words():
    with open("words.txt") as file:
        for word in file:
            word_bank.append(word)

load_words()
word = random.choice(word_bank)

word_spaces = []

for num in range(len(word)):
    word_spaces.append("_")
    

def show_progress(word_spaces):
    output = ""    
    for i in range(len(word_spaces)):
        output += word_spaces[i]
        if i != len(word_spaces) - 1:
            output += " "
    return output

lives = 5

def check_word(guess):
    letter_count = 0
    for i in range(len(word)):
        if word[i] == guess:
            word_spaces[i] = guess
            letter_count += 1
    return letter_count

running = True

# weird issue where it doesn't think we're passing in anythingggggg
while running:
    output = show_progress(word_spaces)
    print(f"{output}\n")
    guess = input("Enter a single letter guess: ").lower()
    while not guess.isalpha() or len(guess) != 1:
        guess = input("Please enter a valid guess: ")
    count = check_word(guess)
    if count == 0:
        lives -=1
        print(f"Your guess was not in the word, you have {lives} lives left\n")


 

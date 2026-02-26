import random

word_bank = []
def load_words():
    with open("words.txt") as file:
        for word in file:
            word_bank.append(word)

load_words()
word = random.choice(word_bank)

word_spaces = []
for num in range(len(word)-1):
    word_spaces.append("_")
    
output = ""
for i in range(len(word_spaces)):
    output += word_spaces[i]
    if i != len(word_spaces)-1:
        output += " "
    
print(output)

import random

words = ["python", "apple", "house", "world", "train"]
word = random.choice(words)

display = ["_"] * len(word)
wrong = 0

print("Welcome to Hangman!")

while wrong < 6 and "_" in display:
    print("Word:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong += 1
        print("Wrong guess! Remaining chances:", 6 - wrong)

if "_" not in display:
    print("You win! The word was:", word)
else:
    print("You lose! The word was:", word)

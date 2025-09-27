#Word guessing Game

print("Welcome to the word guessing game!")


secret_word = "moses"
guess = None
guesses_count = 0

# Create the first hint (underscores)
hint = ""
for each in range(len(secret_word)):
    hint = hint + "_  "
print(f"Your hint is: {hint}")

while guess != secret_word:
    guess = input("what is your guess? ").lower()
    guesses_count += 1
    # 1. Check if guess has the wrong length
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
     # 2. Check if guess is correct
    elif guess == secret_word:
        print("Congratulations! You guessed it!")
     # 3. Otherwise, guess is wrong but right length
    else:
        print("Your guess was not correct.")
        #New hint
        hint = ""
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                hint = hint + guess[i].upper() + " "
            elif guess[i] in secret_word:
                hint = hint + guess[i].lower() + " "
            else:
                hint = hint +  "_"
        print(f"Hint: {hint}")
print(f"It took you {guesses_count} guesses")
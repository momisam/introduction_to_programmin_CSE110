#Guess My Number Game 
import random


play_again = 'yes'

while play_again.lower() == 'yes':
    secret_number = random.randint(1, 100)
    count = 0
    guess = None
    
    while guess != secret_number:
        guess = int(input("what is your guess? "))
        
        if guess < secret_number:
            print("Higher")
        elif guess > secret_number:
            print("Lower")
        else:
            print("You guessed it!")
        count += 1
    print(f"It took you {count} guesses")
    play_again = input("Would you like to play again (yes/no)? ")
print("Thank you for playing. Goodbye.")

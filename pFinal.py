import random

def quest():
    while True:
        guessb = input("Enter an integer from 1 to 200: ")

        if guessb == "":
            print("Input cannot be blank enter a valid number.")
            continue
        
        try:
            guess = int(guessb)
        except ValueError:
            print('Value must be an integer, try again.')
            continue
        
        if guess < 1 or guess > 200:
            print('Value must be between 1 and 200, try again.')
            continue
        
        return guess
def chann():
    while True:
        chancesi = input("Enter number of chances (1-100), default is 15: ")
        
        if chancesi == '':
            chances = 15
            break
        elif chancesi.isdigit():
            chances = int(chancesi)
            if 1 <= chances <= 100:
                break
            else:
                print("Chances must be between 1 and 100, try again.")
        else:
            print("Input must be a valid integer, try again.")
    
    return chances

def main():
    
        
        print("\n" * 20)

        namep = input("Name of the Player--> ")
        n = random.randint(1, 200)

        chances=chann()

        guesses_made = 0
        invalid_guesses = 0
        guess = None

        while guesses_made < chances:
            guesses_left = chances - guesses_made  
            guess = quest()
            guesses_made += 1

            print(f"Guesses left: {guesses_left}")
            
            if guess < n:
                print("Guess is low. You have",guesses_made,"guesses made" )
            elif guess > n:
                print("Guess is high. You have",guesses_made,"guesses made")
            else:
                print(f"Congratulations" ,namep,"! You guessed it right!")
                break
        else:
            print(f"Sorry",namep," you've run out of chances.")

        print(f"Total guesses made: {guesses_made}")
        print(f"Invalid guesses: {invalid_guesses}")

        mm = input('Do you wanna start a new game? Y/N --> ').lower()
        if mm != 'y':
            print(f'Thanks for playing today, {namep}!')
            

main()

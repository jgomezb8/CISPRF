import random

 

games = {

    1: {"name": "Powerball", "max_number": 69, "count": 5},

    2: {"name": "Mega Million", "max_number": 70, "count": 5},

    3: {"name": "Lucky Day Lotto", "max_number": 45, "count": 5},

    4: {"name": "Lotto", "max_number": 52, "count": 6}

}

 



def generate_numbers(max_number, count):

    numbers = random.sample(range(1, max_number + 1), count)

    return sorted(numbers)

 


def display_menu():

    print("\nIllinois Lottery Games:")

    print("1. Powerball")

    print("2. Mega Million")

    print("3. Lucky Day Lotto")

    print("4. Lotto")

    print("9. Quit")

 


def main():
    display_menu()


    ans= 0
    while ans == 0:

        try:

            choice = int(input("Choose a lottery game (1-4) or 9 to quit: "))

            if choice == 9:

                print("Exiting the program.")

                break

            elif choice in games:

                game = games[choice]

                numbers = generate_numbers(game["max_number"], game["count"])

                print(f"{game['name']}: {', '.join(map(str, numbers))}")

            else:

                print("Invalid selection. Please choose a number between 1 and 4, or 9 to quit.")

        except ValueError:

            print("Please enter a valid number.")

       

       

        if input("\nWould you like to run another lottery? (y/n): ").strip().lower() != 'y':

            break

 

main()

# Dawei Sun - Lab 8 (Final Project)

def fahrenheit_to_celsius():
    f = int(input("Enter the temperature in Fahrenheit: "))
    c = (f - 32) * (5 / 9)
    print("The temperature in Celsius is:", c)

name = input("Please enter your name: ")

while True:
    print("\nMenu")
    print("1. Show a joke")
    print("2. Print your name 15 times")
    print("3. Print a quote many times")
    print("4. Guessing game")
    print("5. Fahrenheit to Celsius")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        print("Why don't programmers like nature?")
        print("Because it has too many bugs!")

    elif choice == 2:
        for i in range(15):
            print(name)

    elif choice == 3:
        number = int(input("Enter a number: "))
        for i in range(number):
            print("The future belongs to those who believe in their dreams.")

    elif choice == 4:
        secret = 42
        guess = int(input("Guess a number between 0 and 100: "))

        while guess != secret:
            if guess < 0 or guess > 100:
                print("Please enter a number within the range 0 to 100.")
            elif guess < secret:
                print("Too low!")
            else:
                print("Too high!")

            guess = int(input("Guess again: "))

        print("You won! Great job!")

    elif choice == 5:
        fahrenheit_to_celsius()

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

print("Menu")
print("1. Name joke")
print("2. Print food 20 times")
print("3. Number until 0")

choice = int(input("Choose an option (1-3): "))

# Option 1
if choice == 1:
    name = input("Enter your name: ")
    print(name, "walked into an ancient Chinese temple.")
    print("The wise monk said:", name + ", wisdom comes with patience.")

# Option 2
elif choice == 2:
    food = input("Enter the name of a Chinese food: ")
    for i in range(20):
        print(food)

# Option 3
elif choice == 3:
    number = int(input("Enter a number (0 to stop): "))

    while number != 0:
        print("Warning: This is not the lucky number 0.")
        number = int(input("Enter a number (0 to stop): "))

    print("You entered 0. Balance and harmony achieved.")

else:
    print("Invalid choice.")

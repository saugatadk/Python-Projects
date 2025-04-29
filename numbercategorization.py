# Input: Ask the user to enter an integer

number = int(input("Enter an integer: "))


# Check if the number is positive and even

if number > 0 and number % 2 == 0:

    print("Positive and even")


# Check if the number is positive and odd

elif number > 0 and number % 2 != 0:

    print("Positive and odd")


# Check if the number is negative and even

elif number < 0 and number % 2 == 0:

    print("Negative and even")


# Check if the number is negative and odd

elif number < 0 and number % 2 != 0:

    print("Negative and odd")


# If the number is zero

else:

    print("The number is zero")
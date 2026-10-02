# This is handling invalid input safely

def get_number():
    while True:
        text = input("Enter a whole number: ")

        try:
            number = int(text)

            if number >= 0:
                return number
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("That is not a number. Please try again.")


number = get_number()
print("You entered:", number)
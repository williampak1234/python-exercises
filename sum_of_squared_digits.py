# Problem: Add the sum of the square of the digits of a number
# Difficulty: Medium
# Notes: Had a lot of trouble with this one. Learned a lot about the rules for indexing with strings and integers

def get_num():
    """Retrieves the number from the user"""
    return int(input("Please enter the number: "))

def sum_of_dig_squared(the_number):
    """loops through the digits(as a string) in the number, then adds them to "total" after converting the digit into
     an integer and squaring it. then returns total."""
    total = 0

    for digit in str(the_number):
        total += int(digit) ** 2

    return total

def main():
    """Gets the number from user, returns the sum of the square of the digits"""
    number_to_be_squared = get_num()
    print(sum_of_dig_squared(number_to_be_squared))

if __name__ == "__main__":
    main()
# Print numbers from 1 to 100 inclusively following these instructions:

# if a number is multiple of 3, print "Fizz" instead of this number
# if a number is multiple of 5, print "Buzz" instead of this number
# for numbers that are multiples of both 3 and 5, print "FizzBuzz"
# print the rest of the numbers unchanged.
# Difficulty:
# Notes:

def main():
    """Prints all numbers from 1-100 following the instructions above."""

    for numbers in range(1,101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz")
        elif numbers % 3 == 0:
            print("Fizz")
            continue
        elif numbers % 5 == 0:
            print("Buzz")
        else:
            print(numbers)

if __name__ == "__main__":
    main()
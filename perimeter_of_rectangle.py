# Problem: Find the perimeter of a rectangle
# Difficulty: Easy
# Notes: Utilized while loops to counteract invalid inputs, combined functions to make main function cleaner,
#        learned how to return multiple values from a function

def get_length_from_user():
    """Gets the length of rectangle from user"""
    return int(input("Please enter the length of the rectangle: "))

def get_width_from_user():
    """Gets the width of rectangle from user"""
    return int(input("Please enter the width of the rectangle: "))

def get_dimensions_of_rectangle_from_user():
    """Gets dimensions of rectangle from user, and keeps asking in the case user gives invalid input"""
    while True:
        length = get_length_from_user()
        if length >= 1:
            break
        print("Length must be greater than 0")

    while True:
        width = get_width_from_user()
        if width >= 1:
            break
        print("Width must be greater than 0")

    return length, width

def perimeter_of_rectangle(side1, side2):
    """Returns the perimeter of the rectangle based on the length and width provided by user"""
    return (side1 + side2) * 2

def main():
    """Gets rectangle dimensions from user and prints the perimeter"""
    length, width = get_dimensions_of_rectangle_from_user()
    print(perimeter_of_rectangle(length, width))

if __name__ == "__main__":
    main()
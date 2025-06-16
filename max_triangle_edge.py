# Create a function that finds the maximum range of a triangle's third edge,
# where the side lengths are all integers.

def max_size(side1_len, side2_len):
    max_range_of_third_size = (side1_len + side2_len) - 1
    return max_range_of_third_size

def main():
    side1 = int(input("Enter the size of the first side: "))
    side2 = int(input("Enter the size of the second side: "))

    print(max_size(side1, side2))

if __name__ == "__main__":      # implementing proper code formatting from the start to build good habits
    main()
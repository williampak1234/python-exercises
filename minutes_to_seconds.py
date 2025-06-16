# Problem: Convert minutes into seconds
# Difficulty: Easy
# Notes:

def min_to_sec(minutes):
    """returns the value of minutes into seconds"""
    return minutes * 60


def main():
    time_in_min = int(input("Please enter the number of minutes: "))
    print(f"{time_in_min} minutes is equal to {min_to_sec(time_in_min)} seconds.")


if __name__ == "__main__":
    main()

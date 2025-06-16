# Problem: Takes a single integer and performs multiple operations
# Difficulty: Easy
# Notes: Decided to not create so many functions with user inputs and complicate it,
#        just sticking to the logic as it would be asked in an interview

def main():
    n = int(input())
    reusable_n = n

    #using comments for clarity
    n = n + n              # n = 8 + 8 = 16
    n = n * reusable_n     # n = 16 * 8 = 128
    n = n - reusable_n     # n = 128 - 8 = 120
    n = n // reusable_n    # n = 120 // 8 = 15

    print(n)

if __name__ == "__main__":
    main()
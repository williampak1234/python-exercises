# Problem: Write a function that stutters a word as if someone is struggling to read it.
#          The first two letters are repeated twice with an ellipsis ... and space after each,
#          and then the word is pronounced with a question mark ?

# Source: Edabit
# Difficulty: Easy
# Notes: Utilizing print(f""), utilizing pep257 in order to meet industry standards

def stutter(word):
    """Returns a stuttering phrase of the inputted word"""
    return f"{word[:2]}... {word[:2]}... {word}?"


def main():
    stutter_word = input("Please enter the word: ")
    print(stutter(stutter_word))


if __name__ == "__main__":
    main()

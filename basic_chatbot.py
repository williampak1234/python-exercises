def greet(bot_name, birth_year):
    """Bot greets the user, and states it's time of conception."""
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    """Bot receives data from the user, creates a custom response."""
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    """Uses a mathematical function to guess the age of the user based on the remainders of their age divided by 3,5,and 7"""
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    """Gets a user input for a number and counts up to that number."""
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    """Tests the user on a mini quiz and repeats it until they get the question correct."""
    print("Let's test your programming knowledge.")
    the_answer_is_wrong = True

    while the_answer_is_wrong:
        print("Which language is the best for data science?:")
        print("1. Python")
        print("2. C++")
        print("3. Ruby")
        print("4. HTML")

        answer = int(input())

        if answer == 1:
            the_answer_is_wrong = False
        else:
            continue

    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()

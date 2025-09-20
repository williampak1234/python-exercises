# Lab Exercise 1
# Task: Take two variables and swap their values using a third variable. Print the values before and after swapping.
def swap_two_numbers():
    num1 = int(input("Enter the first variable: "))
    num2 = int(input("Enter the second variable: "))

    temp = 0

    temp = num1
    num1 = num2
    num2 = temp




# Lab Exercise 2
# Ask the user for their gross monthly salary (can be float).
# Calculate the following: 20% goes to tax 30% goes to rent 10% goes to savings
# Print how much money is left for spending.
def money_left():
    monthly_salary = int(input("Enter your monthly salary: "))
    tax = monthly_salary * 0.2
    rent = monthly_salary * 0.3
    saving = monthly_salary * 0.1
    spending = monthly_salary - tax - rent - saving

    print(spending)




# Lab Exercise 3
# Task: Ask the user for a 3-digit number and print the sum of its digits.
def sum_digits():
    three_digit_num = int(input("Please enter a 3 digit number: "))
    length_of_int = len(str(three_digit_num))

    if length_of_int < 3 or length_of_int > 3:
        three_digit_num = int(input("Please enter a 3 digit number, not any more, or any less: "))

    else:
        hundred_digit = three_digit_num // 100
        tens_digit = three_digit_num // 10 % 10
        ones_digit = three_digit_num % 10

        print(f"Sum of digits is {hundred_digit + tens_digit + ones_digit}")




# Lab Exercise 4
# Task: Ask the user for a 3-digit number. Print the reverse of the number.
def reverse_digits():
    three_digit_num = int(input("Please enter a 3 digit number: "))
    length_of_int = len(str(three_digit_num))

    if length_of_int < 3 or length_of_int > 3:
        three_digit_num = int(input("Please enter a 3 digit number, not any more, or any less: "))

    else:
        hundred_digit = three_digit_num // 100
        tens_digit = three_digit_num // 10 % 1
        ones_digit = three_digit_num % 10

        reversed_num = (ones_digit * 100) + (tens_digit * 10) + (hundred_digit)
        print(reversed_num)



# Lab Exercise 5
# Task: Ask the user for a number and tell whether it's even or odd, but don’t use the modulo (%) operator.
def even_or_odd_no_module():
    num = int(input())

    if num // 2 * 2 == num:
        print("Is even")

    else:
        print("Is odd")




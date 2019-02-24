first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
third_number = int(input("Enter third number:"))

if first_number > second_number:
    if first_number > third_number and second_number > third_number:
        print(first_number + third_number)
    elif first_number > third_number and second_number < third_number:
        print(first_number + second_number)
    elif first_number < third_number:
        print(third_number + second_number)
elif second_number > first_number:
    if second_number > third_number and first_number > third_number:
        print(second_number + third_number)
    elif second_number > third_number and first_number < third_number:
        print(second_number + first_number)
    elif second_number < third_number:
        print(third_number + first_number)

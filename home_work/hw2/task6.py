first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
third_number = int(input("Enter third number:"))

if first_number >= second_number >= third_number:
    first_number *= 2
    second_number *= 2
    third_number *= 2
    print(first_number, second_number, third_number)
else:
    test_number = first_number
    first_number = second_number
    second_number = test_number
    print(first_number, second_number)

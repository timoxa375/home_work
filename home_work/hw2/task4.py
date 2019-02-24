first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
third_number = int(input("Enter third number:"))
nums = [first_number, second_number, third_number]

if first_number % 2 == 0 or second_number % 2 == 0 or third_number % 2 == 0:
    print(max(nums))
else:
    print(min(nums))



"""
if first_number % 2 == 0 or second_number % 2 == 0 or third_number % 2 == 0:
    if first_number > second_number:
        if first_number > third_number:
            print("MAX is ", first_number)
        elif first_number < third_number:
            print("MAX is ", third_number)
    elif second_number > first_number:
        if second_number > third_number:
            print("MAX is ", second_number)
        elif second_number < third_number:
            print("MAX is ", third_number)
else:
    if first_number > second_number:
        if first_number > third_number and second_number > third_number:
            print("MIN is ", third_number)
        elif first_number > third_number and second_number < third_number:
            print("MIN is ", second_number)
        elif first_number < third_number:
            print("MIN is ", second_number)
    elif second_number > first_number:
        if second_number > third_number and first_number > third_number:
            print("MIN is ", third_number)
        elif second_number > third_number and first_number < third_number:
            print("MIN is ", first_number)
        elif second_number < third_number:
            print("MIN is ", first_number)
"""
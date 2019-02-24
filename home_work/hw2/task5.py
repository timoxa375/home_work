first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
polusum = (first_number + second_number) / 2
udv_proizv = (first_number * second_number) * 2
if first_number > second_number:
    second_number = polusum
    first_number = udv_proizv
    print("MIN number is:", second_number, ", MAX number is:", first_number)
else:
    first_number = polusum
    second_number = udv_proizv
    print("MIN number is:", first_number, ", MAX number is:", second_number)

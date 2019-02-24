first_operand = int(input("Enter first operand:"))
second_operand = int(input("Enter second operand:"))
operator = input("Enter operator(+,-,*,/):")
if operator == '+' or '-' or '*' or '/':
    if operator == '+':
        print("Result:", first_operand + second_operand)
    elif operator == '-':
        print("Result:", first_operand - second_operand)
    elif operator == '*':
        print("Result:", first_operand * second_operand)
    elif operator == '/':
        print("Result:", first_operand / second_operand)
    else:
        print("Result:NaN")

#a*p4+d*p2+c=0

a = int(input('Введите "a"'))
d = int(input('Введите "d"'))
c = int(input('Введите "c"'))
x = int(input('Введите "x"'))
y = int(input('Введите "y"'))

if (a * x**4 + d * x**2 + c) == 0 and (a * y**4 + d * y**2 + c) == 0:
    print("Являются конрями")
else:
    print("Не являются конрями")

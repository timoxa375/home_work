matr = [[5,2,9,],[3,5,6,]]
total_sum = 0
num = 0
for i in matr:
    for j in i:
        total_sum += j
        num += 1
print("Среднее арифметическое равно: ", int(total_sum / num))
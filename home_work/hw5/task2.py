matr = [
[5,2,9,1],
[3,5,6,2],
[8,1,7,4]]
min_num = int(input("enter min_num: "))
max_num = int(input("enter max_num: "))
num = 0

for i in matr:
    for j in i:
        if min_num <= j <= max_num:
            num += 1
print("Количество элементов равно: ", num)
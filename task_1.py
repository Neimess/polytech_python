numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

# Вычисляем сумму элементов списка, исключая None
total = sum(x for x in numbers if x is not None)

# Заменяем все None на вычисленную сумму
my_list = [x if x is not None else total/(len(numbers)) for x in numbers]
print("Измененный список:", my_list)
list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

maximum = list_numbers.index(max(list_numbers)) # находим индекс максимального элемента
list_numbers[maximum], list_numbers[-1] = list_numbers[-1], list_numbers[maximum] # меняем местами максимальный и минимальный элементы списка
print(list_numbers) # выводим на печать получившийся список
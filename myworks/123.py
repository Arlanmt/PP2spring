
numbers = input("Введите числа через пробел: ")
numbers_list = [int(num) for num in numbers.split()]
maximum = max(numbers_list)
print(f"Максимум: {maximum}")

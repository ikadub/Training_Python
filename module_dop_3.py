def calculate_structure_sum(data): # Принимает на вход структуру данных любого уровня вложенности.
    total_sum = 0 # общая сумма

    def process_item(item):
        nonlocal total_sum

        if isinstance(item, int): # элемент является целым числом (int), добавляем к общей сумме.
            total_sum += item
        elif isinstance(item, str): # элемент является строкой (str), добавляем длину к общей сумме.
            total_sum += len(item)
        elif isinstance(item, dict): # элемент является словарем (dict), рекурсивно обрабатываем ключи и значения.
            for key in item:
                process_item(key)
                process_item(item[key])
        elif isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
        # элемент является списком, кортежем или множеством (list, tuple, set), рекурсия
            for subitem in item:
                process_item(subitem)

    process_item(data)

    return total_sum


# Входные данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вызываем функцию и выводим результат
result = calculate_structure_sum(data_structure)
print("Cумма всех чисел и длин всех строк:", result)  # Ожидаемый результат: 99
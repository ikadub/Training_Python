calls = 0

def count_calls(): # Увеличивает счётчик вызовов
    global calls
    calls += 1

def string_info(string): # Возвращает кортеж из длины строки, строки в верхнем и нижнем регистрах
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search): # Проверяет наличие строки в списке без учёта регистра
    count_calls()
    string_lower = string.lower()
    return any(s.lower() == string_lower for s in list_to_search)

# Примеры вызова функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls) # Вывод количества вызовов функций
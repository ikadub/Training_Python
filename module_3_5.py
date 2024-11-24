def get_multiplied_digits(number):
    # Преобразуем число в строку для удобства работы с отдельными цифрами
    str_number = str(number)
    # print(str_number) # для понимания процесса, потом можно убрать

    # Если длина строки равна 1, возвращаем саму цифру
    if len(str_number) <= 1:
        # вводим новую переменную, чтобы заменить возможный  последний 0 на 1
        # если этого не сделать, то при последнем 0 произведение будет 0
        str_number_1 = int(str_number)
        if str_number_1 == 0:
            str_number = 1
        return int(str_number)


    # Берем первую цифру и преобразуем её в число
    first = int(str_number[0])
    print(first)

    # Рекурсивный вызов функции для оставшихся цифр
    return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(402030))
print(get_multiplied_digits(4020300))



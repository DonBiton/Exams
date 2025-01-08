def check_data_type(user_input):
 # Попробуем преобразовать ввод в целое число
    try:
        # Если можно преобразовать в int, это целое число
        int_value = int(user_input)
        return "Целое число"
    except ValueError:
        pass
    
    try:
        float_value = float(user_input)
        return "Число с плавающей точкой"
    except ValueError:
        pass
    return "Строка или другой тип данных"


user_input = input("Введите данные: ")
result = check_data_type(user_input)
print(f"Тип данных: {result}")















# x = 10
# print(type(x))  # <class 'int'>

# y = "Hello"
# print(isinstance(y, str))  # True

# z = [1, 2, 3]
# print(type(z))  # <class 'list'>
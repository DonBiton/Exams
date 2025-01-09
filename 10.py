def outer_function():
    x = 10  # переменная внешней функции

    def inner_function():
        print("Это вложенная функция.")
        print("Она может доступить переменные внешней функции:", x)

    inner_function()  # вызов вложенной функции

outer_function()



def outer_function(outer_var):
    def inner_function(inner_var):
        return outer_var + inner_var
    return inner_function

# Создаем замыкание
closure = outer_function(10)
print(closure)
print(closure(5))  # 15
# outer_function возвращает inner_function.
# inner_function использует переменную outer_var из внешней функции.
# Даже после завершения работы outer_function, inner_function сохраняет доступ к outer_var, образуя замыкание.

def power_of(n):
    def exponent(base):
        return base ** n
    return exponent

square = power_of(2)  # замыкание для возведения в квадрат
cube = power_of(3)  # замыкание для возведения в куб

print(square(5))  # 25
print(cube(3))  # 27
print('')
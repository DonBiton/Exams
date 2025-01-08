dictionary = {"name": "Alice", "age": 25}
dictionary["city"] = "New York"  # добавляем новый ключ и значение
print(dictionary)

del dictionary["city"]  # удаление по ключу
age = dictionary.pop("age")  # удаляет и возвращает значение
print(dictionary)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)  # объединение
# dict1 = {"a": 1, "b": 3, "c": 4}
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
common_keys = dict1.keys() & dict2.keys()  # пересечение ключей
print(common_keys)  # {'b'}

my_set = {1, 2, 3}
my_set.add(4)  # добавление элемента
my_set.remove(3)  # удаляет элемент, если его нет — вызывает ошибку
my_set.discard(2)  # удаляет элемент, но не вызывает ошибку, если его неt
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # объединение
print(union_set)  # {1, 2, 3, 4, 5}
intersection_set = set1 & set2  # пересечение
print(intersection_set)  # {3}

def factorial(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))
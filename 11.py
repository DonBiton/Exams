# Пример использования списка
tasks = ['Задача 1', 'Задача 2', 'Задача 3']
tasks.append('Задача 4')  # Добавить в конец
print(tasks[2])  # Вывести 3-ю задачу

from collections import deque
queue = deque([1, 2, 3])
queue.append(4)  # Добавить элемент в конец
queue.popleft()  # Удалить элемент с начала
print(queue) #[2, 3, 4]

deque_obj = deque([1, 2, 3])
deque_obj.appendleft(0)  # Добавить элемент в начало
deque_obj.append(4)      # Добавить элемент в конец
print(deque_obj) #[0, 1, 2, 3, 4]

stack = [1, 2, 3]
stack.append(4)  # Добавить элемент в конец (push)
stack.pop()  # Удалить элемент с конца (pop)
print(stack) # [1, 2, 3]

class Stack:
    def __init__(self):
        # Стек реализуем как обычный список
        self.stack = []

    def push(self, item):
        """Добавление элемента в стек"""
        self.stack.append(item)
        print(f"Элемент {item} добавлен в стек.")

    def pop(self):
        """Удаление элемента из стека (если стек не пустой)"""
        if not self.is_empty():
            removed_item = self.stack.pop()
            print(f"Элемент {removed_item} удалён из стека.")
            return removed_item
        else:
            print("Стек пуст!")
            return None

    def peek(self):
        """Возвращает верхний элемент стека без удаления"""
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Стек пуст!")
            return None

    def is_empty(self):
        """Проверка, пуст ли стек"""
        return len(self.stack) == 0

# Тестируем стек
stack = Stack()

# Добавляем три элемента в стек
stack.push(1)
stack.push(2)
stack.push(3)

# Посмотрим на верхний элемент стека
print(f"Верхний элемент стека: {stack.peek()}")

# Удалим один элемент
stack.pop()

# Посмотрим на новый верхний элемент
print(f"Верхний элемент стека после удаления: {stack.peek()}")

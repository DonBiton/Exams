#Пузырьковая сортировка (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Меняем местами
    return arr

mas = [5, 2, 9, 1, 5, 6]
print(bubble_sort(mas))
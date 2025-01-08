import random, time
def find_max_manual(arr):
    max_val = arr[0]
    for i in arr:
        if i > max_val:
            max_val = i
    return max_val
arr = []
for i in range(1_000_000):
    arr.append(random.randint(-100_000, 100_000))
time_max_1 = time.time()
max1 = max(arr)
time_max_2 = time.time()
print(max1,time_max_2-time_max_1)

time_max_1 = time.time()
max2 = find_max_manual(arr)
time_max_2 = time.time()
print(max2,time_max_2-time_max_1)









# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# mas = [1, 2, 5, 10 ,40 ,60, 80,90, 110, 150]
# print(binary_search(mas, 4))
def find_smallest(arr):
    """找出最小数"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def select_sort(arr):
    """选择排序:
            选择最小的放入新数组中,得到一个完整有序的数组
    """
    new_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


arr = [8, 10, 2, 3, 4, 8, 9, 1, 22]
new_arr = select_sort(arr)
print(new_arr)

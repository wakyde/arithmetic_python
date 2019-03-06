def binary_search(num_list, item):
    low = 0
    high = len(num_list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        print(mid)
        if item == num_list[mid]:
            return mid
        elif item < num_list[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None


num_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
find_seek = binary_search(num_list, 1)
if find_seek == None:
    print("该列表中没有该数字!")
else:
    print("找到了该数字,它在第%d个" % find_seek)

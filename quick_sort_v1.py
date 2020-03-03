def quick_sort(array, left, right):
    if left < right:  # left right 为索引
        location = partition(array, left, right)
        quick_sort(array, left, location - 1)
        quick_sort(array, location + 1, right)


def partition(array, left, right):
    target = array[right]
    i = left - 1  # i代表目标值左侧(比target小的值)部分的末尾的索引
    for j in range(left, right):  # j代表目标值右侧（比target值大的部分末尾的索引）
        if array[j] < target:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1  # 返回分界值的位置
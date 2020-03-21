def binary_search(nums, value):
    l, r = 0, len(nums) - 1
    while(l <= r):
        m = (l + r) // 2
        if nums[m] == value:
            return m
        elif nums[m] > value:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == '__main__':
    input = [1, 3, 3.5, 4, 4.5, 5]
    res = binary_search(input, 6)
    print(res)

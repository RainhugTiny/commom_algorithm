def quick_sort(nums, left, right):
    if not nums:
        return
    stack = []
    stack.append([left, right])
    while stack:
        i, j = stack.pop()
        position = partition(nums, i, j)
        if position - 1 > i:
            stack.append([i, position - 1])
        if position + 1 < j:
            stack.append([position + 1, j])


def partition(nums, left, right):
    target = nums[right]
    i = left - 1
    for j in range(left, right):
        if nums[j] < target:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[right] = nums[right], nums[i + 1]
    return i + 1


if __name__ == '__main__':
    a = [1, 2, 3, 2, 3, 2, 3, 2, 3, 1, 2, 3, 1]
    quick_sort(a, 0, 12)
    print(a)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
(1)时间复杂度，O（nlogn）
(2)空间复杂度，O（n），除了递归时所需要的栈空间，在merge时还需要额外的空间来保存有序数组的临时结果，空间复杂度为O（n）
(3)稳定性：稳定。
"""

"""
def merge_sort(nums):  # 类似于树的后序遍历
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[0:mid])
    right = merge_sort(nums[mid:])
    res = merge(left, right)
    return res


def merge(left, right):
    sorted_list = []
    m, n = len(left), len(right)
    i, j = 0, 0
    while i < m and j < n:
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list
"""


def merge_sort(nums, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(nums, left, mid)
        merge_sort(nums, mid + 1, right)
        merge(nums, left, mid, right)


def merge(nums, left, mid, right):
    res = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:  # '<='比较关键，因为要保证归并排序的稳定性
            res.append(nums[i])
            i += 1
        else:
            res.append(nums[j])
            j += 1
    while i <= mid:
        res.append(nums[i])
        i += 1
    while j <= right:
        res.append(nums[j])
        j += 1
    nums[left:right + 1] = res


def merge_sort_non_recursive(nums):
    i = 1
    n = len(nums)
    while i < n:
        low = 0
        while low < n:
            high = min(low + 2 * i - 1, n - 1)  # 要保证nums在low到mid之间和mid到high之间有序
            mid = (low + high) // 2
            merge(nums, low, mid, high)
            low += 2 * i
        i = i * 2


if __name__ == '__main__':
    test_nums = [1, 2, 4, 3, 1, 2, 1, 2, 3, 4, 100, 98, 32, 18, 7]
    # nums = [1]
    # print(merge_sort(num, 0, len(num) - 1))
    # merge_sort(test_nums, 0, len(test_nums) - 1)
    merge_sort_non_recursive(test_nums)
    print(test_nums)

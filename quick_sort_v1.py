#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
（1）时间复杂度
    快速排序最好情况下的时间复杂度为O（nlogn），待排序列越接近无序，算法效率越高
    快速排序在（1）从小到大有序（2）从大到小有序（3）所有元素相同的情况下时间复杂度为O（n^2）
（2）空间复杂度，空间复杂度为O（logn）。快速排序是递归进行的，需要栈的辅助，占用额外空间。
（3）快速排序是不稳定的，在partition交换位置时会出现不稳定。
"""


def quick_sort(array, left, right):  # 类似于树的先序遍历
    if left < right:  # left right 为索引
        location = partition(array, left, right)
        print(location)
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


"""
以下是面试时的错误写法
"""


def quick_sort_interview(nums):
    if not nums:
        return
    position = partirion_interview(nums)
    print(position)
    print(nums)
    quick_sort_interview(nums[0:position])
    quick_sort_interview(nums[position + 1:])


def partirion_interview(nums):
    target = nums[-1]
    i, j = -1, 0
    while j < len(nums) - 1:
        if nums[j] < target:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    nums[i + 1], nums[j] = nums[j], nums[i + 1]
    return i + 1


if __name__ == '__main__':
    a = [1, 2, 3, 2]
    quick_sort(a, 0, 3)
    # quick_sort_interview(a)
    # 面试时写错是因为每次调用quick_sort_interview函数传递的参数不是同一个nums！！！
    # 只有第一次传递的是输入的nums
    print(a)
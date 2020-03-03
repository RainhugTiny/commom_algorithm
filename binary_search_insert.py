#!/usr/bin/env python
# -*- coding: utf-8 -*-

def binary_search_insert(nums, value):
    l, r = 0, len(nums) - 1
    while l <= r:
        """
        最后一次循环、l与r一定相等。因此m与l、r相等。
        若待插入值value大于nums[m]，l应该加一，则value插入到l的位置，就是nums[m]后面的位置，
        若待插入值value小于nums[m]，r应该减一，则value插入到l的位置，就是nums[m]现在的位置，即插入之后nums[m]之前的位置。
        所以循环结束后l一定大于r(l=r+1)，l的值就是待插入值要插入的位置。
        """
        m = (l + r) // 2
        if nums[m] == value:
            return m
        elif nums[m] > value:
            r = m - 1
        else:
            l = m + 1
    return l


def binary_search_left(nums, value):
    """
    找到nums中value最左侧的位置
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] >= value:
            r = m - 1
        else:
            l = m + 1
    return l


def binary_search_right(nums, value):
    """
    找到nums中value最右侧的位置
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] <= value:
            l = m + 1
        else:
            r = m - 1
    return l - 1


if __name__ == '__main__':
    input = [1, 3, 4, 4.5, 4.5, 5]
    value = 3
    # res = binary_search_insert(input, value)
    # input.insert(res, value)
    # print input
    res = binary_search_right(input, value)
    print res

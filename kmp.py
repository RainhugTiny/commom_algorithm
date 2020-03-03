#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
在一个文本串m内查找一个模式串p的出现位置,时间复杂度O(m+n),暴力方法的时间复杂度O(m*n)。
规则
0.模式串p，主串m, next数组表示当模式串中p[j]与主串中的m[i]不匹配时，应该把j指针向前移动到哪个位置。
1.若模式串中的前k个元素与模式串中p[j]元素前的k个元素相同,则next[j] == k。
2.在1的基础上，若模式串中的第k+1个元素p[k]等于第j个元素p[j],则模式串中的前k+1个元素与模式串中p[j+1]元素前的k+1个元素相同,即next[j+1] = k+1。
3.在1的基础上，若模式串中的第k+1个元素p[k]不等于第j个元素p[j], 则问题转化为从主串p[j-k:j]中匹配模式串p[0:k]时p[k]与p[j]不匹配的问题，此时k应该移动到next[k]。
4.当k==-1时, 说明p[j+1]前不存在x，使模式串中的前x个元素与模式串中p[j+1]元素前的x个元素相同。
"""


def getNext(pattern):
    nxt = [0 for i in range(len(pattern))]
    nxt[0] = -1
    k, j = -1, 0
    while j < len(pattern) - 1:
        if k == -1 or pattern[k] == pattern[j]:
            k, j = k + 1, j + 1
            nxt[j] = k
        else:
            k = nxt[k]
    return nxt


def kmp(txt, pattern):
    nxt = ipv_get_next(pattern)
    i, j = 0, 0
    while i < len(txt) and j < len(pattern):
        if j == -1 or txt[i] == pattern[j]:
            i, j = i + 1, j + 1
        else:
            j = nxt[j]
    if j == len(pattern):
        return i - j
    else:
        return -1


def ipv_get_next(pattern):
    nxt = [0 for i in range(len(pattern))]
    nxt[0] = -1
    k, j = -1, 0
    while j < len(pattern) - 1:
        if k == -1 or pattern[k] == pattern[j]:
            k, j = k + 1, j + 1
            if pattern[k] == pattern[j]:
                nxt[j] = nxt[k]
            else:
                nxt[j] = k
        else:
            k = nxt[k]
    return nxt


if __name__ == '__main__':
    p = "dish"
    m = "aaacihdishihabcsohohs"
    print kmp(m, p)

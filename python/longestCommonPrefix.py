#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/24 6:31 PM
# @Author: wisdom
# @File:longestCommonPrefix.py
import math


def longestCommonPrefix(lists):
    commonPre = lists[0]
    for index in range(len(lists)):
        if index < len(lists) - 1:
            commonPre = longCommonPrefix(commonPre, lists[index + 1])
            if commonPre == "":
                print('hello')
                return ""
    return commonPre


def longCommonPrefix(str1, str2):
    result = ""
    if str1 == "" or str2 == "":
        return ""
    length = min(len(str2), len(str1))
    if len(str1) == 0 or len(str2) == 0:
        return result
    for index in range(length):
        if str1[index] == str2[index]:
            result += str1[index]
        else:
            break
    return result


if __name__ == '__main__':
    print('longest common prefix')
    lists = list(map(str, input().split()))
    print(longestCommonPrefix(lists))

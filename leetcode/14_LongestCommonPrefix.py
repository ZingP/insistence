#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/9
"""
内容：
　　Write a function to find the longest common prefix string amongst an array of strings.
　　编写一个函数来查找字符串数组中最长的公共前缀字符串。
理解题目：
　　如数组 ["a", "b"]   最长的公共前缀字符串是 “”；
　　如数组 ["aa", "aa"]   最长的公共前缀字符串是 “aa”；
　　如数组 ["abc", "abcd"]   最长的公共前缀字符串是 “abc”。。。

思路：
1 如果数组为空，则最长公共前缀为""；
2 如果数组不为空：
（1）找出字符串数组中长度最短的字符串min，其长度为min_len; 因为最长的公共前缀长度不会超过min_len；
（2）遍历数组，将min位置为[i] 的字符 和 数组中其他字符串位置为[i]的字符 比较；
        如果不相等，则最长公共前缀为 min的前i个字符；
        如果都相等，则最长公共前缀为 min。
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortstr = min(strs, key=len)
        for i, cha in enumerate(shortstr):
            for other in strs:
                if other[i] != cha:
                    return shortstr[:i]
        return shortstr



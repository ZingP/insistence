#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/3/2

# 保留有限历史记录正是 collections.deque 大显身手的时候。
# 比如，下面的代码在多行上面做简单的文本匹配， 并返回匹配所在行的前N行或者后N行：

from collections import deque

lines = ["aa", "aaa", "abc", "cc", "dd", "ca", "ee"]

def search(lines, pattern, history=5):
    """返回前N行"""
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':

    for line, prevlines in search(lines, 'a', 3):
        print("line>>", line)
        print("prevlines", prevlines)
        for pline in prevlines:
            print(pline)



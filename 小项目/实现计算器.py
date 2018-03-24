#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Zing-p"
# Date: 2017/10/30

import re

def is_symbol(element):
    """遍历element里的元素如果是运算符的话返回的结果为True，如果是数字直接返回False"""
    res = False
    symbol = ['+', '-', '*', '/', '(', ')']
    if element in symbol:
        res = True
    return res

def priority(top_sym, wait_sym):
    """
    根据运算符栈的栈顶元素，与待入栈的元素，返回相应的优先级。
    :param top_sym: 栈顶运算符
    :param wait_sym: 待入栈运算符
    :return: -1 ，0 ，1
    """
    # 定义几种运算级别，'+','-'一个级别。
    level1 = ['+', '-']
    level2 = ['*', '/']
    level3 = ['(']
    level4 = [')']
    # 运算符栈栈顶元素为+，-
    if top_sym in level1:
        if wait_sym in level2 or wait_sym in level3:
            return -1
        else:
            return 1
    # 运算符栈栈顶元素为*/，/
    elif top_sym in level2:
        if wait_sym in level3:
            return -1
        else:
            return 1
    # 运算符栈栈顶元素为(
    elif top_sym in level3:
        if wait_sym in level4:  # 右括号)碰到了(,那么左括号应该弹出栈。
            return 0
        else:
            return -1  # 只要栈顶元素为(,等待入栈的元素都应该无条件入栈。
    else:
        return -1

def calculate(num1, symbol, num2):
    res = 0
    if symbol == '+':
        res = num1 + num2
    elif symbol == '-':
        res = num1 - num2
    elif symbol == '*':
        res = num1 * num2
    elif symbol == '/':
        res = num1 / num2
    return res

def init_action(formula):
    # 通过re模块去掉空格
    formula = re.sub(' ', '', formula)
    # 以横杠数字为分隔符进行切分
    formula_1 = [i for i in re.split('(\-\d+\.*\d*)', formula) if i]
    # 作为最后生成的列表添加入此列表
    formula_ele_list = []
    while True:
        # 如果列表为空退出循环
        if len(formula_1) == 0:
            break
        # 利用列表的pop方法把最后一个值弹出来
        exp = formula_1.pop(0)
        # print('==>',exp)
        # 判断是负数还是减号。
        if len(formula_ele_list) == 0 and re.search('^\-\d+\.*\d*$', exp):
            formula_ele_list.append(exp)
            continue
        # 和formula_ele_list进行比较，如果横杠数字左边那个符号是一个加减乘除左括号那它肯定就是一个负号的形式。
        if len(formula_ele_list) > 0:
            if re.search('[\+\-\*\/\(]$', formula_ele_list[-1]):
                formula_ele_list.append(exp)
                continue
        new_l = [i for i in re.split('([\+\-\*\/\(\)])', exp) if i]
        formula_ele_list += new_l
    print(formula_ele_list)
    return formula_ele_list

def main(formula_list):

    number_stack = []
    symbol_stack = []
    for ele in formula_list:
        print('-'*20)
        print('数字栈', number_stack)
        print('运算符栈', symbol_stack)
        print('待入栈运算符', ele)
        ret = is_symbol(ele)
        if not ret:
            # 压入数字栈
            # 字符串转换为符点数，你也可以转换为整数，整数不如浮点数运算精度高
            ele = float(ele)
            number_stack.append(ele)
        else:
            # 压入运算符栈
            while True:
                # 如果运算符栈等于0无条件入栈
                if len(symbol_stack) == 0:
                    symbol_stack.append(ele)
                    # break掉while循环
                    break
                # 用priority函数进行优先级比较得出一个res的结果
                res = priority(symbol_stack[-1], ele)

                if res == -1:
                    # 如果是-1压入符号栈进入下一次循环
                    symbol_stack.append(ele)
                    break
                elif res == 0:
                    # 如果是0弹出栈内元素，进入下一次循环
                    symbol_stack.pop()
                    break
                elif res == 1:
                    # 如果是1弹出栈内元素，弹出数字元素。
                    symbol = symbol_stack.pop()
                    num2 = number_stack.pop()
                    num1 = number_stack.pop()
                    # 执行计算
                    # 计算之后压入数字栈
                    number_stack.append(calculate(num1, symbol, num2))
    while len(symbol_stack) != 0:
        symbol = symbol_stack.pop()
        num2 = number_stack.pop()
        num1 = number_stack.pop()
        number_stack.append(calculate(num1, symbol, num2))

    return number_stack, symbol_stack

if __name__ == '__main__':
    # strings = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))'
    strings = '-1-2*(-2+3)'
    # strings = input("请输入算式：")
    formula_li = init_action(strings)
    # print(formula_li)
    r = main(formula_li)
    # print('====>', r)
    print('最终结果是：', r[0][0])
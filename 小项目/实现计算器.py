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
    print("横杠数字分割之后：", formula_1)
    # 作为最后生成的列表添加入此列表
    formula_ele_list = []
    while True:
        # 如果列表为空退出循环
        if len(formula_1) == 0:
            break
        # 利用列表的pop方法把第一个值弹出来
        exp = formula_1.pop(0)
        print("取出的exp::", exp)
        # print('==>',exp)
        # 如果是第一个是以-开头的数字（包括小数）则无条件加入。^\-\d+ 匹配-开头，接着是数字一次或者多次， 匹配小数点0次或多次，匹配数字0次或多次
        if len(formula_ele_list) == 0 and re.search('^\-\d+\.*\d*$', exp):
            formula_ele_list.append(exp)
            continue
        # 和formula_ele_list进行比较，如果横杠数字左边那个符号是一个加减乘除左括号那它肯定就是一个负号的形式。
        if len(formula_ele_list) > 0:
            # 如果formula_ele_list最后一个元素是运算符，）除外，新来的数字无条件入栈。
            if re.search('[\+\-\*\/\(]$', formula_ele_list[-1]):
                print("匹配", formula_ele_list[-1])
                formula_ele_list.append(exp)
                continue
        # 按照运算符分割开
        new_l = [i for i in re.split('([\+\-\*\/\(\)])', exp) if i]
        print("将exp分割", new_l)
        formula_ele_list += new_l
        print("list:", formula_ele_list)
    return formula_ele_list

def main(formula_list):

    number_stack = []
    symbol_stack = []
    for ele in formula_list:
        print('-'*20)
        print('数字栈', number_stack)
        print('运算符栈', symbol_stack)
        print('待入栈字符', ele)
        ret = is_symbol(ele)
        # ret = ele.isdigit()  不能判断小数和负数
        if not ret:
            print("是数字", ele)
            # 压入数字栈
            # 字符串转换为符点数，你也可以转换为整数，整数不如浮点数运算精度高
            ele = float(ele)
            number_stack.append(ele)
        else:
            # 如果是运算符
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
                    print("弹出后", symbol_stack)
                    break
                elif res == 1:
                    # 如果是1弹出栈内元素，弹出数字元素。
                    symbol = symbol_stack.pop()
                    num2 = number_stack.pop()
                    num1 = number_stack.pop()
                    # 执行计算
                    # 计算之后压入数字栈
                    number_stack.append(calculate(num1, symbol, num2))
                    print("数字-运算符", number_stack, symbol_stack)
    while len(symbol_stack) != 0:
        print(symbol_stack, number_stack)
    # if len(symbol_stack) == 1:
    #
        symbol = symbol_stack.pop()
        num2 = number_stack.pop()
        num1 = number_stack.pop()
        number_stack.append(calculate(num1, symbol, num2))

    return number_stack, symbol_stack

if __name__ == '__main__':
    # strings = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))'
    strings = '-1-2*((-2+3)+(-2/2))'
    # strings = input("请输入算式：")
    formula_li = init_action(strings)
    # print(formula_li)
    r = main(formula_li)
    # print('====>', r)
    print('最终结果是：', r[0][0])
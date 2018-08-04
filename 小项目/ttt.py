#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "liuyouyuan"
# Date: 2018/4/28
menu = {
   '山东':{
      '青岛':['四方''黄岛','崂山','李沧'],
      '济南':['历城','槐荫','高新','长青'],
      '烟台':['龙口','莱山','蓬莱','招远']
   },
   '江苏':{
      '苏州':['沧浪','平江','吴中','昆山'],
      '南京':['秦淮','浦口','栖霞','江宁'],
      '无锡':['崇安','南山','北塘','锡山']
   },
   '浙江':{
      '杭州':['西湖','江干','下城','上城'],
      '宁波':['海曙','鸠江','无为','南陵'],
      '蚌埠':['蚌山','龙子湖','淮上','怀远',]
   },
   '广东':{
      '深圳':['罗湖','福田','南山','宝安'],
      '广州':['天河','海珠','越秀','白云'],
      '东莞':['长安','虎门','大朗','常平']

   }
}

exit_flag = False
while not exit_flag:
 for i in menu:
  print(i)
 choice_s = input("请输入以上任一省或直辖市名称>>>:")
 if choice_s.isdigit():
     choice_s = int(choice_s)
 if choice_s in menu:
  while not exit_flag:
   for i in menu[choice_s]:
    print("\t",i)
   choice_q = input("请输入以上任一市名称>>>:")
   if choice_q.isdigit():
       choice_q = int(choice_q)
   if choice_q in menu[choice_s]:
    while not exit_flag:
     for i in menu[choice_s][choice_q]:
      print("\t\t",i)
     choice_j = input("请输入以上任一区名称>>>:")
     if choice_j.isdigit():
         choice_j = int(choice_j)
     if choice_j in menu[choice_s][choice_q]:
      #print("gggg", choice_s, choice_q, choice_j)
      if menu[choice_s][choice_q] is list:
          pass
      #for i in menu[choice_s][choice_q][choice_j]:
       #print("\t\t",i)
      last = input("最后一层，按b返回>>>:")
      if last == "b":
       pass
      elif last == "q":
       exit_flag = True
     if choice_j == "b":
      break
     elif choice_j == "q":
      exit_flag = True
   if choice_q == "b":
    break
   elif choice_q == "q":
    exit_flag = True
#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
from prettytable import PrettyTable
p_table = PrettyTable()


def Get_Line(per_F):
    global p_table 

    #读取存储acl权限的文件
    per_Line = open(per_F,"r")

    #edit file
    per_S = ""
    per_read = per_Line.readlines()
    per_Line.close()

    row_one = ["dir\\account",]

    #创建表格的第一行
    for x in per_read:
        if "user:" in x and "default" not in x:
            row_oneIndex = x.split(':')[1]
            if row_oneIndex != "":
                row_one.append(row_oneIndex)
        if "owner" in x:
            row_owner = x.split(" ")[2].strip()
            if row_owner != "root":
                row_one.append(row_owner)

    #去掉第一行的重复用户名
    row_ONE = []
    [row_ONE.append(x) for x in row_one if x not in row_ONE]

    #删除不需要的行,并生成字符串
    per_neLine = [x for x in per_read  
            if "mask" not in x and "group" not in x and "default" not in x and "other" not in x and "user::" not in x and "owner:" not in x]
    for x in per_neLine:
        per_S += x

    p_table = PrettyTable(row_ONE)
    #p_table.align["目录\账号"] = "l"
    p_table.align["dir\\account"] = "l"

    Edit_Line(per_S,row_ONE)


def Edit_Line(per_line,row_ONE):
    """del do not need chat at the first , 
    sec del include .xls .doc master dir ext. ,
    thi create list to draw table
    """
    global p_table 

    #define del do not need chat regex pattern
    del_recycle_pat = re.compile(r"# file:.*回收站.*?\n\n",re.MULTILINE|re.DOTALL)
    #该脚本只显示二级目录的acl权限。顾用下面这个正则匹配
    del_morefile_pat = re.compile(r"# file:[^/]+//[^/]+/?[^/]+\n\n",re.MULTILINE|re.DOTALL)

    #下面这2个变量使用来移除符合条件的元素的
    enter="\n\n"
    y = ""

    per_lineL = per_line.split("\n\n")

    #把需要获取权限的目录都放进下面这个fine_lineL列表
    fine_lineL = []
    for x in per_lineL:
        y = x + enter
        ##第一个目录加入列表,等待删除
        #if del_masterfile_pat.findall(y):
        #    remove_lineL.append(x)
        #只查看到2级目录的权限
        if del_morefile_pat.findall(y):
            fine_lineL.append(x)

    #Create a remove list store remove list,创建一个空元素，在生成的per_lineL里面可能会有空元素用这个删除
    remove_lineL = []

    #把有回收站的目录加入列表,等待删除
    for x in fine_lineL:
        y = x + enter
        if del_recycle_pat.findall(y):
            remove_lineL.append(x)
    #删除回收站
    for x in remove_lineL:
        fine_lineL.remove(x)


    #获得目录对应用户的权限列表
    #row_ONE
    len_row = len(row_ONE)
    per_user = []

    for x in fine_lineL:
        #给表格的行,这个列表存的是目录以及用户对应的权限,例如["/xxx","r-x"],默认为---无权限
        row_per = []
        [row_per.append("---") for y in range(len_row)]
        #把每个目录和目录的用户权限分出来
        per_user = x.split("\n")
        dir = per_user[0].split(":")
        row_per[0]=dir[1].strip()
        #根据row_ONE里面的用户顺序来添加目录对应的权限到row_per列表
        for u in per_user[0:]:
            if "user:" in u:
                per_u = u.split(":")[1]
                #print per_u,
                for user in row_ONE:
                    if per_u == user:
                        permiss = u.split(":")[2].strip()
                        In = row_ONE.index(user)
                        row_per[In] = permiss
        p_table.add_row(row_per)

    print p_table

if __name__ == "__main__":
    from sys import argv
    Get_Line(argv[1])


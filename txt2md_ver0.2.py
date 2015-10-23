# -*- coding: utf-8 -*-
import re ,sys ,os
os.system("D:\\web\\txt2md_Project\\py\\txt2md_ver0.2")

def file_to_text_lst(file):
    #读取文件,转换为文本列表(文本文件为utf16)
    #str -> lst
    #例子:
    #lst=file_to_text_lst("D:\\web\\test1\\source\\test3.TXT")
    lst=[]
    file = open(file,"r",encoding='utf16')
    for line in file.readlines():
        lst.append(line)
    file.close()
    return lst
def replace_words_in_text(text_lst,word_lst):
    #替换制定文本
    #lst , lst -> lst
    #例子
    #print(replace_words_in_text( ['  7室内环境\n',
    #    '7.1  日照、天然采光、遮阳\n',
    #     '7.1.1  每套住宅应至少有一个居住空间能获得冬季日照。\n'],
    #    [("7","8"),("日照","太阳照"),("\n",""),(" ","")]))
    newlst=text_lst[:]
    for i in range(0,len(text_lst)):
        for word in word_lst:
            if word[0] in text_lst[i] :
                newlst[i]=newlst[i].replace(word[0],word[1],
                    len(newlst[i])//len(word[0]))
    return newlst
def del_line(text_lst,con_lst):
    #设定条件删除行
    #lst , lst -> lst
    #例子
    #print(del_line(test_text,[is_empty,is_page]))
    # newlst=text_lst[:]
    # for i in range(len(newlst)-1,-1,-1):
    #     for con in con_lst:
    #         if con(newlst,i):
    #             del newlst[i]
    newlst=[]
    for i in range(0,len(text_lst)):
        if con_judge(text_lst,i,con_lst):
            pass
        else:
            newlst.append(text_lst[i])
    return newlst

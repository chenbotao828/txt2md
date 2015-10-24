# -*- coding: utf-8 -*-
import re
#******************************************************************************
#对 aline["text"] 进行上下文无关的判定,返回 True 或者 False
#******************************************************************************
def cft_content_start(aline):
    return True if aline["text"]=="目录"or"目次" else False
def cft_content_title(aline):
    return True if re.match('\d+\w+[．….]+',aline["text"]) else False
def cft_content_subtitle(aline):
    return True if re.match('\d+\.\d+\w+[．….]+',aline["text"]) else False
def cft_content_else(aline):
    return True if re.match('\w+[．….]+',aline["text"]) else False
def cft_pic(aline):
    return True if re.match('图\d+\w.*',aline["text"]) else False
def cft_empty(aline):
    return True if aline["text"] == "" else False
def cft_table_name(aline):
    return True if re.match("表\d+\.\d+\.\d+",aline["text"]) else False
def cft_md_table(aline):
    return True if re.match("\|.*\|$",aline["text"]) else False
def cft_table(aline):
    if cft_table_name(aline) :
        return True
    elif cft_md_table(aline):
        return True
    return False
def cft_table_grid(aline):
    a= re.match('┏[━┳]*┓',aline["text"])
    b= re.match('┣[━╋]*┫',aline["text"])
    c= re.match('┗[━┻]*┛',aline["text"])
    if a or b or c:
        return True
    else:
        False
def cft_table_remarks(aline):
    return True if re.match("注：",aline["text"]) else False
def cft_page(aline):
    if re.match('\d+',aline["text"]):
        if aline["text"] == re.match('\d+',aline["text"]).group():
            return True
    else:
        return False
def cft_0p0p0(aline):
    return True if re.match('\d+\.\d+\.\d+',aline["text"]) else False
def cft_0p0(aline):
    return True if re.match('\d+\.\d+',aline["text"]) else False
def cft_0(aline):
    return True if re.match('\d+',aline["text"]) else False
#******************************************************************************
#对在aline_lst内的第i项aline["text"] 进行上下文有关的判定,返回 True 或者 False
#******************************************************************************
def cft_list(aline):
    return True if re.match('\d+\.\d+\.\d+.*：1.*[。；]2',aline["text"]) else False

#******************************************************************************
#其他
#******************************************************************************
def con_judge(text_lst,i,con_lst):
    for con in con_lst:
        if con(text_lst,i):
            return True
    return False
def make_aline(raw_text,i):
    return{"num":i,
           "raw_text":raw_text,}
def file_to_aline_lst(file):
    lst=[]
    file = open(file,"r",encoding='utf16')
    f=file.readlines()
    for i in range(0,len(f)):
        lst.append(make_aline(f[i],i))
    file.close()
    return lst
def replace_aline_lst(lst,word_lst):
    # lst=lst[:]
    for i in range(0,len(lst)):
        lst[i]["text"]=lst[i]["raw_text"]
        for word in word_lst:
            if word[0] in lst[i]["text"]:
                lst[i]["text"]=lst[i]["text"].replace(word[0],word[1])
    return lst
def add_cft(lst,cft_con_lst):
    def cft(aline,cft_con_lst):
        for con in cft_con_lst:
            if eval(con+"(aline)"):
                return con
        return "default"
    for aline in lst:
       aline["cft"]=cft(aline,cft_con_lst)
    return lst
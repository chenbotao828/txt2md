# -*- coding: utf-8 -*-
import re
#******************************************************************************
#对 aline["text"] 进行上下文无关的判定,返回 True 或者 False
#******************************************************************************
def default_info(aline):
    return "none"
def cft_content_start_info(aline):
    return  "none"
def cft_content_start(aline):
    return True if aline["text"]=="目录"or"目次" else False
def cft_content_title_info(aline):
    ma=re.match('(\d+)(\w)+[．….]+',aline["text"])
    return [int(ma.group(1)),ma.group(2)]
def cft_content_title(aline):
    return True if re.match('\d+\w+[．….]+',aline["text"]) else False
def cft_content_subtitle_info(aline):
    ma=re.match('(\d+)\.(\d+)(\w+)[．….]+',aline["text"])
    return [int(ma.group(1)),int(ma.group(2)),ma.group(3)]
def cft_content_subtitle(aline):
    return True if re.match('\d+\.\d+\w+[．….]+',aline["text"]) else False
def cft_content_else_info(aline):
    return "none"
def cft_content_else(aline):
    return True if re.match('\w+[．….]+',aline["text"]) else False
def cft_pic_info(aline):
    ma= re.match('图(\d+)(\w*)',aline["text"])
    return ["图",int(ma.group(1)),ma.group(2)]
def cft_pic(aline):
    return True if re.match('图\d+\w*',aline["text"]) else False
def cft_empty_info(aline):
    return "none"
def cft_empty(aline):
    return True if aline["text"] == "" else False
def cft_table_name_info(aline):
    ma = re.match("表(\d+)\.(\d+)\.(\d+)(.*)",aline["text"])
    return ["表",int(ma.group(1)),int(ma.group(2)),int(ma.group(3)),ma.group(4)]
def cft_table_name(aline):
    return True if re.match("表\d+\.\d+\.\d+",aline["text"]) else False
def cft_md_table_info(aline):
    return "none"
def cft_md_table(aline):
    return True if re.match("\|.*\|$",aline["text"]) else False
def cft_table_info(aline):
    return "none"
def cft_table(aline):
    if cft_table_name(aline) :
        return True
    elif cft_md_table(aline):
        return True
    return False
def cft_table_grid_info(aline):
    return "none"
def cft_table_grid(aline):
    a= re.match('┏[━┳]*┓',aline["text"])
    b= re.match('┣[━╋]*┫',aline["text"])
    c= re.match('┗[━┻]*┛',aline["text"])
    if a or b or c:
        return True
    else:
        False
def cft_table_remarks_info(aline):
    return ["注:",re.match("注：(.*)",aline["text"]).group(1)]
def cft_table_remarks(aline):
    return True if re.match("注：.*",aline["text"]) else False
def cft_page_info(aline):
    return [int(re.match('(\d+)',aline["text"]).group(1)),]
def cft_page(aline):
    if re.match('\d+',aline["text"]):
        if aline["text"] == re.match('\d+',aline["text"]).group():
            return True
    else:
        return False
def cft_0p0p0_info(aline):
    ma=re.match('(\d+)\.(\d+)\.(\d+)(.*)',aline["text"])
    return [int(ma.group(1)),int(ma.group(2)),int(ma.group(3)),ma.group(4)]
def cft_0p0p0(aline):
    return True if re.match('\d+\.\d+\.\d+',aline["text"]) else False
def cft_0p0_info(aline):
    ma=re.match('(\d+)\.(\d+)(.*)',aline["text"])
    return [int(ma.group(1)),int(ma.group(2)),ma.group(3)]
def cft_0p0(aline):
    return True if re.match('\d+\.\d+',aline["text"]) else False
def cft_0_info(aline):
    ma=re.match('(\d+)(.*)',aline["text"])
    return [int(ma.group(1)),ma.group(2)]
def cft_0(aline):
    return True if re.match('\d+',aline["text"]) else False
#******************************************************************************
#对在aline_lst内的第i项aline["text"] 进行上下文有关的判定,返回 True 或者 False
#******************************************************************************
def neighbor_is_right(lst,i,r,is_down,is_up):
    for j in range (1,r+1):#上下 r 行之内有正确的邻居
        if j+i in range (0,len(lst)):
            if is_down(lst,i,j):
                return True
        if i-j in range (0,len(lst)):
            if is_up(lst,i,j):
                return True
    return False
def cst_index(lst,i):
    def is_down(lst,i,j):
        if i+j in range(0,len(lst)):
            info=lst[i]["cft_info"]
            info1=lst[i+j]["cft_info"]
            if info1[:-1] in [
                [info[0],info[1],info[2]+1],
                [info[0],info[1]],
                [info[0],info[1]+1],
                [info[0]+1],
                ]:
                return True
        else: False
    def is_up(lst,i,j):
        if i-j in range(0,len(lst)):
            info=lst[i]["cft_info"]
            info1=lst[i-j]["cft_info"]
            if info1[:-1] in [
                [info[0],info[1],info[2]-1],
                [info[0],info[1]],
                ]:
                return True
        else: False
    if lst[i]["cft"]=="cft_0p0p0":
        if neighbor_is_right(lst,i,50,is_down,is_up):
            return True
    return False
def cst_subtitle(lst,i):
    def is_down(lst,i,j):
        if i+j in range(0,len(lst)):
            info=lst[i]["cft_info"]
            info1=lst[i+j]["cft_info"]
            if lst[i+j]["cft"]=="cft_0p0p0":
                if info1[:-1]==[info[0],info[1],1]:
                    return True
        else: False
    def is_up(lst,i,j):
        if i-j in range(0,len(lst)):
            info=lst[i]["cft_info"]
            info1=lst[i-j]["cft_info"]
            if lst[i-j]["cft"]=="cft_0p0p0":
                if info1[0]==info[0] and info1[1]==info1[1]-1 :
                    return True
            elif lst[i-j]["cft"]=="cft_0":
                if info1[0]==info1[0]:
                    return True
        else: False
    if lst[i]["cft"]=="cft_0p0":
        if neighbor_is_right(lst,i,5,is_down,is_up):
            return True
    return False
def cst_title(lst,i):
    def is_down(lst,i,j):
        if i+j in range(0,len(lst)):
            info=lst[i]["cft_info"]
            info1=lst[i+j]["cft_info"]
            if lst[i+j]["cft"]=="cft_0p0":
                if info1[:-1]==[info[0],1]:
                    return True
        else: False
    def is_up(lst,i,j):
        if i-j in range(0,len(lst)):
            info=lst[i]["cft_info"]
            info1=lst[i-j]["cft_info"]
            if lst[i-j]["cft"]=="cft_0p0p0":
                if info1[0]==info[0]-1 :
                    return True
        else: False
    if lst[i]["cft"]=="cft_0":
        if neighbor_is_right(lst,i,5,is_down,is_up):
            return True
    return False
# def cst_list(lst,i):
#     def is_down(lst,i,j):
#         return False
#     def is_up(lst,i,j):
#         if i-j in range(0,len(lst)):
#             if lst[i-j]["text"][-1] =="：":

#     if lst[i]["cft"]=="cft_0":
#         if neighbor_is_right(lst,i,30,is_down,is_up):
#             return True
#     return False
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
    #content free type
    for aline in lst:
       aline["cft"]=cft(aline,cft_con_lst)
    return lst
def add_cft_info(lst):
    for aline in lst:
        con = aline["cft"]
        aline["cft_info"]= eval(con+"_info(aline)")
    return lst
def add_cst(lst,cst_con_lst):
    def cst(lst,i,cst_con_lst):
        for con in cst_con_lst:
            if eval(con+"(lst,i)"):
                return con
        return "none"
    #content sensitive type
    for i in range(0,len(lst)):
        lst[i]["cst"]=cst(lst,i,cst_con_lst)
    return lst
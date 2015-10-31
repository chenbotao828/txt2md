# -*- coding: utf-8 -*-
import func.rt 

txt_list=[
"C:\\Users\\Administrator\\Documents\\GitHub\\txt2md\\test_sample\\术语.txt",
]
doc_type="GB_SY"

do_list=[
    ("replace_aline_lst","replace_word_lst"),
    ("add_cft","cft_con_lst"),
    ("add_cft_info","cft_info_dic"),
    ("add_cst","cst_con_lst"),
    ("add_md","md_con_dic"),
    ("del_lst","del_con_lst"),
    ("insert_lst","insert_con_dic"),
    ("merge_lst","merge_con_lst"),
]

exec("import config."+doc_type)
for txt in txt_list:
    lst=func.rt.file_to_aline_lst(txt)
    for do in do_list:
        exec("lst=func.rt."+do[0]+"(lst,config."+doc_type+"."+do[1]+")")

    f=open(txt[:-3]+"md",'w',encoding='utf16')
    for aline in lst:
        if "md" in aline.keys():
            line=aline["md"]+'\n'
            f.write(line)
    f.close()

#for aline in lst:
#    print(aline)
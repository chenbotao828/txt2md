# -*- coding: utf-8 -*-
import func.rt , config.GB_ZW
txt_list=[
"C:\\Users\\Administrator\\Documents\\GitHub\\txt2md\\test_sample\\条文说明.txt",
"C:\\Users\\Administrator\\Documents\\GitHub\\txt2md\\test_sample\\正文.txt"
]


for txt in txt_list:
    lst=func.rt.file_to_aline_lst(txt)
    lst=func.rt.replace_aline_lst(lst,config.GB_ZW.replace_word_lst)
    lst=func.rt.add_cft(lst,config.GB_ZW.cft_con_lst)
    lst=func.rt.add_cft_info(lst)
    lst=func.rt.add_cst(lst,config.GB_ZW.cst_con_lst)
    lst=func.rt.add_md(lst,config.GB_ZW.md_con_dic)
    lst=func.rt.del_lst(lst,config.GB_ZW.del_con_lst)
    lst=func.rt.insert_lst(lst,config.GB_ZW.insert_con_dic)
    lst=func.rt.merge_lst(lst,config.GB_ZW.merge_con_lst)

    f=open(txt[:-3]+"md",'w',encoding='utf16')
    for aline in lst:
        if "md" in aline.keys():
            line=aline["md"]+'\n'
            f.write(line)
    f.close()
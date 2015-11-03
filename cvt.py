# -*- coding: utf-8 -*-
import func.rt , sys ,os
'''
使用方法:

python cvt.py type root

type=>文本类型,例如"GB"
root=>文件路径,例如"C:\\Users\\Administrator\\Documents\\GitHub\\txt2md\\test_sample\\GB50096-2011"
脚本程序生成新Markdown文档,位于原路径
'''
# page_type , file => make .md
def make_md_page(page_type,txt):
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
    lst=func.rt.file_to_aline_lst(txt)
    exec("import config."+page_type)
    for do in do_list:
        lst=eval("func.rt."+do[0]+"(lst,config."+page_type+"."+do[1]+")")
    f=open(txt[:-3]+"md",'w',encoding='utf16')
    for aline in lst:
        if "md" in aline.keys():
            line=aline["md"]+'\n'
            f.write(line)
    f.close()
    print(page_type+" "+txt+" DONE!")
# main
doc_type=sys.argv[1]
root = sys.argv[2]
#例子:
#doc_type = "GB"
#root = "C:\\Users\\Administrator\\Documents\\GitHub\\txt2md\\test_sample\\GB50096-2011"
exec("import config."+doc_type)
for i in os.listdir(root):
    if os.path.isfile(os.path.join(root,i)) and i[-4:] in [".txt",".TXT"]:
        txt = root + os.sep + i
        make_md_page(config.GB.make_page_type(i,doc_type),txt)
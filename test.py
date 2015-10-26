# -*- coding: utf-8 -*-
import func.rt , config.GB_ZW
lst=func.rt.file_to_aline_lst(
    "C:\\Users\\Administrator\\Documents\\GitHub\\txt2md\\test_sample\\正文.txt")
lst=func.rt.replace_aline_lst(lst,config.GB_ZW.replace_word_lst)
lst=func.rt.add_cft(lst,config.GB_ZW.cft_con_lst)
lst=func.rt.add_cft_info(lst)
lst=func.rt.add_cst(lst,config.GB_ZW.cst_con_lst)
for aline in lst:
    print(aline["cst"])
    print(aline["text"])
    # print(aline)

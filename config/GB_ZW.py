#存放参数

#******************************************************************************
#replace_word_lst 用于 replace_aline_lst函数,将aline["raw_text"]中的词语替换
#生成aline["text"]
#******************************************************************************
replace_word_lst =[
#correction_replace_lst
    ("mz" , "㎡"),
    ("m2" , "㎡"),
    ("m3" , "m³"),
    ("mo" , "m。"),
    (":" , "："),
    ("／", "/"),
    ("(" , "（"),
    (")" , "）"),
    (" " , ""),
    ("．" , "."),
    ("," , "，"),
    (";" , "；"),
    ("房问","房间"),
    ("空问","空间"),
    ("oo","00"),
    ("OO","00"),
    ("ll","11"),
    ("lO","10"),
    ("\n" , ""),
#markdown_replace_lst
     ('┃','|'),
    ('\\','\\\\'),
    ('`','\`'),
    ('*','\*'),
    ('_','\_'),
    ('#','\#'),
    ('+','\+'),
    ('!','\!'),]

#******************************************************************************
#cft_con_lst 添加aline["cft"]属性,即上下文无关类型
#******************************************************************************
cft_con_lst=[
    "cft_pic",
    "cft_empty",
    "cft_table_name",
    "cft_md_table",
    "cft_table_grid",
    "cft_table_remarks",
    "cft_page",
    "cft_0p0p0",
    "cft_0p0",
    "cft_0",
    ]
#******************************************************************************
#cft_info_dic 添加aline["cft_info"]属性
#******************************************************************************
cft_info_dic={
    "cft_pic":"cft_pic_info",
    "cft_table_name":"cft_table_name_info",
    "cft_table_remarks":"cft_table_remarks_info",
    "cft_page":"cft_page_info",
    "cft_0p0p0":"cft_0p0p0_info",
    "cft_0p0":"cft_0p0_info",
    "cft_0":"cft_0_info",
}
#******************************************************************************
#cst_con_lst 添加aline["cst"]属性,即上下文有关类型
#******************************************************************************
cst_con_lst=[
    "cst_more_index",
    "cst_index",
    "cst_subtitle",
    "cst_title",
    "cst_list",
    "cst_first_md_table",
    ]

#******************************************************************************
#md_con_dic 用于 add_md函数,添加aline["md"]属性,即md格式内容
#******************************************************************************
md_con_dic={
    "cst_more_index":"md_more_index",
    "cst_index":"md_index",
    "cst_subtitle":"md_subtitle",
    "cst_title":"md_title",
    "cst_list":"md_list",
    "cft_pic":"md_pic",
    "cft_empty":"md_empty",
    "cft_table_name":"md_table_name",
    "cst_first_md_table":"md_md_table",
    "cft_md_table":"md_md_table",
    "cft_table_grid":"md_table_grid",
    "cft_table_remarks":"md_table_remarks",
    }
#******************************************************************************
# del_con_lst 用于 del_lst 函数,表示删除的内容
#******************************************************************************
del_con_lst=[
    "cft_empty",
    "cft_table_grid",
    "cft_page",
]
#******************************************************************************
# insert_con_dic 用于 insert_lst 函数,表示插入的情况和内容
#******************************************************************************
insert_con_dic={
    "cst_first_md_table":"insert_first_md_table",
    "cst_more_index":"insert_empty",
    "cst_index":"insert_empty",
    "cst_subtitle":"insert_empty",
    "cst_title":"insert_empty",
    "cft_pic":"insert_empty",
    "cft_table_name":"insert_empty",
    "cft_table_remarks":"insert_empty",
    "cst_list":"insert_empty",
    }
#******************************************************************************
# merge_con_lst 用于 merge_lst 函数,表示连接的内容
#******************************************************************************
merge_con_lst=[
    "cft_empty",
    "cft_table_remarks",
    "cft_table_name",
    "cft_md_table",
    "md_table_head",
    "cst_more_index",
    "cst_index",
    "cst_subtitle",
    "cst_title",
    "cst_list",
    "cft_pic",
    ]

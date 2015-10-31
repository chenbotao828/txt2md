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
    (":" , "："),
    ("／", "/"),
    ("(" , "（"),
    (")" , "）"),
    (" " , ""), #全角空格
    (" ",""),#半角空格
    ("．" , "."),
    ("," , "，"),
    (";" , "；"),
    ("房问","房间"),
    ("空问","空间"),
    # ("oo","00"),
    # ("OO","00"),
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
    "cft_content_start",
    "cft_content_title",
    "cft_content_subtitle",
    "cft_content_else",
    "cft_empty",
    "cft_page",
    ]
#******************************************************************************
#cft_info_dic 添加aline["cft_info"]属性
#******************************************************************************
cft_info_dic={
    "cft_content_title":"cft_content_title_info",
    "cft_content_subtitle":"cft_content_subtitle_info",
    "cft_content_else":"cft_content_else_info",
    "cft_page":"cft_page_info",
}
#******************************************************************************
#cst_con_lst 添加aline["cst"]属性,即上下文有关类型
#******************************************************************************
cst_con_lst=[
    ]

#******************************************************************************
#md_con_dic 用于 add_md函数,添加aline["md"]属性,即md格式内容
#******************************************************************************
md_con_dic={
    "cft_empty":"md_empty",
    "cft_content_start":"md_content_start",
    "cft_content_title":"md_content_title",
    "cft_content_subtitle":"md_content_subtitle",
    "cft_content_else":"md_content_else",
    }
#******************************************************************************
# del_con_lst 用于 del_lst 函数,表示删除的内容
#******************************************************************************
del_con_lst=[
    "cft_empty",
    "cft_page",
    ]
#******************************************************************************
# insert_con_dic 用于 insert_lst 函数,表示插入的情况和内容
#******************************************************************************
insert_con_dic={
    "cft_content_start":"insert_separator",
    "cft_content_title":"insert_separator",
    "cft_content_subtitle":"insert_empty",
    "cft_content_else":"insert_empty",
    }
#******************************************************************************
# merge_con_lst 用于 merge_lst 函数,表示连接的内容
#******************************************************************************
merge_con_lst=[
    "cft_empty",
    "md_separator",
    "cft_content_start",
    "cft_content_title",
    "cft_content_subtitle",
    "cft_content_else",
    ]
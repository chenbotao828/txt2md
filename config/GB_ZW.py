#存放参数


#******************************************************************************
#replace_word_lst 用于 replace_aline_lst函数,将aline["raw_text"]中的词语替换
#生成aline["text"]
#******************************************************************************
replace_word_lst =[
#correction_replace_lst
    ("mz" , "㎡"),
    ("m2" , "㎡"),
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
    # ("oo","00"),
    # ("OO","00"),
    ("\n" , ""),
#markdown_replace_lst
     ('┃','|'),
    ('\\','\\\\'),
    ('`','\\`'),
    ('*','\\*'),
    ('_','\\_'),
    ('#','\\#'),
    ('+','\\+'),
    ('!','\\!'),]
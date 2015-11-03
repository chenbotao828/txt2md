# GB :国家标准的缩写
def make_page_type(txt,doc_type):
    if "目次" in txt:
        return "GB_ML"
    if "术语" in txt:
        return "GB_SY"
    else:
        return "GB_ZW"
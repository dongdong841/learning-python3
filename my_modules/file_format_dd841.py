# 模块名：file_format_dd841
# 功能：提供文件格式相关的操作
# 作者：zhangtianyu

import chardet

# 函数名：get_file_encoding_format
# 函数功能：获取文件的编码格式
# 参数：文件路径
# 返回值：文件的编码格式

def get_file_encoding_format(path):
    f = open(path, 'rb')
    c = f.read()
    f.close()
    info = chardet.detect(c)
    return info['encoding']

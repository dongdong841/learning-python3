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

# 函数名：chg_file_encoding_format
# 函数功能：将目标文件的编码格式转换到目标格式，结果是生成以_new结尾新文件，源文件不变。
#           注意_new是在文件名称最后面，文件名称是包含扩展名的。
#           例如：源文件：1.txt
#                 新文件：1.txt_new
#                 源文件：test
#                 新文件：test_new
# 参数：path 要转换的文件路径
#           tgt_encoding_format 目标编码格式
# 返回值：无
def chg_file_encoding_format(path, tgt_encoding_format):
    src_encoding_format = get_file_encoding_format(path)
    with open(path, 'r', encoding=src_encoding_format) as f:
        with open(path+'_new', 'w', encoding=tgt_encoding_format) as tgt_f:
            for line in f:
                tgt_f.write(line)
            tgt_f.close()
        f.close()

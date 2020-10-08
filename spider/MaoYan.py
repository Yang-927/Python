from fontTools.ttLib import TTFont

font = TTFont('./base.woff')  # 读取woff文件
font.saveXML('./base.xml')  # 转成xml

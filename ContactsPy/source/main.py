# -*- coding: utf-8 -*-

print "hello"

file = open('wxgui.py', 'r', encoding='UTF-8')
content = file.read()
print(content)
file.close()

#coding=big5
import os
from lib.person import Person
from lib.xmlfile import writeFile, readFile
from lib.editfile import editFile, add, remove, view, viewAll, save
from xml.dom import minidom

def openFile():
    
    name = raw_input("請輸入檔案名稱: ")
    
    if os.path.exists(name+".xml"):
        
        print (name + "檔案存在!\n")
        persons = readFile(name)
        
        editFile(name, persons)

    else:
        
        print "檔案不存在!\n"

def creatFile():
    
    name = raw_input("請輸入檔案名稱: ")
    
    if not os.path.exists(name+".xml"):

        file = open(name+".xml","w")
        print "已建立新檔案" + name + "\n"
        file.close()
        
    else:
        print "建立失敗!有同名檔案存在!\n"

def removeFile():

    name = raw_input("請輸入欲移除檔案名稱: ")
    
    if os.path.exists(name+".xml"):

        os.remove(name)
        print "移除檔案 " + name + " 成功!\n"
        
    else:
        print "失敗!檔案不存在!\n"

# Main

exit = False

while not exit:
    
    print "歡迎使用通訊錄管理系統!"
    print "*********************"
    print "請選擇功能:"
    print "1.開啟檔案"
    print "2.建立新檔"
    print "3.移除檔案"
    print "0.離開"
    print "*********************"
    choice = raw_input("選擇代號: ")

    if choice == "1":
        openFile()

    elif choice == "2":
        creatFile()

    elif choice == "3":
        removeFile()

    elif choice == "0":
        exit = True

    else:
        print "輸入錯誤! 請重新輸入!\n"

print "\n謝謝您使用!\n"

# Main End




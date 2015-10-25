#coding=utf-8

import os
from lib.person import Person
from lib.file import writeFile, readFile
from lib.addperson import add
from lib.delperson import remove
from lib.view import view, viewAll
from xml.dom import minidom

def editFile(fileName, persons):

    exit = False

    while not exit:
        
        print "目前使用檔案:" + fileName
        print "*********************"
        print "請選擇功能:"
        print "1.View"
        print "2.View All"
        print "3.Add"
        print "4.Remove"
        print "5.Save"
        print "6.Exit"
        print "*********************"
        
        choice = raw_input("選擇代號:")
        
        if choice == "1":
            view(persons)

        elif choice == "2":
            viewAll(persons)

        elif choice == "3":
            add(persons)

        elif choice == "4":
            remove(persons)

        elif choice == "5":
            save(persons)

        elif choice == "6":
            exit = True

def openFile():
    
    name = raw_input("請輸入檔案名稱:")
    
    if os.path.exists(name+".xml"):
        
        print (name + "檔案存在!\n")
        persons = readFile(name)
        
        editFile(name, persons)

    else:
        
        print "檔案不存在!\n"

def creatFile():
    
    name = raw_input("請輸入檔案名稱:")
    
    if not os.path.exists(name+".xml"):

        file = open(name+".xml","w")
        print "已建立新檔案\n"
        file.close()
        
    else:
        print "建立失敗!有同名檔案存在!\n"

def removeFile():

    name = raw_input("請輸入欲移除檔案名稱:")
    
    if os.path.exists(name+".xml"):

        os.remove(name)
        print "移除檔案成功!\n"
        
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
    print "4.離開"
    print "*********************"
    choice = raw_input("選擇代號:")

    if choice == "1":
        openFile()

    elif choice == "2":
        creatFile()

    elif choice == "3":
        removeFile()

    elif choice == "4":
        exit = True

print "\n謝謝您使用!\n"

# Main End




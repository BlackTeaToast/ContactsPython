# -*- coding: utf-8 -*-

import os
import lib.person
from lib.person import Person

exit = False
john = Person("John","Man","0912228","123456@gmail.com")
john.name = "as"
print john

while not exit:
    
    print "歡迎使用通訊錄管理系統!"
    print "*********************"
    print "請選擇功能:"
    print "1.開啟檔案"
    print "2.離開"
    print "*********************"
    choice = raw_input("選擇代號:")

    if choice == "1":
        name = raw_input("請輸入檔案名稱:")
        if os.path.exists(name):
            print (name + "檔案存在!\n")
            file = open(name,"r")
            content = file.read()
            print(content)
            file.close()
        else:
            print "檔案不存在!\n"

    elif choice == "2":
        exit = True
        print "\n謝謝您使用!\n"

def editFile():
    a




# -*- coding: utf-8 -*-

exit = False

while not exit:
    
    print "歡迎使用通訊錄管理系統!\n"
    print "*********************"
    print "請選擇功能:"
    print "1.開啟檔案"
    print "2.離開"
    print "*********************"
    choice = raw_input("選擇代號:")

    if choice == "1":
        name = raw_input("請輸入檔案名稱:")
        file = open(name,"r")
        content = file.read()
        print(content)
        file.close()

    elif choice == "2":
        exit = True
        print "\n謝謝您使用!\n"


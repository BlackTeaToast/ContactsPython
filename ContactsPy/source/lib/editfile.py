#coding=big5
from person import Person
from xmlfile import writeFile
                
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
        print "0.Exit"
        print "*********************"
        
        choice = raw_input("選擇代號: ")
        
        if choice == "1":
            view(persons)

        elif choice == "2":
            viewAll(persons)

        elif choice == "3":
            add(persons)

        elif choice == "4":
            remove(persons)

        elif choice == "5":
            save(fileName, persons)

        elif choice == "0":
            exit = True

        else:
            print "輸入錯誤! 請重新輸入!\n"

def add(persons):
    
    name = raw_input("請輸入名字: ")
    gender = raw_input("請輸入性別: ")
    phone = raw_input("請輸入電話: ")
    email = raw_input("請輸入Email: ")

    newPerson = Person(name, gender, phone, email)
    
    persons.append(newPerson)

    print "已新增聯絡人 " + name + " !\n"
                    
def remove(persons):
    
    name = raw_input("請輸入欲刪除的人名字: ")
    
    for person in persons:
        
        if person.name == name:
            persons.remove(person)
            print name + " 刪除成功!\n"
            return

    print "搜尋不到 " + name + "\n"

def view(persons):

    exit = False
    
    while not exit:

        print "*********************"
        print "請選擇View功能:"
        print "1.Search by name"
        print "2.Search by phone"
        print "3.Search by email"
        print "0.Exit"
        print "*********************"
        
        choice = raw_input("選擇代號: ")

        if choice == "1":
            searchByName(persons)

        elif choice == "2":
            searchByPhone(persons)

        elif choice == "3":
            searchByEmail(persons)

        elif choice == "0":
            exit = True

        else:
            print "輸入錯誤! 請重新輸入!\n"
        


def viewAll(persons):

    num = 0;
    
    for person in persons:

        print person
        num += 1

    print "共 " + str(num) + " 筆資料"
    print "ViewAll結束!\n"

def save(fileName, persons):
    
    writeFile(fileName, persons)
    print "儲存完成!\n"

def searchByName(persons):

    num = 0
    
    name = raw_input("請輸入搜尋名字: ")

    for person in persons:

        if name in person.name:

            print person
            num += 1

    if num == 0:

        print "未搜尋到任何相關 " + name

    else:

        print "共發現  " + str(num) + " 筆符合條件"

    print ""

def searchByPhone(persons):

    num = 0
    
    phone = raw_input("請輸入搜尋電話: ")

    for person in persons:

        if phone in person.phone:

            print person
            num += 1

    if num == 0:

        print "未搜尋到任何相關 " + phone

    else:

        print "共發現  " + str(num) + " 筆符合條件"

    print ""

def searchByEmail(persons):

    num = 0
    
    email = raw_input("請輸入搜尋Email: ")

    for person in persons:

        if email in person.email:

            print person
            num += 1

    if num == 0:

        print "未搜尋到任何相關 " + email

    else:

        print "共發現  " + str(num) + " 筆符合條件"

    print ""
    

#coding=big5
from person import Person
from xmlfile import writeFile
                
#define add
def add(persons):
    
    name = raw_input("請輸入名字: ")
    gender = raw_input("請輸入性別: ")
    phone = raw_input("請輸入電話: ")
    email = raw_input("請輸入Email: ")

    newPerson = Person(name, gender, phone, email)
    
    persons.append(newPerson)
                    
def remove(persons):
    
    name = raw_input("請輸入欲刪除的人名字: ")
    
    for person in persons:
        
        if person.name == name:
            persons.remove(person)
            print name + " 刪除成功!"
            return

    print "搜尋不到 " + name

def view(persons):

    choice = raw_input("請輸入代號:")


def viewAll(persons):

    for person in persons:

        print person

def save(fileName, persons):
    
    writeFile(fileName, persons)
    print "儲存完成!"


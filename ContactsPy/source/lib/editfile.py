#coding=big5
from person import Person
from xmlfile import writeFile
                
def editFile(fileName, persons):

    exit = False

    while not exit:
        
        print "�ثe�ϥ��ɮ�:" + fileName
        print "*********************"
        print "�п�ܥ\��:"
        print "1.View"
        print "2.View All"
        print "3.Add"
        print "4.Remove"
        print "5.Save"
        print "0.Exit"
        print "*********************"
        
        choice = raw_input("��ܥN��: ")
        
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
            print "��J���~! �Э��s��J!\n"

def add(persons):
    
    name = raw_input("�п�J�W�r: ")
    gender = raw_input("�п�J�ʧO: ")
    phone = raw_input("�п�J�q��: ")
    email = raw_input("�п�JEmail: ")

    newPerson = Person(name, gender, phone, email)
    
    persons.append(newPerson)

    print "�w�s�W�p���H " + name + " !\n"
                    
def remove(persons):
    
    name = raw_input("�п�J���R�����H�W�r: ")
    
    for person in persons:
        
        if person.name == name:
            persons.remove(person)
            print name + " �R�����\!\n"
            return

    print "�j�M���� " + name + "\n"

def view(persons):

    exit = False
    
    while not exit:

        print "*********************"
        print "�п��View�\��:"
        print "1.Search by name"
        print "2.Search by phone"
        print "3.Search by email"
        print "0.Exit"
        print "*********************"
        
        choice = raw_input("��ܥN��: ")

        if choice == "1":
            searchByName(persons)

        elif choice == "2":
            searchByPhone(persons)

        elif choice == "3":
            searchByEmail(persons)

        elif choice == "0":
            exit = True

        else:
            print "��J���~! �Э��s��J!\n"
        


def viewAll(persons):

    num = 0;
    
    for person in persons:

        print person
        num += 1

    print "�@ " + str(num) + " �����"
    print "ViewAll����!\n"

def save(fileName, persons):
    
    writeFile(fileName, persons)
    print "�x�s����!\n"

def searchByName(persons):

    num = 0
    
    name = raw_input("�п�J�j�M�W�r: ")

    for person in persons:

        if name in person.name:

            print person
            num += 1

    if num == 0:

        print "���j�M�������� " + name

    else:

        print "�@�o�{  " + str(num) + " ���ŦX����"

    print ""

def searchByPhone(persons):

    num = 0
    
    phone = raw_input("�п�J�j�M�q��: ")

    for person in persons:

        if phone in person.phone:

            print person
            num += 1

    if num == 0:

        print "���j�M�������� " + phone

    else:

        print "�@�o�{  " + str(num) + " ���ŦX����"

    print ""

def searchByEmail(persons):

    num = 0
    
    email = raw_input("�п�J�j�MEmail: ")

    for person in persons:

        if email in person.email:

            print person
            num += 1

    if num == 0:

        print "���j�M�������� " + email

    else:

        print "�@�o�{  " + str(num) + " ���ŦX����"

    print ""
    

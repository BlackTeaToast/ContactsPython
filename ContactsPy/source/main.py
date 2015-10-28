#coding=big5
import os
from lib.person import Person
from lib.xmlfile import writeFile, readFile
from lib.editfile import editFile, add, remove, view, viewAll, save
from xml.dom import minidom

def openFile():
    
    name = raw_input("�п�J�ɮצW��: ")
    
    if os.path.exists(name+".xml"):
        
        print (name + "�ɮצs�b!\n")
        persons = readFile(name)
        
        editFile(name, persons)

    else:
        
        print "�ɮפ��s�b!\n"

def creatFile():
    
    name = raw_input("�п�J�ɮצW��: ")
    
    if not os.path.exists(name+".xml"):

        file = open(name+".xml","w")
        print "�w�إ߷s�ɮ�" + name + "\n"
        file.close()
        
    else:
        print "�إߥ���!���P�W�ɮצs�b!\n"

def removeFile():

    name = raw_input("�п�J�������ɮצW��: ")
    
    if os.path.exists(name+".xml"):

        os.remove(name)
        print "�����ɮ� " + name + " ���\!\n"
        
    else:
        print "����!�ɮפ��s�b!\n"

# Main

exit = False

while not exit:
    
    print "�w��ϥγq�T���޲z�t��!"
    print "*********************"
    print "�п�ܥ\��:"
    print "1.�}���ɮ�"
    print "2.�إ߷s��"
    print "3.�����ɮ�"
    print "0.���}"
    print "*********************"
    choice = raw_input("��ܥN��: ")

    if choice == "1":
        openFile()

    elif choice == "2":
        creatFile()

    elif choice == "3":
        removeFile()

    elif choice == "0":
        exit = True

    else:
        print "��J���~! �Э��s��J!\n"

print "\n���±z�ϥ�!\n"

# Main End




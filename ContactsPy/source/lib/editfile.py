#coding=big5
from person import Person
from xmlfile import writeFile
                
#define add
def add(persons):
    
    name = raw_input("�п�J�W�r: ")
    gender = raw_input("�п�J�ʧO: ")
    phone = raw_input("�п�J�q��: ")
    email = raw_input("�п�JEmail: ")

    newPerson = Person(name, gender, phone, email)
    
    persons.append(newPerson)
                    
def remove(persons):
    
    name = raw_input("�п�J���R�����H�W�r: ")
    
    for person in persons:
        
        if person.name == name:
            persons.remove(person)
            print name + " �R�����\!"
            return

    print "�j�M���� " + name

def view(persons):

    choice = raw_input("�п�J�N��:")


def viewAll(persons):

    for person in persons:

        print person

def save(fileName, persons):
    
    writeFile(fileName, persons)
    print "�x�s����!"


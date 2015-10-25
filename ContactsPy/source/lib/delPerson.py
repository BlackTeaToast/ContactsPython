#coding:utf-8

from person import Person

def remove(persons):
    
    name = raw_input('Please Enter The Person You Want To Delete >>> ')
    
    for person in persons:
        
        if person.name == name:
            persons.remove(person)
            print 'Success DEL'
            return

    print "搜尋不到" + name


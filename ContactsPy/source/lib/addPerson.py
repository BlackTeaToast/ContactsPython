#coding=utf-8
from person import Person
                
#define add
def add(persons):
    
    name = raw_input("Please Enter Your name >>> ")
    gender = raw_input("Please Enter Your gender >>> ")
    phone = raw_input("Please Enter Your phone >>> ")
    email = raw_input("Please Enter Your E-mail >>> ")

    newPerson = Person(name, gender, phone, email)
    
    persons.append(newPerson)
                    

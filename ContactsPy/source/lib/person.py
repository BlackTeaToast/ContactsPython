#coding:big5

class Person:
    def __init__(self, name, gender, phone, email):
        self.name = name
        self.gender = gender
        self.phone = phone
        self.email = email;

    def __str__(self):
        return "�W�r:{0} �ʧO:{1} �q��:{2} Email:{3})".format(
            self.name, self.gender, self.phone, self.email)

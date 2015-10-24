class Person:
    def __init__(self, name, gender, phone, email):
        self.name = name
        self.gender = gender
        self.phone = phone
        self.email = email;

    def hello(self):
        print('Hello, ' + self.name)

    def __str__(self):
        return 'Person({0}, {1}, {2}, {3})'.format(
            self.name, self.gender, self.phone, self.email)

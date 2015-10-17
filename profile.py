#-*- coding: utf-8 -*-

class Profile:
    def __init__(self, name, subject, age, school, phone):
        self.name = name.encode('utf-8')
        self.subject = subject.encode('utf-8')
        self.age = age.encode('utf-8')
        self.school = school.encode('utf-8')
        self.phone = phone.encode('utf-8')

#-*- coding: utf-8 -*-

import MySQLdb

class DataBase():

    def __init__(self):
        self.connection = MySQLdb.connect('localhost', 'root', 'projectDanbi', 'orbi_message', charset='utf8', use_unicode=True)
        self.connection.autocommit(True)

    def execute(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)

        return cursor

    def put(self, profile):
        variables = "('{0}', '{1}', '{2}', '{3}', '{4}');".format(profile.name, profile.subject, profile.age, profile.school, profile.phone)
        query = "INSERT INTO `teachers`(`name`, `subject`, `age`, `school`, `phone`) VALUES " + variables
        self.execute(query).close()

#-*- coding: utf-8 -*-

import MySQLdb

class DataBase():

    def __init__(self):
        self.connection = MySQLdb.connect('localhost', 'root', 'projectDanbi', 'orbi_message')
        self.connection.autocommit(True)

    def execute(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)

        return cursor

    def put(self, name, phone):
        query = "INSERT INTO `teachers`(`name`, `phone`) VALUES ('{0}', '{1}');".format(name, phone)
        self.execute(query).close()

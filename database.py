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
        if self.is_exists(profile.phone):
            return

        variables = "('{0}', '{1}', '{2}', '{3}', '{4}');".format(profile.name, profile.subject, profile.age, profile.school, profile.phone)
        query = "INSERT INTO `teachers`(`name`, `subject`, `age`, `school`, `phone`) VALUES " + variables
        self.execute(query).close()

    def get_phone(self, id):
        query = "SELECT `phone` FROM `teachers` WHERE `id` = '{0}';".format(id)
        cursor = self.execute(query)
        result = cursor.fetchone()['phone']
        cursor.close()
        return result

    def is_exists(self, phone):
        query = "SELECT COUNT(*) AS count FROM `teachers` WHERE `phone` = '{0}';".format(phone)
        cursor = self.execute(query)
        result = cursor.fetchone()['count']
        cursor.close()
        return int(result) > 0

    def is_available(self, id):
        query = "SELECT `contact` FROM `teachers` WHERE `id` = '{0}';".format(id)
        cursor = self.execute(query)
        result = cursor.fetchone()['contact']
        cursor.close()
        return int(result) == 0

    def update_available(self, id):
        query = "UPDATE `teachers` SET `contact` = '1' WHERE `id` = '{0}';".format(id)
        cursor = self.execute(query).close()

    def get_count(self):
        query = "SELECT COUNT(*) AS count FROM `teachers`;"
        cursor = self.execute(query)
        result = cursor.fetchone()['count']
        cursor.close()
        return result

from db.db_helper import DBHelper

class Account(object):

    def __init__(self, username = '', password = ''):
        self.username = username
        self.password = password
        self.db = DBHelper()

    def create(self):
        self.db.create_account(self)

    def login(self):
        return self.db.login(self)

    def add_role(self, role):
        self.db.add_role(role)
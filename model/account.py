from db.db_helper import DBHelper
from value.strings import *

class Account(object):

    def __init__(self, username, password, status = 0):
        self.id = 0
        self.username = username
        self.password = password
        self.status = status
        self.db = DBHelper()

    def create(self):
        self.db.create_account(self)

    def login(self):
        if self.db.login(self):
            self.status = 1

    def list_role(self):
        roles = self.db.get_role(self)
        print(FMT_LIST_HEAD)
        if len(roles) == 0:
            print(STR_NO_ROLE)
        if len(roles) < 5:
            print(STR_ADD_ROLE)
        for i, role in enumerate(roles, 1):
            print(FMT_LIST_LINE)
            print(STR_LIST_ROLE % (i, role.name, role.career))
        print(FMT_LIST_HEAD)
        return roles

    def add_role(self, role):
        self.db.add_role(self, role)

    def __str__(self):
        return 'username: %s, password: %s, status: %s' % (self.username, self.password, self.status)
import sqlite3
from model import *

class DBHelper(object):

    def __init__(self):
        self.qn = sqlite3.connect('qiannv.db')
        '''
        新建表
        account: id int, username str, password str
        role: id int, account int, name str, school int 
        '''
        cursor = self.qn.cursor()
        cursor.execute("create table if not exists account (id integer primary key autoincrement, usr varchar(20), pwd varchar(50))")
        cursor.execute("create table if not exists role (id integer primary key autoincrement, account integer, name varchar(10), school integer)")
        cursor.close
        self.qn.close

    def create_account(self, account):
        '''
        创建账号
        :type account: Account
        '''
        cursor = self.qn.cursor()
        cursor.execute("insert into account (usr, pwd) values ('%s', '%s')" % (account.username, account.password))
        self.qn.commit()
        cursor.close
        self.qn.close

    def login(self, account):
        '''
        登录验证
        :type account: Account
        :rtype: bool
        '''
        cursor = self.qn.cursor()
        cursor.execute("select id from account where usr = '%s' and pwd = '%s'" % (account.username, account.password))
        result = False
        if cursor.rowcount == 1:
            result = True
        cursor.close
        self.qn.close
        return result

    def add_role(self, role):
        '''
        创建角色
        :type role: Role
        :rtype: int
        '''
        cursor = self.qn.cursor()
        cursor.execute("insert into role (account, name, school) values ('%s', '%s')" % (role.name, role.school))
        self.qn.commit()
        cursor.close
        self.qn.close
        pass


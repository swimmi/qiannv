import sqlite3
from model.role import Role

class DBHelper(object):

    def __init__(self):
        self.qn = sqlite3.connect('qiannv.db')
        self.qn.isolation_level = None
        '''
        account: id int, username str, password str, status bool
        role: id int, account int, name str, school int 
        '''
        cursor = self.qn.cursor()
        cursor.execute("create table if not exists account (id integer primary key autoincrement, usr varchar(20), pwd varchar(50), status integer default 0)")
        cursor.execute("create table if not exists role (id integer primary key autoincrement, account integer, name varchar(10), career integer)")
        cursor.close
        self.qn.close

    def create_account(self, account):
        '''
        :type account: Account
        '''
        cursor = self.qn.cursor()
        cursor.execute("insert into account (usr, pwd) values ('%s', '%s')" % (account.username, account.password))
        self.qn.commit()
        cursor.close
        self.qn.close

    def login(self, account):
        '''
        :type account: Account
        :rtype: bool
        '''
        cursor = self.qn.cursor()
        cursor.execute("select id from account where usr = '%s' and pwd = '%s'" % (account.username, account.password))
        res = cursor.fetchone()
        result = False
        if res is not None:
            result = True
        cursor.close
        self.qn.close
        return result

    def add_role(self, account, role):
        '''
        :type role: Role
        :rtype: int
        '''
        cursor = self.qn.cursor()
        cursor.execute("insert into role (account, name, career) values (%d, '%s', '%s')" % (account.id, role.name, role.career))
        self.qn.commit()
        cursor.close
        self.qn.close

    def get_role(self, account):
        '''
        :type account: Account
        :rtype: List[Role]
        '''
        cursor = self.qn.cursor()
        cursor.execute("select name, career from role where account = %d" % account.id)
        res = cursor.fetchall()
        roles = []
        for line in res:
            role = Role(line[0], line[1])
            roles.append(role)
        return roles

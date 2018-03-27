from model.account import Account
from model.role import Role
from model.equip import Equip
from value.strings import *

class Player(object):
    
    def __init__(self):
        self.act = Account('swimmi','52371314')
        self.act.create()

    def start_game(self):
        print(STR_WELCOME)

    def login_account(self):
        while True:
            self.act.username = input(STR_INPUT_USR)
            self.act.password = input(STR_INPUT_PWD)
            self.act.login()
            if self.act.status == 1:
                print(STR_LOGIN_SUCCESS % self.act.username)
                break
            else:
                print(STR_LOGIN_FAILED)

    def choose_role(self):
        roles = self.act.list_role()
        while 1:
            x = input(STR_CHOOSE % len(roles))
            try:
                i = int(x)
                if 0 <= i <= len(roles):
                    if i == 0:
                        name = input(STR_INPUT_NAME)
                        career = input(STR_INPUT_CAREER)
                        role = Role(name, career)
                        self.act.add_role(role)
                        self.choose_role()
                    else:
                        self.role = roles[i-1]
                    break
            except:
                pass

    def show_role(self):
        print(self.role)

    def wait_command(self):
        while 1:
            x = input(STR_MENU)
            i = int(x)
            if 0 <= i <= 9:
                if i == 0:
                    equip = Equip()
                    print(equip)
                    pass
                elif i == 1:
                    pass
                else:
                    pass
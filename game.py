from model.account import Account
from model.role import Role
from value.strings import *

'''
流程：
登录帐号
选择角色

'''

act = Account('swimmi','52371314')
act.create()

#登录帐号
def login_account():
    while True:
        act.username = input(STR_INPUT_USR)
        act.password = input(STR_INPUT_PWD)
        act.login()
        if act.status == 1:
            print(STR_LOGIN_SUCCESS % act.username)
            break
        else:
            print(STR_LOGIN_FAILED)
#选择角色
def choose_role():
    #显示已有角色
    roles = act.list_role()
    while 1:
        x = input(STR_CHOOSE % len(roles))
        try:
            i = int(x)
            
            if 0 <= i <= len(roles):
                if i == 0:
                    name = input(STR_INPUT_NAME)
                    career = input(STR_INPUT_CAREER)
                    role = Role(name, career)
                    act.add_role(role)
                else:
                    pass
                break
        except:
            pass

if __name__=="__main__":
    print(STR_WELCOME)
    login_account()
    choose_role()
    while 1:
        x = input()
        if x == '退出':
            break
from model.account import Account

'''
流程：
登录帐号
选择角色

'''

#登录帐号
def login_account():
    act = Account('swimmi','52371314')
    act.create()
    while True:
        act.username = input('请输入账号：')
        act.password = input('请输入密码：')
        try:
            act.login()
            print('登录成功，欢迎%s回来' % act.username)
            break
        except:
            print('登录失败，请重新输入')
#选择角色
def choose_role():
    pass

if __name__=="__main__":
    print('欢迎来到倩女幽魂')
    login_account()
    choose_role()
    while 1:
        x = input()
        if x == '退出':
            break
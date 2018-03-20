#encoding:utf-8

"""
编写登陆认证程序
基础需求：
让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序

升级需求：
可以支持多个用户登录 (提示，通过列表存多个账户信息)
用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）

用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写 '''
模式    描述
r    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb    以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+    打开一个文件用于读写。文件指针将会放在文件的开头。
rb+    以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb    以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+    打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+    以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+    打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""



#用户 密码
user_dict = {"caideyang":"123456","chengwanqing":"123","deyangcai":"111111"}
wrong_passwd_user_count = {"caideyang":0,"chengwanqing":0,"deyangcai":0}
insert_count = 0

#打开已经锁定用户名的文件
user_lock_file = open("user.lock","r+")
#锁定用户名列表
user_lock = user_lock_file.readlines()
def register(username):
    pass


def login():
    #全局变量
    global insert_count
    global wrong_passwd_user_count
    username = input("Pls. insert your name: ")
    passwd = input("Pls insert your password: ")
    #判断用户是否被锁定
    if username+"\n" in user_lock:
        print("The user [ %s ] you insert is locked ! " % username)
        user_lock_file.close()
        exit()
    #判断用户是否存在
    if username not in user_dict.keys():
        print("The user [ %s ] you insert is not exist !" % username)
        user_lock_file.close()
        exit()
    #判断用户名密码是否相符
    if user_dict[username] != passwd :
        print("Wrong password !Pls. Login again !")
        if wrong_passwd_user_count[username] < 3 or insert_count <3 :
            wrong_passwd_user_count[username] += 1
            insert_count += 1
            if wrong_passwd_user_count[username] == 3:
                user_lock_file.write(username+"\n")
                user_lock_file.flush()
                print("The user [ %s ] you insert is locked now ! " % username)
                user_lock_file.close()
                exit()
            if insert_count == 3 :
                print("Up to the count !")
                user_lock_file.close()
                exit()
            login()
    else:
        import time
        print("Login....")
        time.sleep(3)
        print("Login Successfully ! Welcome [ %s ] !" % username)
        user_lock_file.close()
        exit()
        


while __name__ == "__main__":
    login()
            
    


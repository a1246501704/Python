#!/usr/bin/env python
#_*_coding:utf-8_*_

import socketserver
import json
import configparser
import os
import hashlib
from conf import settings

STATUS_CODE = {
    250:"Invalid cmd format, e.g:{'action':'get','filename':'test.py','size':344}",
    251:"Invalid cmd",
    252:"Invalid auth data",
    253:"Wrong username or password",
    254:"Passed authentication",
    255:"filename doesn't provided",
    256:"File doesn't exist on server",
    257:"ready to send file",
    258:"md5 verification",
}

'''
250：“无效的cmd格式，例如：{'action'：'get'，'filename'：'test.py'，'size'：344}”，
251：“无效的CMD”，
252：“验证数据无效”，
253：“错误的用户名或密码”，
254：“通过身份验证”，
255：“文件名不提供”，
256：“服务器上不存在文件”，
257：“准备发送文件”，
258:“md5验证”,
'''

class FTPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        '''接收客户端消息（用户，密码，action）'''
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            # self.request.sendall(self.data.upper())

            if not self.data:
                print("client closed...")
                break
            data = json.loads(self.data.decode())  #接收客户端消息
            if data.get('action') is not None:  #action不为空
                print("---->", hasattr(self, "_auth"))
                if hasattr(self, "_%s" % data.get('action')): #客户端action 符合服务端action
                    func = getattr(self, "_%s" % data.get('action'))
                    func(data)
                else:  #客户端action 不符合服务端action
                    print("invalid cmd")
                    self.send_response(251)  # 251：“无效的CMD”
            else:  #客户端action 不正确
                print("invalid cmd format")
                self.send_response(250) # 250：“无效的cmd格式，例如：{'action'：'get'，'filename'：'test.py'，'size'：344}”

    def send_response(self,status_code,data=None):
        '''向客户端返回数据'''
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode())

    def _auth(self,*args,**kwargs):
        '''核对服务端 发来的用户，密码'''
        # print("---auth",args,kwargs)
        data = args[0]
        if data.get("username") is None or data.get("password") is None: #客户端的用户和密码有一个为空 则返回错误
            self.send_response(252)  # 252：“验证数据无效”

        user = self.authenticate(data.get("username"),data.get("password")) #把客户端的用户密码进行验证合法性
        if user is None: #客户端的数据为空 则返回错误
            self.send_response(253)  # 253：“错误的用户名或密码”
        else:
            print("password authentication",user)
            self.user = user
            self.send_response(254)  # 254：“通过身份验证”

    def authenticate(self,username,password):
        '''验证用户合法性，合法就返回数据，核对本地数据'''
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():  #用户匹配成功
            _password = config[username]["Password"]
            if _password == password:  #密码匹配成功
                print("pass auth..",username)
                config[username]["Username"] = username
                return config[username]

    def _put(self,*args,**kwargs):
        "client send file to server"
        data = args[0]
        base_filename = data.get('filename')
        file_obj = open(base_filename, 'wb')
        data = self.request.recv(4096)
        file_obj.write(data)
        file_obj.close()

    def _get(self,*args,**kwargs):
        '''get 下载方法'''
        data = args[0]
        if data.get('filename') is None:
            self.send_response(255)  # 255：“文件名不提供”，
        user_home_dir = "%s/%s" %(settings.USER_HOME,self.user["Username"]) #当前连接用户的目录
        file_abs_path = "%s/%s" %(user_home_dir,data.get('filename'))  #客户端发送过来的目录文件
        print("file abs path",file_abs_path)

        if os.path.isfile(file_abs_path):  #客户端目录文件名 存在服务端
            file_obj = open(file_abs_path,'rb')  # 用bytes模式打开文件
            file_size = os.path.getsize(file_abs_path)  #传输文件的大小
            self.send_response(257,data={'file_size':file_size}) #返回即将传输的文件大小 和状态码

            self.request.recv(1)  #等待客户端确认

            if data.get('md5'): #有 --md5 则传输时加上加密
                md5_obj = hashlib.md5()
                for line in file_obj:
                    self.request.send(line)
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    self.send_response(258,{'md5':md5_val})
                    print("send file done....")
            else:  #没有 --md5  直接传输文件
                for line in file_obj:
                    self.request.send(line)
                else:
                    file_obj.close()
                    print("send file done....")

        else:
            self.send_response(256) # 256：“服务器上不存在文件”=


    def _ls(self,*args,**kwargs):
        pass

    def _cd(self,*args,**kwargs):
        pass


if __name__ == '__main__':
    HOST, PORT = "127.0.0.1", 9999



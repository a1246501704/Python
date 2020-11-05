"""
根据URL中不同的路径返回不同的内容--函数版
"""

import socket

# 将返回不同的内容部分封装成函数
def f1(request):
    """
    处理用户请求，并返回相应的内容
    :param request: 用户请求的所有信息
    :return:
    """
    f = open('index.zhy','rb') # 以rb的方式读取index.zhy页面的内容
    data = f.read()
    f.close()
    return data

def f2(request):
    f = open('aricle.tpl','r',encoding='utf-8')
    data = f.read()
    f.close()
    import time
    ctime = time.time()
    data = data.replace('@@sw@@',str(ctime))  # 使数据变动，访问时刷新就变。html充当模版的角色，放点占位符替换即可。#在网页中定义好特殊符号，用动态的数据去替换提前定义好的特殊符号
    return bytes(data,encoding='utf-8')

def f3(request):
    import pymysql
    # create table userinfo(id int,name varchar(50),sex enum('male','female'),age int(3));
    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='db1')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,name,sex,age from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    content_list = []
    for row in user_list:
        tp = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" %(row['id'],row['name'],row['sex'],row['age'])
        content_list.append(tp)
    content = "".join(content_list) # 全部拼接到一起

    f = open('userlist.html','r',encoding='utf-8')
    template = f.read()
    f.close()

    # 模板渲染（模板+数据）
    data = template.replace('@@sadfasdfadf@@',content)
    return bytes(data,encoding='utf-8')

def f4(request):
    import pymysql

    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='db1')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,name,sex,age from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    f = open('hostlist.html','r',encoding='utf-8')
    data = f.read()
    f.close()

    # 基于第三方工具实现的模板渲染
    from jinja2 import Template
    template = Template(data)
    data = template.render(xxxxx=user_list,user='用户信息查询',name='用户信息列表') # xxxxx成为模版中被循环的数据对象，user被替换里面的{{user}}
    return data.encode('utf-8')

# 定义一个url和实际要执行的函数的对应关系
routers = [
    ('/xxx', f1),
    ('/ooo', f2),
    ('/userlist.html', f3),
    ('/host.html', f4),
]


def run():
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1',8080))
    sock.listen(5)

    while True:
        conn,addr = sock.accept() # hang住
        # 有人来连接了
        # 获取用户发送的数据
        data = conn.recv(8096)  # 接收客户端发来的消息
        data = str(data,encoding='utf-8') # 把收到的字节类型的数据转换成字符串
        headers,bodys = data.split('\r\n\r\n')
        temp_list = headers.split('\r\n')
        method,url,protocal = temp_list[0].split(' ')
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n") # 因为要遵循HTTP协议，所以回复的消息也要加状态行

        # 根据不同的路径返回不同内容，response是具体的响应体
        func_name = None # 定义一个保存将要执行的函数名的变量
        for item in routers:
            if item[0] == url:
                func_name = item[1]
                break

        if func_name:
            response = func_name(data)
        else:
            response = b"404"

        conn.send(response) # 返回具体的响应消息
        conn.close()

if __name__ == '__main__':
    run()
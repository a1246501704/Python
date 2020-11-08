from django.shortcuts import render,redirect
import pymysql
def classes(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='day65',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,title from class")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request,'classes.html',{'class_list': class_list}) # 将数据中填充到classes.html模版文件返回给浏览器，浏览器渲染后展示给给用户

def add_class(request):
    if request.method == "GET":
        return render(request,'add_class.html') # 展示添加页面给用户（第一次http请求）
    else:
        print(request.POST)
        v = request.POST.get('title') # 在响应体中获取add_class.html中定义的title，通过POST 提交上来的。（第二次http请求）
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='day65',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into class(title) values(%s)",[v,])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/') # 添加完成后再跳转到 urls.py 的/classes/路由（第三次http请求）

def del_class(request):
    nid = request.GET.get('nid') # 在响应体中获取clsses.html中定义并的nid（第一次http请求）

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='day65',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class where id=%s",[nid,])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/') # 删除完跳转到 /classes/路由（第二次http请求）

def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid') # 在响应体中获取中clsses.html中定义并的nid
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='day65',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class where id = %s",[nid,])
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        print(result) # 类型为字典的一行数据
        return render(request,'edit_class.html',{'result':result})
    else: # 点击“提交”时是POST请求
        nid = request.GET.get('nid') # 在请求头中获取nid
        # nid = request.POST.get('nid') # edit_class.html中另一种方法，在请求体中获取nid
        title = request.POST.get('title')

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='day65',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title=%s where id = %s",[title,nid,])
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/classes/')
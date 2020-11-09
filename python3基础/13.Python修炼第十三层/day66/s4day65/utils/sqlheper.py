import pymysql

def get_list(sql,args):
    '''
    查询所有数据
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='day65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_one(sql,args):
    '''
    查询一行数据
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='day65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def modify(sql,args):
    '''
    修改数据
    '''
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='day65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,args)
    conn.commit()
    cursor.close()
    conn.close()
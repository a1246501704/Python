#/usr/local/env python
#_*_coding:utf-8_*_

#第一部分：sql解析
import os
def sql_parse(sql): #用户输入sql 转成结构化的字典
    '''
    第一步：sql解析 流程
    1.收到 sql查询条件
    2.sql_parse 来分发要求给 select_parse
    3.select_parse 调用 handle_parse 解析sql
    4.handle_parse 返回解析sql后的结果 sql_dic 给 select_parse
    5.select_parse 把 sql_dic 返回给sql_parse
    sql_dic=sql_parse(sql) #用户输入sql 转成结构化的字典sql_dic
    sql语句四种操作格式：insert delete update select
    提取用户输入sql 的操作关键词 再进行分析和分发操作
    把sql字符串切分，提取命令信息，分发给具体解析函数去解析
    :param sql:用户输入的字符串
    :return:返回字典格式sql解析结果
    '''
    #sql命令操作 解析函数的字典  根据用户的命令来找相对应的函数
    parse_func={
        'insert':insert_parse,
        'delete':delete_parse,
        'update':update_parse,
        'select':select_parse,
    }

    #print('用户输入 sql str is : %s' %sql) #打印用户输入的sql
    sql_l=sql.split(' ') #按空格切割用户sql 成列表 方便提取命令信息
    func=sql_l[0] #取出用户的sql命令

    #判断用户输入的sql命令 是否在定义好的sql命令函数的字典里面,如果不在字典里面，则返回空
    res=''
    if func in parse_func:
        res=parse_func[func](sql_l) #把切割后的 用户sql的列表 传入对应的sql命令函数里

    return res

def insert_parse(sql_l):
    '''
    定义insert语句的语法结构，执行sql解析操作，返回sql_dic
    :param sql:sql按照空格分割的列表
    :return:返回字典格式的sql解析结果
    '''
    sql_dic={
        'func':insert, #函数名
        'insert':[],   #insert选项,留出扩展
        'into':[],     #表名
        'values':[],   #值
    }
    return handle_parse(sql_l,sql_dic)

def delete_parse(sql_l):
    '''
    定义delete语句的语法结构，执行sql解析操作，返回sql_dic
    :param sql:sql按照空格分割的列表
    :return:返回字典格式的sql解析结果
    '''
    sql_dic = {
        'func': delete,
        'delete': [],  # delete选项,留出扩展
        'from': [],  # 表名
        'where': [],  # filter条件
    }
    return handle_parse(sql_l, sql_dic)

def update_parse(sql_l):
    '''
    定义update语句的语法结构，执行sql解析操作，返回sql_dic
    :param sql:sql按照空格分割的列表
    :return:返回字典格式的sql解析结果
    '''
    sql_dic = {
        'func': update,
        'update': [],  # update选项,留出扩展
        'set': [],  # 修改的值
        'where': [],  # filter条件
    }
    return handle_parse(sql_l, sql_dic)

def select_parse(sql_l):
    '''
    定义select语句的语法结构，执行sql解析操作，返回sql_dic
    :param sql:sql按照空格分割的列表
    :return:返回字典格式的sql解析结果
    '''
    # print('from in the select_parse :\033[42;1m%s\033[0m' %sql_l)
    # select语句多种条件查询，列成字典，不同条件不同列表
    sql_dic={
        'func':select, #执行select语句
        'select':[], #查询字段
        'from':[],   #数据库.表
        'where':[],  #filter条件，怎么找
        'limit':[],  #limit条件，限制
    }
    return handle_parse(sql_l,sql_dic)

def handle_parse(sql_l,sql_dic): #专门做sql解析操作
    '''
    执行sql解析操作，返回sql_dic
    :param sql_l: sql按照空格分割的列表
    :param sql_dic: 待填充的字典
    :return: 返回字典格式的sql解析结果
    '''
    # print('sql_l is \033[41;1m%s\033[0m \nsql_dic is \033[41;1m%s\033[0m' %(sql_l,sql_dic))

    tag=False  #设置警报 默认是关闭False
    for item in sql_l:  #循环 按空格切割用户sql的列表
        if tag and item in sql_dic: #判断警报拉响是True 并且用户sql的条件 在条件select语句字典里面，则关闭警报
            tag=False #关闭警报
        if not tag and item in sql_dic: #判断警报没有拉响 并且用户sql的条件 在条件select语句字典里面
            tag=True #拉响警报
            key=item #取出用户sql的条件
            continue #跳出本次判断
        if tag: #判断报警拉响
            sql_dic[key].append(item) #把取出的用户sql 添加到 select语句多种条件对应的字典里
    if sql_dic.get('where'): #判断 用户sql where语句
        sql_dic['where']=where_parse(sql_dic.get('where')) #['id>4','and','id<10'] #调用where_parse函数 把整理好的用户sql的where语句 覆盖之前没整理好的
    # print('from in the handle_parse sql_dic is \033[43;1m%s\033[0m' %sql_dic)
    return sql_dic #返回 解析好的 用户sql 字典

def where_parse(where_l): #['id>','4','and','id','<10'] ---> #['id>4','and','id<10']
    '''
    分析用户sql where的各种条件，再拼成合理的条件字符串
    :param where_l:用户输入where后对应的过滤条件列表
    :return:
    '''
    res=[]  #存放最后整理好条件的列表
    key=['and','or','not']  #逻辑运算符
    char=''  #存放拼接时的字符串
    for i in where_l:  #循环用户sql
        if len(i) == 0 :continue  #判断 长度是0 就继续循环
        if i in key:
            #i为key当中存放的逻辑运算符
            if len(char) != 0:  #必须 char的长度大于0
                char=three_parse(char)  #把char字符串 转成列表的形式
                res.append(char)  #把之前char的字符串,加入res #char='id>4'--->char=['id','>','4']
                res.append(i)  #把用户sql 的逻辑运算符 加入res
                char=''  #清空 char ，为了下次加入char到res时 数据不重复
        else:
            char+=i  #'id>4' #除了逻辑运算符,都加入char #char='id<10'--->char=['id','>','4']
    else:
        char = three_parse(char)  # 把char字符串 转成列表的形式
        res.append(char)  #循环完成后 char里面有数据 ，再加入到res里面
    # ['id>4','and','id<10'] ---> #['id','>','4','and','id','<','10']
    # print('from in the where_parse res is \033[43;1m%s\033[0m' % res)
    return res  #返回整理好的 where语句列表

def three_parse(exp_str):  # 把where_parse函数里面 char的字符串 转成字典
    '''
    将每一个小的过滤条件如,name>=1转换成['name','>=','1']
    :param exp_str:条件表达式的字符串形式,例如'name>=1'
    :return:
    '''
    key=['>','<','=']  #区分运算符
    res=[]   #定义空列表 存放最终值
    char=''  #拼接 值的字符串
    opt=''   #拼接 运算符
    tag=False   #定义警报
    for i in exp_str:  #循环 字符串和运算符
        if i in key:  #判断 当是运算符时
            tag=True   #拉响警报
            if len(char) != 0:  #判断char的长度不等于0时(方便添加连续运算符)才做列表添加
                res.append(char)  #把拼接的字符串加入 res列表
                char=''   #清空char 使下次循环不重复添加数据到res列表
            opt+=i    #把循环的运算符加入opt
        if not tag:   #判断 警报没有拉响
            char+=i    #把循环的字符串加入 char

        if tag and i not in key: #判断 警报拉响(表示上次循环到运算符)，并且本次循环的不是运算符
            tag=False  #关闭警报
            res.append(opt)  #把opt里面的运算符 加入res列表
            opt=''  #清空opt 使下次循环不重复添加数据到res列表
            char+=i #把循环到的 字符串加入char
    else:
        res.append(char) #循环结束，把最后char的字符串加入res列表

    #新增解析 like的功能
    if len(res) == 1:  #判断 ['namelike李'] 是个整体
        res=res[0].split('like')  #以like切分字符串
        res.insert(1,'like')  #加入like字符串，因为上面切分的时候剔除了like

    # print('three_parse res is \033[43;1m%s\033[0m' % res)
    return res  #返回res列表结果

#第二部分：sql执行
def sql_action(sql_dic): #接收用户输入的sql 的结构化的字典  然后执行sql
    '''
    从字典sql_dic提取命令，分发给具体的命令执行函数去执行
    执行sql的统一接口,内部执行细节对用户完全透明
    :param sql_dic:
    :return:
    '''
    return sql_dic.get('func')(sql_dic) #接收用户sql，分发sql,执行命令

def insert(sql_dic):
    print('insert %s' %sql_dic)
    db,table=sql_dic.get('into')[0].split('.')  #切分文件路径，相对应数据库，表
    with open('%s/%s' %(db,table),'ab+') as fh:  #安装上面的路径 打开文件 ab+模式
        # 读出文件最后一行，赋值给last 配合+
        offs = -100  #
        while True:
            fh.seek(offs,2)
            lines = fh.readlines()
            if len(lines)>1:
                last = lines[-1]
                break
            offs *= 2
        last=last.decode(encoding='utf-8')

        last_id=int(last.split(',')[0])  #取出最后一行id号
        new_id=last_id+1   #id号加1 实现id自增效果
        #insert into db1.emp values alex,30,18500841678,运维,2007-8-1
        record=sql_dic.get('values')[0].split(',')   #提取用户想要 添加的sql
        record.insert(0,str(new_id))  #加入自增后的id 到用户sql的头部

        #['26','alex','35','13910015353','运维','2005 - 06 - 27\n']
        record_str=','.join(record)+'\n'  #把用户sql列表切成字符串
        fh.write(bytes(record_str,encoding='utf-8'))  #把添加 id后的用户想添加的sql  用bytes写入文件
        fh.flush()
    return [['insert successful']]

def delete(sql_dic):
    db,table=sql_dic.get('from')[0].split('.')
    bak_file=table+'_bak'
    with open("%s/%s" %(db,table),'r',encoding='utf-8') as r_file,\
            open('%s/%s' %(db,bak_file),'w',encoding='utf-8') as w_file:
        del_count=0
        for line in r_file:
            title="id,name,age,phone,dept,enroll_date"
            dic=dict(zip(title.split(','),line.split(',')))
            filter_res=logic_action(dic,sql_dic.get('where'))
            if not filter_res:
                w_file.write(line)
            else:
                del_count+=1
        w_file.flush()
    os.remove("%s/%s" % (db, table))
    os.rename("%s/%s" %(db,bak_file),"%s/%s" %(db,table))
    return [[del_count],['delete successful']]

def update(sql_dic):
    #update db1.emp set id='sb' where name like alex
    db,table=sql_dic.get('update')[0].split('.')
    set=sql_dic.get('set')[0].split(',')
    set_l=[]
    for i in set:
        set_l.append(i.split('='))
    bak_file=table+'_bak'
    with open("%s/%s" %(db,table),'r',encoding='utf-8') as r_file,\
            open('%s/%s' %(db,bak_file),'w',encoding='utf-8') as w_file:
        update_count=0
        for line in r_file:
            title="id,name,age,phone,dept,enroll_date"
            dic=dict(zip(title.split(','),line.split(',')))
            filter_res=logic_action(dic,sql_dic.get('where'))
            if filter_res:
                for i in set_l:
                    k=i[0]
                    v=i[-1].strip("'")
                    print('k v %s %s' %(k,v))
                    dic[k]=v
                print('change dic is %s ' %dic)
                line=[]
                for i in title.split(','):
                    line.append(dic[i])
                update_count+=1
                line=','.join(line)
            w_file.write(line)

        w_file.flush()
    os.remove("%s/%s" % (db, table))
    os.rename("%s/%s" %(db,bak_file),"%s/%s" %(db,table))
    return [[update_count],['update successful']]

def select(sql_dic):
    '''
    执行select语句，接收解析好的sql字典
    :param sql_dic:
    :return:
    '''
    # print('from select sql_dic is %s' %sql_dic) #打印 解析好的sql字典

    # first:form
    db,table=sql_dic.get('from')[0].split('.') #切分出库名和表名，就是文件路径

    fh=open("%s/%s" %(db,table),'r',encoding='utf-8') #打开文件 根据取到的路径

    #second:where
    filter_res=where_action(fh,sql_dic.get('where')) #定义where执行函数，查询条件
    fh.close()
    # for record in filter_res:  # 循环打印 用户sql where的执行结果
    #     print('file res is %s' %record)

    #third:limit
    limit_res=limit_action(filter_res,sql_dic.get('limit')) #定义limit执行函数,限制行数
    # for record in limit_res:  # 循环打印 显示用户sql limit的执行结果
    #     print('limit res is %s' %record)

    #lase:select
    search_res=search_action(limit_res,sql_dic.get('select'))  #定义select执行函数
    # for record in search_res:  # 循环打印 显示用户sql select的执行结果
    #     print('select res is %s' %record)

    return search_res

def where_action(fh,where_l):  #执行where条件语句  where_l=where的多条件解析后的列表
    #id,name,age,phone,dept,enroll_data
    #10,吴东杭,21,17710890829,运维,1995-08-29
    #['id>7', 'and', 'id<10', 'or', 'namelike']

    # print('in where_action \033[41;1m%s\033[0m' %where_l)
    res=[]  #定义最后返回值的列表
    logic_l=['and','or','not']   #定义逻辑运算符
    title="id,name,age,phone,dept,enroll_data"  #定义好表文件内容的标题
    if len(where_l) != 0:  #判断用户sql 是否有where语句
        for line in fh:  #循环 表文件
            dic=dict(zip(title.split(','),line.split(','))) #一条记录 让标题和文件内容一一对应
            #逻辑判断
            logic_res=logic_action(dic,where_l) #让 logic_action函数来操作对比
            if logic_res:  #如果逻辑判断为True
                res.append(line.split(','))  #加入res
    else:
        res=fh.readlines()  #用户sql 没有where语句，则返回表文件所有内容

    # print('>>>>>>>> %s' %res)
    return res #返回执行 where 后的结果

def logic_action(dic,where_l):
    '''
    用户sql select的where多条件 执行对比文件内容
    文件内容 跟所有的 where_l 的条件比较
    :param dic:
    :param where_l:
    :return:
    '''
    # print('from logic_action %s' %dic)  #from logic_action {'id': '23', 'name': '翟超群', 'age': '24', 'phone': '13120378203', 'dept': '运维', 'enroll_data': '2013-3-1\n'}
    # print('---- %s' %where_l)  #[['name', 'like', '李'], 'or', ['id', '<=', '4']]
    res=[]  #存放 bool值 结果的空列表
    # where_l=[['name', 'like', '李'], 'or', ['id', '<=', '4']]
    for exp in where_l:  #循环where条件列表，跟dic做比较
        #dic与exp做bool运算
        if type(exp) is list:  #只留下 where_l列表里 相关的条件
            #如果是列表 做bool运算  #[['name', 'like', '李']
            exp_k,opt,exp_v=exp  #匹配 一个where条件列表的格式
            if exp[1]  == '=':   #如果 列表的运算符是 =号
                opt="%s=" %exp[1]   #用字符串拼接出 两个 ==号
            if dic[exp_k].isdigit():  #判断是否数字  用户的条件是否对应文件内容(字典)
                dic_v=int(dic[exp_k])  #文件内容的数字 转成整形 做比较
                exp_v=int(exp_v)    #where_l列表的数字 转成整形 做比较
            else:
                dic_v="'%s'" %dic[exp_k]  #不是数字的时候 存取出来
            if opt != 'like':  #如果运算符 不是 like
                exp=str(eval("%s%s%s" %(dic_v,opt,exp_v))) #转成字符串(逻辑判断后是bool值)：做逻辑判断：文件数字，运算符，用户数字
            else:   #如果 运算符位置是 like
                if exp_v in dic_v:   #判断 sql里like的值 是否在 文件内容里
                    exp='True'
                else:
                    exp='False'
        res.append(exp)  #['True','or','False','or','true']

    # print('---------- %s' %res)
    res=eval(" ".join(res)) # 把bool值列表转成字符串 然后再做逻辑判断  结果是bool值
    return res  #返回 res结果

def limit_action(filter_res,limit_l): #执行limit条件 限制行数
    res=[]  #最后的返回值列表
    if len(limit_l) != 0:  #判断 用户sql 是否有 limit条件
        index=int(limit_l[0])   #取出 用户sql limit条件的数字
        res=filter_res[0:index]
    else:  #如果 用户sql 没有 limit条件 就整个返回
        res=filter_res
    return res  #返回最后的sql结果

def search_action(limit_res,select_l):  #执行select执行函数
    res=[]   #最后的返回值列表
    fileds_l = []
    title = "id,name,age,phone,dept,enroll_data"   #title = select的条件
    if select_l[0] == '*' :   #判断 如果 用户sql 的select 条件是 *
        fields_l=title.split(',')   #用户sql 的select 条件是 * ,则匹配所有条件
        res=limit_res   #如果 用户sql 的select 条件是 * 则返回全部
    else:   #判断 如果用户sql的select条件不是 * ，提取用户的select语句条件
        for record in limit_res:   #循环 匹配好的where语句和limit语句的结果
            dic=dict(zip(title.split(','),record))   #每条记录都对应 select条件，生成字典
            r_l=[]   #存放用户sql的select条件
            fields_l=select_l[0].split(',')  #取出用户sql 的select条件
            for i in fields_l:   #循环用户sql的select条件，区分多条件，id,name
                r_l.append(dic[i].strip())  #把用户sql的select多条件 加入 r_l列表
            res.append(r_l)   #把r_l列表 加入res

    return (fields_l,res)  #返回用户sql的select条件，selcet执行结果


if __name__ == '__main__':  #程序主函数
    while True:
        sql=input("sql> ").strip()  #用户输入sql
        if sql == 'exit':break      #exit 随时退出
        if len(sql) == 0 :continue  #用户如果输入空，继续输入

        sql_dic=sql_parse(sql) #用户输入sql 转成结构化的字典sql_dic

        #print('main res is %s' %sql_dic) #打印用户非法输入
        if len(sql_dic) == 0:continue  #如果用户输入等于0 不执行sql_action 让用户继续输入sql

        res=sql_action(sql_dic) #用户执行sql之后的结果res
        print('\033[43;1m%s\033[0m' %res[0])  #打印 select的条件
        for i in res[-1]:  # 循环打印 显示用户sql select的执行结果
            print(i)

'''
测试执行 select语句
select * from db1.emp
select * from db1.emp limit 3
select * from db1.emp where name like 李 or id <= 4 or id = 24 limit 4
select id,name from db1.emp where name like 李 or id <= 4 or id = 24 limit 4

测试执行 insert语句
insert into db1.emp values alex,30,18500841678,运维,2007-8-1

测试执行 delete语句
delete from db1.emp where id>47

测试执行 update语句
update db1.emp set alex='haha' where id=47
'''




\一 介绍
MySQL数据操作： DML

========================================================

在MySQL管理软件中，可以通过SQL语句中的DML语言来实现数据的操作，包括

使用INSERT实现数据的插入
使用UPDATE实现数据的更新
使用DELETE实现数据的删除
使用SELECT查询数据以及。
========================================================

本节内容包括：
  插入数据
  更新数据
  删除数据
  查询数据

\二 插入数据INSERT
1. 插入完整数据（顺序插入）
    语法一：
    INSERT INTO 表名(字段1,字段2,字段3…字段n) VALUES(值1,值2,值3…值n);

    语法二：
    INSERT INTO 表名 VALUES (值1,值2,值3…值n);

2. 指定字段插入数据
    语法：
    INSERT INTO 表名(字段1,字段2,字段3…) VALUES (值1,值2,值3…);

3. 插入多条记录
    语法：
    INSERT INTO 表名 VALUES
        (值1,值2,值3…值n),
        (值1,值2,值3…值n),
        (值1,值2,值3…值n);
        
4. 插入查询结果
    语法：
    INSERT INTO 表名(字段1,字段2,字段3…字段n) 
                    SELECT (字段1,字段2,字段3…字段n) FROM 表2
                    WHERE …;

\三 更新数据UPDATE
语法：
    UPDATE 表名 SET
        字段1=值1,
        字段2=值2,
        WHERE CONDITION;

示例：
    UPDATE mysql.user SET password=password(‘123’) where user=’root’ and host=’localhost’;

\四 删除数据DELETE
语法：
    DELETE FROM 表名 WHERE CONITION;

示例：
    DELETE FROM mysql.user WHERE password=’’;

练习：
    更新MySQL root用户密码为mysql123
    删除除从本地登录的root用户以外的所有用户

\五 查询数据SELECT
6.1 单表查询：http://www.cnblogs.com/linhaifeng/articles/7267592.html
6.2 多表查询：http://www.cnblogs.com/linhaifeng/articles/7267596.html


\六 权限管理
#授权表
user         #该表放行的权限，针对：所有数据，所有库下所有表，以及表下的所有字段
db           #该表放行的权限，针对：某一数据库，该数据库下的所有表，以及表下的所有字段
tables_priv  #该表放行的权限。针对：某一张表，以及该表下的所有字段
columns_priv #该表放行的权限，针对：某一个字段

#按图解释：
# mysql安装完以后默认有个mysql库下面的这几张表就是控制权限的。
user：放行db1，db2及其包含的所有
db：  放行db1，及其db1包含的所有
tables_priv:  放行db1.table1，及其该表包含的所有
columns_prive:放行db1.table1.column1，只放行该字段


## 权限相关操作
#创建用户
create user 'egon'@'1.1.1.1' identified by '123';
create user 'egon'@'192.168.1.%' identified by '123';
create user 'egon'@'%' identified by '123';
# 查看MYSQL数据库中所有用户
mysql> # SELECT DISTINCT CONCAT('User: ''',user,'''@''',host,''';') AS query FROM mysql.user;

#授权：对文件夹，对文件，对文件某一字段的权限
查看帮助：help grant
常用权限有：select,update,alter,delete
all可以代表除了grant之外的所有权限

#针对所有库的授权:*.*
grant select on *.* to 'egon1'@'localhost' identified by '123'; #只在user表中可以查到egon1用户的select权限被设置为Y

#针对某一数据库：db1.*
grant select on db1.* to 'egon2'@'%' identified by '123';       #只在db表中可以查到egon2用户的select权限被设置为Y

#针对某一个表：db1.t4
grant select on db1.t3 to 'egon3'@'%' identified by '123';      #只在tables_priv表中可以查到egon3用户的select权限

#针对某一个字段：
mysql> create table t3(id int primary key auto_increment,name varchar(20),age int not null);
mysql> insert into t3 values(1,'egon1',18),(2,'egon2',19),(3,'egon3',29);
mysql> select * from t3;
+------+-------+------+
| id   | name  | age  |
+------+-------+------+
|    1 | egon1 |   18 |
|    2 | egon2 |   19 |
|    3 | egon3 |   29 |
+------+-------+------+

mysql> grant select (id,name),update (age) on db1.t3 to 'egon4'@'localhost' identified by '123'; 

mysql -uegon4 -p123
mysql> select id,name  from t3;
+----+-------+
| id | name  |
+----+-------+
|  1 | egon1 |
|  2 | egon2 |
|  3 | egon3 |
+----+-------+
3 rows in set (0.00 sec)
mysql> select * from t3;
ERROR 1142 (42000): SELECT command denied to user 'egon4'@'localhost' for table 't3'


#可以在tables_priv和columns_priv中看到相应的权限
mysql> select * from tables_priv where user='egon4'\G
*************************** 1. row ***************************
       Host: localhost
         Db: db1
       User: egon4
 Table_name: t3
    Grantor: root@localhost
  Timestamp: 0000-00-00 00:00:00
 Table_priv:
Column_priv: Select,Update
row in set (0.00 sec)

mysql> select * from columns_priv where user='egon4'\G
*************************** 1. row ***************************
       Host: localhost
         Db: db1
       User: egon4
 Table_name: t3
Column_name: id
  Timestamp: 0000-00-00 00:00:00
Column_priv: Select
*************************** 2. row ***************************
       Host: localhost
         Db: db1
       User: egon4
 Table_name: t3
Column_name: name
  Timestamp: 0000-00-00 00:00:00
Column_priv: Select
*************************** 3. row ***************************
       Host: localhost
         Db: db1
       User: egon4
 Table_name: t3
Column_name: age
  Timestamp: 0000-00-00 00:00:00
Column_priv: Update
rows in set (0.00 sec)

\刷新权限
flush privileges;



\MySQL 赋予用户权限命令的简单格式可概括为：
grant 权限 on 数据库对象 to 用户

# 一、grant 普通数据用户，查询、插入、更新、删除 数据库中所有表数据的权利。
grant select on testdb.* to common_user@'%'
grant insert on testdb.* to common_user@'%'
grant update on testdb.* to common_user@'%'
grant delete on testdb.* to common_user@'%'

或者，用一条 MySQL 命令来替代：
grant select, insert, update, delete on testdb.* to common_user@'%'

# 二、grant 数据库开发人员，创建表、索引、视图、存储过程、函数。。。等权限。
grant 创建、修改、删除 MySQL 数据表结构权限。
grant create on testdb.* to developer@'192.168.0.%';
grant alter on testdb.* to developer@'192.168.0.%';
grant drop on testdb.* to developer@'192.168.0.%';

grant 操作 MySQL 外键权限。
grant references on testdb.* to developer@'192.168.0.%';

grant 操作 MySQL 临时表权限。
grant create temporary tables on testdb.* to developer@'192.168.0.%';

grant 操作 MySQL 索引权限。
grant index on testdb.* to developer@'192.168.0.%';

grant 操作 MySQL 视图、查看视图源代码 权限。
grant create view on testdb.* to developer@'192.168.0.%';
grant show view on testdb.* to developer@'192.168.0.%';

grant 操作 MySQL 存储过程、函数 权限。
grant create routine on testdb.* to developer@'192.168.0.%'; #  now, can show procedure status
grant alter routine on testdb.* to developer@'192.168.0.%';  #  now, you can drop a procedure
grant execute on testdb.* to developer@'192.168.0.%';

# 三、grant 普通 DBA 管理某个 MySQL 数据库的权限。
grant all privileges on testdb to dba@'localhost'
其中，关键字 “privileges” 可以省略。

# 四、grant 高级 DBA 管理 MySQL 中所有数据库的权限。
grant all on *.* to dba@'localhost'

# 五、MySQL grant 权限，分别可以作用在多个层次上。
1. grant 作用在整个 MySQL 服务器上：
grant select on *.* to dba@localhost; # dba 可以查询 MySQL 中所有数据库中的表。
grant all on *.* to dba@localhost;    # dba 可以管理 MySQL 中的所有数据库

2. grant 作用在单个数据库上：
grant select on testdb.* to dba@localhost; # dba 可以查询 testdb 中的表。

3. grant 作用在单个数据表上：
grant select, insert, update, delete on testdb.orders to dba@localhost;

这里在给一个用户授权多张表时，可以多次执行以上语句。例如：
grant select(user_id,username) on smp.users to mo_user@'%' identified by '123345';
grant select on smp.mo_sms to mo_user@'%' identified by '123345';

4. grant 作用在表中的列上：
grant select(id, se, rank) on testdb.apache_log to dba@localhost;

5. grant 作用在存储过程、函数上：
grant execute on procedure testdb.pr_add to 'dba'@'localhost'
grant execute on function testdb.fn_add to 'dba'@'localhost'

# 六、查看 MySQL 用户权限
查看当前用户（自己）权限：
show grants;

查看其他 MySQL 用户权限：
show grants for dba@localhost;

# 七、撤销已经赋予给 MySQL 用户权限的权限。
revoke 跟 grant 的语法差不多，只需要把关键字 “to” 换成 “from” 即可：
grant all on *.* to dba@localhost;
revoke all on *.* from dba@localhost;
revoke select on db1.* from 'egon'@'%';

# 八、MySQL grant、revoke 用户权限注意事项
1. grant, revoke 用户权限后，该用户只有重新连接 MySQL 数据库，权限才能生效。
2. 如果想让授权的用户，也可以将这些权限 grant 给其他用户，需要选项 “grant option“
grant select on testdb.* to dba@localhost with grant option;
这个特性一般用不到。实际中，数据库权限最好由 DBA 来统一管理。

\刷新权限
flush privileges;
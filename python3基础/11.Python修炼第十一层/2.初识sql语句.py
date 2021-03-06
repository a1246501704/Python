有了mysql这个数据库软件，就可以将程序员从对数据的管理中解脱出来，专注于对程序逻辑的编写
mysql服务端软件即mysqld帮我们管理好文件夹以及文件，前提是作为使用者的我们，需要下载mysql的客户端，或者其他模块来连接到mysqld，然后使用mysql软件规定的语法格式去提交自己命令，
实现对文件夹或文件的管理。该语法即sql（Structured Query Language 即结构化查询语言）


SQL语言主要用于存取数据、查询数据、更新数据和管理关系数据库系统,SQL语言由IBM开发。SQL语言分为3种类型：
DDL（Data Definition Languages）语句  
    # 数据定义语言，这些语句定义了不同的数据段、数据库、表、列、索引等数据库对象的定义。常用的语句关键字主要包括 create、drop、alter等。
DML（Data Manipulation Language）语句 
    # 数据操纵语句，用于添加、删除、更新和查询数据库记录，并检查数据完整性，常用的语句关键字主要包括 insert、delete、udpate 和select 等。(增添改查）
DCL（Data Control Language）语句      
    # 数据控制语句，用于控制不同数据段直接的许可和访问级别的语句。这些语句定义了数据库、表、字段、用户的访问权限和安全级别。主要的语句关键字包括 grant、revoke 等。

#1. 操作文件夹（库）
    增：create database db1 charset utf8;
    查：show databases;
    改：alter database db1 charset gbk;  # 库名无法修改
    删除: drop database db1;


#2. 操作文件（表）
先切换到文件夹下：use db1
    增：create table t1(id int,name char);
    查：show tables
        show create table t1;  # 查看t1表的详细信息
        desc t1;               # 查看t1表的表结构
    改：alter table t1 modify name char(3);
       alter table t1 change name name1 char(2);
    删：drop table t1;
    

#3. 操作文件中的内容/记录
    增：insert into t1 values(1,'egon1'),(2,'egon2'),(3,'egon3');
    查：select * from t1;
    改：update t1 set name='sb' where id=2;  # 也可以 where id >1  
    删：delete from t1 where id=1;           # 也可以 where name  = 'sb'

    清空表：
        delete from t1;    # 如果有自增id，新增的数据，仍然是以删除前的最后一样作为起始。
        truncate table t1; # 数据量大，删除速度比上一条快，且直接从零开始，
        auto_increment 表示：自增
        primary key 表示：约束（不能重复且不能为空）；加速查找




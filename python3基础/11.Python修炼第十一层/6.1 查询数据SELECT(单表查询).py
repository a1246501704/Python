\五 查询数据SELECT
\一、单表查询的语法顺序
SELECT  distinct 字段1,字段2... FROM 库名.表名
                  WHERE 条件
                  GROUP BY 
                  HAVING 筛选
                  ORDER BY field
                  LIMIT 限制条数

\二、关键字的执行优先级(重点)
# 重点中的重点：关键字的执行优先级
from
where    # 过滤条件 
group by # 分组依据
having   # 过滤条件
select   # 查询
distinct # 去重复
order by # 排序的字段
limit    # 显示显示的条数

1.找到表:from
2.拿着where指定的约束条件，去文件/表中取出一条条记录
3.将取出的一条条记录进行分组group by，如果没有group by，则整体作为一组
4.将分组的结果进行having过滤
5.执行select
6.去重
7.将结果按条件排序：order by
8.限制结果的显示条数 详细见：http://www.cnblogs.com/linhaifeng/articles/7372774.html

\三、简单查询
准备表和记录:
employee表
    员工id      id                  int             
    姓名        emp_name            varchar
    性别        sex                 enum
    年龄        age                 int
    入职日期     hire_date           date
    岗位        post                varchar
    职位描述     post_comment        varchar
    薪水        salary              double


# 创建表:
mysql> create table employee(
id int not null unique auto_increment,
name varchar(20) not null,
sex enum('male','female') not null default 'male', #大部分是男的
age int(3) unsigned not null default 28,
hire_date date not null,
post varchar(50),
post_comment varchar(100),
salary double(15,2),
);


# 查看表结构:
mysql> desc employee;
+--------------+-----------------------+------+-----+---------+----------------+
| Field        | Type                  | Null | Key | Default | Extra          |
+--------------+-----------------------+------+-----+---------+----------------+
| id           | int(11)               | NO   | PRI | NULL    | auto_increment |
| name         | varchar(20)           | NO   |     | NULL    |                |
| sex          | enum('male','female') | NO   |     | male    |                |
| age          | int(3) unsigned       | NO   |     | 28      |                |
| hire_date    | date                  | NO   |     | NULL    |                |
| post         | varchar(50)           | YES  |     | NULL    |                |
| post_comment | varchar(100)          | YES  |     | NULL    |                |
| salary       | double(15,2)          | YES  |     | NULL    |                |
+--------------+-----------------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)

# 插入记录:
    三个部门：教学，销售，运营
mysql> insert into employee(name,sex,age,hire_date,post,salary) values
('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33), #以下是教学部
('alex','male',78,'20150302','teacher',1000000.31),
('wupeiqi','male',81,'20130305','teacher',8300),
('yuanhao','male',73,'20140701','teacher',3500),
('liwenzhou','male',28,'20121101','teacher',2100),
('jingliyang','female',18,'20110211','teacher',9000),
('jinxin','male',18,'19000301','teacher',30000),
('成龙','male',48,'20101111','teacher',10000),

('歪歪','female',48,'20150311','sale',3000.13),#以下是销售部门
('丫丫','female',38,'20101101','sale',2000.35),
('丁丁','female',18,'20110312','sale',1000.37),
('星星','female',18,'20160513','sale',3000.29),
('格格','female',28,'20170127','sale',4000.33),

('张野','male',28,'20160311','operation',10000.13), #以下是运营部门
('程咬金','male',18,'19970312','operation',20000),
('程咬银','female',18,'20130311','operation',19000),
('程咬铜','male',18,'20150411','operation',18000),
('程咬铁','female',18,'20140512','operation',17000)
;
mysql> select * from employee;
+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+
| id | name       | sex    | age | hire_date  | post                                    | post_comment | salary     |
+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+
|  1 | egon       | male   |  18 | 2017-03-01 | 老男孩驻沙河办事处外交大使                   | NULL         |    7300.33 |
|  2 | alex       | male   |  78 | 2015-03-02 | teacher                                 | NULL         | 1000000.31 |
|  3 | wupeiqi    | male   |  81 | 2013-03-05 | teacher                                 | NULL         |    8300.00 |
|  4 | yuanhao    | male   |  73 | 2014-07-01 | teacher                                 | NULL         |    3500.00 |
|  5 | liwenzhou  | male   |  28 | 2012-11-01 | teacher                                 | NULL         |    2100.00 |
|  6 | jingliyang | female |  18 | 2011-02-11 | teacher                                 | NULL         |    9000.00 |
|  7 | jinxin     | male   |  18 | 1900-03-01 | teacher                                 | NULL         |   30000.00 |
|  8 | 成龙       | male   |  48 | 2010-11-11 | teacher                                 | NULL         |   10000.00 |
|  9 | 歪歪       | female |  48 | 2015-03-11 | sale                                    | NULL         |    3000.13 |
| 10 | 丫丫       | female |  38 | 2010-11-01 | sale                                    | NULL         |    2000.35 |
| 11 | 丁丁       | female |  18 | 2011-03-12 | sale                                    | NULL         |    1000.37 |
| 12 | 星星       | female |  18 | 2016-05-13 | sale                                    | NULL         |    3000.29 |
| 13 | 格格       | female |  28 | 2017-01-27 | sale                                    | NULL         |    4000.33 |
| 14 | 张野       | male   |  28 | 2016-03-11 | operation                               | NULL         |   10000.13 |
| 15 | 程咬金     | male   |  18 | 1997-03-12 | operation                               | NULL         |   20000.00 |
| 16 | 程咬银     | female |  18 | 2013-03-11 | operation                               | NULL         |   19000.00 |
| 17 | 程咬铜     | male   |  18 | 2015-04-11 | operation                               | NULL         |   18000.00 |
| 18 | 程咬铁     | female |  18 | 2014-05-12 | operation                               | NULL         |   17000.00 |
+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+
18 rows in set (0.00 sec)

# 简单查询:
    查询全部
        SELECT * FROM employee;
    指定字段查询
        SELECT id,name,sex,age,hire_date,post,post_comment,salary FROM employee;
        SELECT name,salary FROM employee;

\DISTINCT（记录去重）
mysql> SELECT DISTINCT post FROM employee;  
+-----------------------------------------+
| post                                    |
+-----------------------------------------+
| 老男孩驻沙河办事处外交大使              |
| teacher                                 |
| sale                                    |
| operation                               |
+-----------------------------------------+
4 rows in set (0.00 sec)

\通过四则运算查询:
# 将salary字段计算
mysql> SELECT name, salary*12 FROM employee;
+------------+-------------+
| name       | salary*12   |
+------------+-------------+
| egon       |    87603.96 |
| alex       | 12000003.72 |
| wupeiqi    |    99600.00 |
| yuanhao    |    42000.00 |
| liwenzhou  |    25200.00 |
| jingliyang |   108000.00 |
| jinxin     |   360000.00 |
| 成龙       |   120000.00 |
| 歪歪       |    36001.56 |
| 丫丫       |    24004.20 |
| 丁丁       |    12004.44 |
| 星星       |    36003.48 |
| 格格       |    48003.96 |
| 张野       |   120001.56 |
| 程咬金     |   240000.00 |
| 程咬银     |   228000.00 |
| 程咬铜     |   216000.00 |
| 程咬铁     |   204000.00 |
+------------+-------------+
18 rows in set (0.00 sec)
# 将salary字段计算后输出重命名
mysql> SELECT name, salary*12 AS Annual_salary FROM employee;
+------------+---------------+
| name       | Annual_salary |
+------------+---------------+
| egon       |      87603.96 |
| alex       |   12000003.72 |
| wupeiqi    |      99600.00 |
| yuanhao    |      42000.00 |
| liwenzhou  |      25200.00 |
| jingliyang |     108000.00 |
| jinxin     |     360000.00 |
| 成龙       |     120000.00 |
| 歪歪       |      36001.56 |
| 丫丫       |      24004.20 |
| 丁丁       |      12004.44 |
| 星星       |      36003.48 |
| 格格       |      48003.96 |
| 张野       |     120001.56 |
| 程咬金     |     240000.00 |
| 程咬银     |     228000.00 |
| 程咬铜     |     216000.00 |
| 程咬铁     |     204000.00 |
+------------+---------------+
18 rows in set (0.00 sec)
mysql> SELECT name as NAME, salary*12 AS Annual_salary FROM employee;
mysql> SELECT name, salary*12 Annual_salary FROM employee;

\定义显示格式: CONCAT() 函数用于连接字符串
mysql> SELECT CONCAT('姓名: ',name,'  年薪: ', salary*12)  AS Annual_salary FROM employee;
+---------------------------------------+
| Annual_salary                         |
+---------------------------------------+
| 姓名: egon  年薪: 87603.96            |
| 姓名: alex  年薪: 12000003.72         |
| 姓名: wupeiqi  年薪: 99600.00         |
| 姓名: yuanhao  年薪: 42000.00         |
| 姓名: liwenzhou  年薪: 25200.00       |
| 姓名: jingliyang  年薪: 108000.00     |
| 姓名: jinxin  年薪: 360000.00         |
| 姓名: 成龙  年薪: 120000.00           |
| 姓名: 歪歪  年薪: 36001.56            |
| 姓名: 丫丫  年薪: 24004.20            |
| 姓名: 丁丁  年薪: 12004.44            |
| 姓名: 星星  年薪: 36003.48            |
| 姓名: 格格  年薪: 48003.96            |
| 姓名: 张野  年薪: 120001.56           |
| 姓名: 程咬金  年薪: 240000.00         |
| 姓名: 程咬银  年薪: 228000.00         |
| 姓名: 程咬铜  年薪: 216000.00         |
| 姓名: 程咬铁  年薪: 204000.00         |
+---------------------------------------+
18 rows in set (0.00 sec)

mysql> SELECT CONCAT('姓名: ',name) as new_name,CONCAT('  年薪: ', salary*12)  as new_salary FROM employee;
+--------------------+-----------------------+
| new_name           | new_salary            |
+--------------------+-----------------------+
| 姓名: egon         |   年薪: 87603.96      |
| 姓名: alex         |   年薪: 12000003.72   |
| 姓名: wupeiqi      |   年薪: 99600.00      |
| 姓名: yuanhao      |   年薪: 42000.00      |
| 姓名: liwenzhou    |   年薪: 25200.00      |
| 姓名: jingliyang   |   年薪: 108000.00     |
| 姓名: jinxin       |   年薪: 360000.00     |
| 姓名: 成龙         |   年薪: 120000.00     |
| 姓名: 歪歪         |   年薪: 36001.56      |
| 姓名: 丫丫         |   年薪: 24004.20      |
| 姓名: 丁丁         |   年薪: 12004.44      |
| 姓名: 星星         |   年薪: 36003.48      |
| 姓名: 格格         |   年薪: 48003.96      |
| 姓名: 张野         |   年薪: 120001.56     |
| 姓名: 程咬金       |   年薪: 240000.00     |
| 姓名: 程咬银       |   年薪: 228000.00     |
| 姓名: 程咬铜       |   年薪: 216000.00     |
| 姓名: 程咬铁       |   年薪: 204000.00     |
+--------------------+-----------------------+
18 rows in set (0.00 sec)

mysql> select concat(name,":",age) from employee;
+----------------------+
| concat(name,":",age) |
+----------------------+
| egon:18              |
| alex:78              |
| wupeiqi:81           |
| yuanhao:73           |
| liwenzhou:28         |
| jingliyang:18        |
| jinxin:18            |
| 成龙:48              |
| 歪歪:48              |
| 丫丫:38              |
| 丁丁:18              |
| 星星:18              |
| 格格:28              |
| 张野:28              |
| 程咬金:18            |
| 程咬银:18            |
| 程咬铜:18            |
| 程咬铁:18            |
+----------------------+
18 rows in set (0.00 sec)

\CONCAT_WS() 第一个参数为分隔符
mysql> SELECT CONCAT_WS(':',name,salary*12)  AS Annual_salary FROM employee;
+----------------------+
| Annual_salary        |
+----------------------+
| egon:87603.96        |
| alex:12000003.72     |
| wupeiqi:99600.00     |
| yuanhao:42000.00     |
| liwenzhou:25200.00   |
| jingliyang:108000.00 |
| jinxin:360000.00     |
| 成龙:120000.00       |
| 歪歪:36001.56        |
| 丫丫:24004.20        |
| 丁丁:12004.44        |
| 星星:36003.48        |
| 格格:48003.96        |
| 张野:120001.56       |
| 程咬金:240000.00     |
| 程咬银:228000.00     |
| 程咬铜:216000.00     |
| 程咬铁:204000.00     |
+----------------------+
18 rows in set (0.00 sec)

\结合CASE语句
   SELECT (
           CASE
           WHEN NAME = 'egon' THEN
               NAME
           WHEN NAME = 'alex' THEN
               CONCAT(name,'_BIGSB')
           ELSE
               concat(NAME, 'SB')
           END
       ) as new_name
   FROM  employee;
+--------------+
| new_name     |
+--------------+
| egon         |
| alex_BIGSB   |
| wupeiqiSB    |
| yuanhaoSB    |
| liwenzhouSB  |
| jingliyangSB |
| jinxinSB     |
| 成龙SB       |
| 歪歪SB       |
| 丫丫SB       |
| 丁丁SB       |
| 星星SB       |
| 格格SB       |
| 张野SB       |
| 程咬金SB     |
| 程咬银SB     |
| 程咬铜SB     |
| 程咬铁SB     |
+--------------+
18 rows in set (0.00 sec)


# 小练习：
1 查出所有员工的名字，薪资,格式为
    <名字:egon>    <薪资:3000>
2 查出所有的岗位（去掉重复）
3 查出所有员工名字，以及他们的年薪,年薪的字段名为annual_year

select concat('<名字:',name,'>    ','<薪资:',salary,'>') from employee;
select distinct depart_id from employee;
select name,salary*12 annual_year from employee;


\四、WHERE约束
# 用于分组前过滤

where字句中可以使用：

1. 比较运算符：> < >= <= <> !=
2. between 80 and 100 ，80到100之间。
3. in(80,90,100) 值是10或20或30
4. like 'egon%'
    pattern可以是%或_，
    %表示任意多字符
    _表示一个字符
5. 逻辑运算符：在多个条件直接可以使用逻辑运算符 and or not

# 单条件查询
    SELECT name FROM employee WHERE post='sale';
        
# 多条件查询
    SELECT name,salary FROM employee WHERE post='teacher' AND salary>10000;

# 关键字BETWEEN AND(表示大于等于10000 小于等于20000，也就是10000和20000之间的。)
    SELECT name,salary FROM employee WHERE salary BETWEEN 10000 AND 20000;

    SELECT name,salary FROM employee  WHERE salary NOT BETWEEN 10000 AND 20000;
    
# 关键字IS NULL(判断某个字段是否为NULL不能用等号，需要用IS)
    SELECT name,post_comment FROM employee WHERE post_comment IS NULL;

    SELECT name,post_comment FROM employee WHERE post_comment IS NOT NULL;
        
    SELECT name,post_comment FROM employee WHERE post_comment=''; 
    注意''是空字符串，不是null
    ps：
        执行
        update employee set post_comment='' where id=2;
        再用上条查看，就会有结果了

# 关键字IN集合查询
    SELECT name,salary FROM employee  WHERE salary=3000 OR salary=3500 OR salary=4000 OR salary=9000;
    SELECT name,salary FROM employee  WHERE salary IN (3000,3500,4000,9000);
    SELECT name,salary FROM employee  WHERE salary NOT IN (3000,3500,4000,9000);

# 关键字LIKE模糊查询
    通配符’%’：任意多个字符
    SELECT * FROM employee WHERE name LIKE 'eg%';

    通配符’_’：任意一个字符
    SELECT * FROM employee WHERE name LIKE 'al__';

# 小练习：
1. 查看岗位是teacher的员工姓名、年龄
2. 查看岗位是teacher且年龄大于30岁的员工姓名、年龄
3. 查看岗位是teacher且薪资在9000-1000范围内的员工姓名、年龄、薪资
4. 查看岗位描述不为NULL的员工信息
5. 查看岗位是teacher且薪资是10000或9000或30000的员工姓名、年龄、薪资
6. 查看岗位是teacher且薪资不是10000或9000或30000的员工姓名、年龄、薪资
7. 查看岗位是teacher且名字是jin开头的员工姓名、年薪

select name,age from employee where post = 'teacher';
select name,age from employee where post='teacher' and age > 30; 
select name,age,salary from employee where post='teacher' and salary between 9000 and 10000;
select * from employee where post_comment is not null;
select name,age,salary from employee where post='teacher' and salary in (10000,9000,30000);
select name,age,salary from employee where post='teacher' and salary not in (10000,9000,30000);
select name,salary*12 from employee where post='teacher' and name like 'jin%';


\五、分组查询:GROUP BY
一 什么是分组？为什么要分组？
#1、首先明确一点：分组发生在where之后，即分组是基于where之后得到的记录而进行的
#2、分组指的是：将所有记录按照某个相同字段进行归类，比如针对员工信息表的职位分组，或者按照性别进行分组等
#3、为何要分组呢？
    取每个部门的最高工资
    取每个部门的员工数
    取男人数和女人数

小窍门：‘每’这个字后面的字段，就是我们分组的依据

#4、大前提：
    可以按照任意字段分组，但是分组完毕后，比如group by post，只能查看post字段，如果想查看组内信息，需要借助于聚合函数.

二 ONLY_FULL_GROUP_BY
#查看MySQL 5.7默认的sql_mode如下：
mysql> select @@global.sql_mode;
+------------------------+
| @@global.sql_mode      |
+------------------------+
| NO_ENGINE_SUBSTITUTION |
+------------------------+
1 row in set (0.00 sec)

ONLY_FULL_GROUP_BY
STRICT_TRANS_TABLES
NO_ZERO_IN_DATE
NO_ZERO_DATE
ERROR_FOR_DIVISION_BY_ZERO
NO_AUTO_CREATE_USER
NO_ENGINE_SUBSTITUTION

#！！！注意
ONLY_FULL_GROUP_BY的语义就是确定select target list中的所有列的值都是明确语义，简单的说来，
在ONLY_FULL_GROUP_BY模式下，target list中的值要么是来自于聚集函数的结果，要么是来自于group by list中的表达式的值。

#设置sql_mole如下操作(我们可以去掉ONLY_FULL_GROUP_BY模式)：
mysql> set global sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';

mysql> select @@global.sql_mode;
+-------------------+
| @@global.sql_mode |
+-------------------+
|                   |
+-------------------+
row in set (0.00 sec)

mysql> select * from employee group by post; 
+----+------+--------+-----+------------+----------------------------+--------------+------------+
| id | name | sex    | age | hire_date  | post                       | post_comment | salary     | 
+----+------+--------+-----+------------+----------------------------+--------------+------------+
| 14 | 张野 | male   |  28 | 2016-03-11 | operation                  | NULL         |   10000.13 |
|  9 | 歪歪 | female |  48 | 2015-03-11 | sale                       | NULL         |    3000.13 |
|  2 | alex | male   |  78 | 2015-03-02 | teacher                    | NULL         | 1000000.31 |
|  1 | egon | male   |  18 | 2017-03-01 | 老男孩驻沙河办事处外交大使     | NULL         |    7300.33 |
+----+------+--------+-----+------------+----------------------------+--------------+------------+
rows in set (0.00 sec)


#由于没有设置ONLY_FULL_GROUP_BY,于是也可以有结果，默认都是组内的第一条记录，但其实这是没有意义的

mysql> set global sql_mode='ONLY_FULL_GROUP_BY';
Query OK, 0 rows affected (0.00 sec)

mysql> quit #设置成功后，一定要退出，然后重新登录方可生效
Bye

mysql> use db1;
Database changed
mysql> select * from emp group by post; #报错
ERROR 1055 (42000): 'db1.emp.id' isn't in GROUP BY
mysql> select post,count(id) from employee group by post; #只能查看分组依据和使用聚合函数
+----------------------------+-----------+
| post                       | count(id) |
+----------------------------+-----------+
| operation                  |         5 |
| sale                       |         5 |
| teacher                    |         7 |
| 老男孩驻沙河办事处外交大使     |         1 |
+----------------------------+-----------+
rows in set (0.00 sec)

# 聚合函数
max # 最大
    select post,max(salary) from employee group by post; # 取出组内 最大的工资
min # 最小
    select post,max(salary) from employee group by post;
avg # 平均值
    select post,avg(salary) from employee group by post;
sum # 综合
    select post,sum(salary) from employee group by post;
count # 统计个数
    select post,count(id) from employee group by post; # 统计每个部门的人数


三 GROUP BY
# 单独使用GROUP BY关键字分组
    SELECT post FROM employee GROUP BY post;
    注意：我们按照post字段分组，那么select查询的字段只能是post，想要获取组内的其他相关信息，需要借助函数

# GROUP BY关键字和GROUP_CONCAT()函数一起使用
    SELECT post,GROUP_CONCAT(name) FROM employee GROUP BY post; # 按照岗位分组，并查看组内成员名
    SELECT post,GROUP_CONCAT(name) as emp_members FROM employee GROUP BY post;

# GROUP BY与聚合函数一起使用
    select post,count(id) as count from employee group by post; # 按照岗位分组，并查看每个组有多少人

# 强调：
    如果我们用unique的字段作为分组的依据，则每一条记录自成一组，这种分组没有意义
    多条记录之间的某个字段值相同，该字段通常用来作为分组的依据
    where不能使用聚合函数

四 聚合函数
#强调：聚合函数聚合的是组的内容，若是没有分组，则默认一组

示例：
    SELECT COUNT(*) FROM employee;
    SELECT COUNT(*) FROM employee WHERE depart_id=1;
    SELECT MAX(salary) FROM employee;
    SELECT MIN(salary) FROM employee;
    SELECT AVG(salary) FROM employee;
    SELECT SUM(salary) FROM employee;
    SELECT SUM(salary) FROM employee WHERE depart_id=3;

五 小练习：
1. 查询岗位名以及岗位包含的所有员工名字
2. 查询岗位名以及各岗位内包含的员工个数
3. 查询公司内男员工和女员工的个数
4. 查询岗位名以及各岗位的平均薪资
5. 查询岗位名以及各岗位的最高薪资
6. 查询岗位名以及各岗位的最低薪资
7. 查询男员工与男员工的平均薪资，女员工与女员工的平均薪资

# 题1：分组
mysql> select post,group_concat(name) from employee group by post;
+-----------------------------------------+---------------------------------------------------------+
| post                                    | group_concat(name)                                      |
+-----------------------------------------+---------------------------------------------------------+
| operation                               | 张野,程咬金,程咬银,程咬铜,程咬铁                        |
| sale                                    | 歪歪,丫丫,丁丁,星星,格格                                |
| teacher                                 | alex,wupeiqi,yuanhao,liwenzhou,jingliyang,jinxin,成龙   |
| 老男孩驻沙河办事处外交大使                  | egon                                                    |
+-----------------------------------------+---------------------------------------------------------+


# 题目2：
mysql> select post,count(id) from employee group by post;
+-----------------------------------------+-----------+
| post                                    | count(id) |
+-----------------------------------------+-----------+
| operation                               |         5 |
| sale                                    |         5 |
| teacher                                 |         7 |
| 老男孩驻沙河办事处外交大使              |         1 |
+-----------------------------------------+-----------+


# 题目3：
mysql> select sex,count(id) from employee group by sex;
+--------+-----------+
| sex    | count(id) |
+--------+-----------+
| male   |        10 |
| female |         8 |
+--------+-----------+

# 题目4：
mysql> select post,avg(salary) from employee group by post;
+-----------------------------------------+---------------+
| post                                    | avg(salary)   |
+-----------------------------------------+---------------+
| operation                               |  16800.026000 |
| sale                                    |   2600.294000 |
| teacher                                 | 151842.901429 |
| 老男孩驻沙河办事处外交大使              |   7300.330000 |
+-----------------------------------------+---------------+

# 题目5
mysql> select post,max(salary) from employee group by post;
+-----------------------------------------+-------------+
| post                                    | max(salary) |
+-----------------------------------------+-------------+
| operation                               |    20000.00 |
| sale                                    |     4000.33 |
| teacher                                 |  1000000.31 |
| 老男孩驻沙河办事处外交大使              |     7300.33 |
+-----------------------------------------+-------------+

# 题目6
mysql> select post,min(salary) from employee group by post;
+-----------------------------------------+-------------+
| post                                    | min(salary) |
+-----------------------------------------+-------------+
| operation                               |    10000.13 |
| sale                                    |     1000.37 |
| teacher                                 |     2100.00 |
| 老男孩驻沙河办事处外交大使              |     7300.33 |
+-----------------------------------------+-------------+

# 题目七
mysql> select sex,avg(salary) from e p m group by sex;
+--------+---------------+
| sex    | avg(salary)   |
+--------+---------------+
| male   | 110920.077000 |
| female |   7250.183750 |
+--------+---------------+


\六、HAVING过滤
# 用于分组之后进行过滤，即在分组之后专门针对聚合的结果进行筛选。
HAVING与WHERE不一样的地方在于!!!!!!
#！！！执行优先级从高到低：where > group by > having 
#1. Where 发生在分组group by之前进行过滤，因而Where中可以有任意字段，但是绝对不能使用聚合函数。
#2. Having发生在分组group by之后进行过滤，因而Having中可以使用分组的字段，无法直接取到其他字段,可以使用聚合函数

# 验证:
mysql> select @@sql_mode;
+--------------------+
| @@sql_mode         |
+--------------------+
| ONLY_FULL_GROUP_BY |
+--------------------+
row in set (0.00 sec)

mysql> select * from employee where salary > 100000;
+----+------+------+-----+------------+---------+--------------+------------+
| id | name | sex  | age | hire_date  | post    | post_comment | salary     |
+----+------+------+-----+------------+---------+--------------+------------+
|  2 | alex | male |  78 | 2015-03-02 | teacher | NULL         | 1000000.31 |
+----+------+------+-----+------------+---------+--------------+------------+
row in set (0.00 sec)

mysql> select * from employee having salary > 100000;
ERROR 1463 (42000): Non-grouping field 'salary' is used in HAVING clause

mysql> select post,group_concat(name) from employee group by post having salary > 10000; #错误，分组后无法直接取到salary字段
ERROR 1054 (42S22): Unknown column 'salary' in 'having clause'

mysql> select post,group_concat(name) from employee group by post having avg(salary) > 10000;
+-----------+-------------------------------------------------------+
| post | group_concat(name)                                         |
+-----------+-------------------------------------------------------+
| operation | 程咬铁,程咬铜,程咬银,程咬金,张野                          |
| teacher   | 成龙,jinxin,jingliyang,liwenzhou,yuanhao,wupeiqi,alex |
+-----------+-------------------------------------------------------+
rows in set (0.00 sec)


# 小练习：
1. 查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
3. 查询各岗位平均薪资大于10000的岗位名、平均工资
4. 查询各岗位平均薪资大于10000且小于20000的岗位名、平均工资
#题1：
mysql> select post,group_concat(name),count(id) from employee group by post having count(id) < 2;
+-----------------------------------------+--------------------+-----------+
| post                                    | group_concat(name) | count(id) |
+-----------------------------------------+--------------------+-----------+
| 老男孩驻沙河办事处外交大使                   | egon               |         1 |
+-----------------------------------------+--------------------+-----------+

#题目2：
mysql> select post,avg(salary) from employee group by post having avg(salary) > 10000;
+-----------+---------------+
| post      | avg(salary)   |
+-----------+---------------+
| operation |  16800.026000 |
| teacher   | 151842.901429 |
+-----------+---------------+

#题目3：
mysql> select post,avg(salary) from employee group by post having avg(salary) > 10000 and avg(salary) <20000;
+-----------+--------------+
| post      | avg(salary)  |
+-----------+--------------+
| operation | 16800.026000 |
+-----------+--------------+

\七、查询排序:ORDER BY
# order by时已经分完组了，可以使用聚合函数。


# 按单列排序
    SELECT * FROM employee;
    SELECT * FROM employee ORDER BY salary; # 默认是升序（从小到大）
    SELECT * FROM employee ORDER BY salary ASC; # 升序
    SELECT * FROM employee ORDER BY salary DESC;# 降序（从大到小）

# 按多列排序:先按照age排序，如果年纪相同，则按照薪资降序排序
    SELECT * from employee ORDER BY age,salary DESC; 

# 小练习：
1. 查询所有员工信息，先按照age升序排序，如果age相同则按照hire_date降序排序
2. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资升序排列
3. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资降序排列

#题目1
mysql> select * from employee ORDER BY age asc,hire_date desc;

#题目2
mysql> select post,avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) asc;
+-----------+---------------+
| post      | avg(salary)   |
+-----------+---------------+
| operation |  16800.026000 |
| teacher   | 151842.901429 |
+-----------+---------------+

#题目3
mysql> select post,avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) desc;
+-----------+---------------+
| post      | avg(salary)   |
+-----------+---------------+
| teacher   | 151842.901429 |
| operation |  16800.026000 |
+-----------+---------------+



\八、限制查询的记录数:LIMIT
# 语法角度和执行顺序都是排在最后使用


# 示例：
    SELECT * FROM employee ORDER BY salary DESC LIMIT 3;   # 默认初始位置为0 
    SELECT * FROM employee ORDER BY salary DESC LIMIT 0,5; # 从第0开始，即先查询出第一条，然后包含这一条在内往后查5条
    SELECT * FROM employee ORDER BY salary DESC LIMIT 5,5; # 从第5开始，即先查询出第6条，然后包含这一条在内往后查5条

# 小练习：
1. 分页显示，每页5条
mysql> select * from  employee limit 0,5; # 从0 开始往后取5条
+----+-----------+------+-----+------------+-----------------------------------------+--------------+------------+
| id | name      | sex  | age | hire_date  | post                                    | post_comment | salary     |
+----+-----------+------+-----+------------+-----------------------------------------+--------------+------------+
|  1 | egon      | male |  18 | 2017-03-01 | 老男孩驻沙河办事处外交大使                   | NULL         |    7300.33 |
|  2 | alex      | male |  78 | 2015-03-02 | teacher                                 | NULL         | 1000000.31 |
|  3 | wupeiqi   | male |  81 | 2013-03-05 | teacher                                 | NULL         |    8300.00 |
|  4 | yuanhao   | male |  73 | 2014-07-01 | teacher                                 | NULL         |    3500.00 |
|  5 | liwenzhou | male |  28 | 2012-11-01 | teacher                                 | NULL         |    2100.00 |
+----+-----------+------+-----+------------+-----------------------------------------+--------------+------------+
rows in set (0.00 sec)

mysql> select * from  employee limit 5,5; # 从5 开始往后取5条
+----+------------+--------+-----+------------+---------+--------------+----------+
| id | name       | sex    | age | hire_date  | post    | post_comment | salary   |
+----+------------+--------+-----+------------+---------+--------------+----------+
|  6 | jingliyang | female |  18 | 2011-02-11 | teacher | NULL         |  9000.00 |
|  7 | jinxin     | male   |  18 | 1900-03-01 | teacher | NULL         | 30000.00 |
|  8 | 成龙       | male   |  48 | 2010-11-11 | teacher | NULL         | 10000.00 |
|  9 | 歪歪       | female |  48 | 2015-03-11 | sale    | NULL         |  3000.13 |
| 10 | 丫丫       | female |  38 | 2010-11-01 | sale    | NULL         |  2000.35 |
+----+------------+--------+-----+------------+---------+--------------+----------+
rows in set (0.00 sec)

mysql> select * from  employee limit 10,5; # 从10 开始往后取5条
+----+-----------+--------+-----+------------+-----------+--------------+----------+
| id | name      | sex    | age | hire_date  | post      | post_comment | salary   |
+----+-----------+--------+-----+------------+-----------+--------------+----------+
| 11 | 丁丁      | female |  18 | 2011-03-12 | sale      | NULL         |  1000.37 |
| 12 | 星星      | female |  18 | 2016-05-13 | sale      | NULL         |  3000.29 |
| 13 | 格格      | female |  28 | 2017-01-27 | sale      | NULL         |  4000.33 |
| 14 | 张野      | male   |  28 | 2016-03-11 | operation | NULL         | 10000.13 |
| 15 | 程咬金    | male   |  18 | 1997-03-12 | operation | NULL         | 20000.00 |
+----+-----------+--------+-----+------------+-----------+--------------+----------+
rows in set (0.00 sec)

\九、使用正则表达式查询：regexp
# 比like更灵活

SELECT * FROM employee WHERE name REGEXP '^ale';  # 以ale开头
SELECT * FROM employee WHERE name REGEXP 'on$';   # 以on结尾的
SELECT * FROM employee WHERE name REGEXP 'm{2}';  # 

# 小结：对字符串匹配的方式
WHERE name = 'egon';
WHERE name LIKE 'yua%';
WHERE name REGEXP 'on$';

# 小练习：
查看所有员工中名字是jin开头，n或者g结尾的员工信息
select * from employee where name regexp '^jin.*[gn]$';
select * from employee where name regexp '^jin.*(g|n)$';

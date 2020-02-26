
\一 介绍
存储引擎决定了表的类型，而表内存放的数据也要有不同的类型，每种数据类型都有自己的宽度，但宽度是可选的

详细参考：
http://www.runoob.com/mysql/mysql-data-types.html
http://dev.mysql.com/doc/refman/5.7/en/data-type-overview.html

\mysql常用数据类型概览
#1. 数字：
    整型：tinyinit  int  bigint
    小数：
        float ：在位数比较短的情况下不精准
        double ：在位数比较长的情况下不精准
            0.000001230123123123
            存成：0.000001230000

        decimal：（如果用小数，则用推荐使用decimal）
            精准
            内部原理是以字符串形式去存

#2. 字符串：
    char（10）：简单粗暴，浪费空间，存取速度快
        root存成root000000
    varchar：精准，节省空间，存取速度慢

    sql优化：创建表时，定长的类型往前放，变长的往后放
            比如性别           比如地址或描述信息

    >255个字符，超了就把文件路径存放到数据库中。
            比如图片，视频等找一个文件服务器，数据库中只存路径或url。

#3. 时间类型：
    最常用：datetime

#4. 枚举类型与集合类型



\二 数值类型
# 1、整数类型
整数类型：TINYINT SMALLINT MEDIUMINT INT BIGINT（详情见图）
作用：存储年龄，等级，id，各种号码等
========================================
        tinyint[(m)] [unsigned] [zerofill]

            小整数，数据类型用于保存一些范围的整数数值范围：
            有符号：
                -128 ～ 127
            无符号：
                ～ 255

            PS： MySQL中无布尔值，使用tinyint(1)构造。

========================================
        int[(m)][unsigned][zerofill]

            整数，数据类型用于保存一些范围的整数数值范围：
            有符号：
                -2147483648 ～ 2147483647
            无符号：
                ～ 4294967295

========================================
        bigint[(m)][unsigned][zerofill]
            大整数，数据类型用于保存一些范围的整数数值范围：
            有符号：
                -9223372036854775808 ～ 9223372036854775807
            无符号：
                ～  18446744073709551615

# 验证
# =========有符号和无符号tinyint==========
#tinyint默认为有符号
MariaDB [db1]> create table t1(x tinyint); #默认为有符号，即数字前有正负号。x为字段名。
MariaDB [db1]> desc t1;
MariaDB [db1]> insert into t1 values
    -> (-129),
    -> (-128),
    -> (127),
    -> (128);
MariaDB [db1]> select * from t1;
+------+
| x    |
+------+
| -128 | #-129存成了-128
| -128 | #有符号，最小值为-128
|  127 | #有符号，最大值127
|  127 | #128存成了127
+------+

#设置无符号tinyint
MariaDB [db1]> create table t2(x tinyint unsigned);
MariaDB [db1]> insert into t2 values
    -> (-1),
    -> (0),
    -> (255),
    -> (256);
MariaDB [db1]> select * from t2;
+------+
| x    |
+------+
|    0 | -1存成了0
|    0 | #无符号，最小值为0
|  255 | #无符号，最大值为255
|  255 | #256存成了255
+------+

# ============有符号和无符号int=============
#int默认为有符号
MariaDB [db1]> create table t3(x int); # 默认为有符号整数
MariaDB [db1]> insert into t3 values
    -> (-2147483649),
    -> (-2147483648),
    -> (2147483647),
    -> (2147483648);
MariaDB [db1]> select * from t3;
+-------------+
| x           |
+-------------+
| -2147483648 | #-2147483649存成了-2147483648
| -2147483648 | #有符号，最小值为-2147483648
|  2147483647 | #有符号，最大值为2147483647
|  2147483647 | #2147483648存成了2147483647
+-------------+

#设置无符号int
MariaDB [db1]> create table t4(x int unsigned);
MariaDB [db1]> insert into t4 values
    -> (-1),
    -> (0),
    -> (4294967295),
    -> (4294967296);
MariaDB [db1]> select * from t4;
+------------+
| x          |
+------------+
|          0 | #-1存成了0
|          0 | #无符号，最小值为0
| 4294967295 | #无符号，最大值为4294967295
| 4294967295 | #4294967296存成了4294967295
+------------+

# ==============有符号和无符号bigint=============
MariaDB [db1]> create table t6(x bigint);
MariaDB [db1]> insert into t5 values  
    -> (-9223372036854775809),
    -> (-9223372036854775808),
    -> (9223372036854775807),
    -> (9223372036854775808);

MariaDB [db1]> select * from t5;
+----------------------+
| x                    |
+----------------------+
| -9223372036854775808 |
| -9223372036854775808 |
|  9223372036854775807 |
|  9223372036854775807 |
+----------------------+

MariaDB [db1]> create table t6(x bigint unsigned);
MariaDB [db1]> insert into t6 values  
    -> (-1),
    -> (0),
    -> (18446744073709551615),
    -> (18446744073709551616);

MariaDB [db1]> select * from t6;
+----------------------+
| x                    |
+----------------------+
|                    0 |
|                    0 |
| 18446744073709551615 |
| 18446744073709551615 |
+----------------------+

# ======用zerofill测试整数类型的显示宽度=============
MariaDB [db1]> create table t7(x int(3) zerofill);
MariaDB [db1]> insert into t7 values
    -> (1),
    -> (11),
    -> (111),
    -> (1111);
MariaDB [db1]> select * from t7;
+------+
| x    |
+------+
|  001 |
|  011 |
|  111 |
| 1111 | # 超过宽度限制仍然可以存
+------+

注意：为该类型指定宽度时，仅仅只是指定查询结果的显示宽度，与存储范围无关，存储范围如下
其实我们完全没必要为整数类型指定显示宽度，使用默认的就可以了。默认的显示宽度，都是在最大值的基础上加1

(见 数据类型图)

int的存储宽度是4个Bytes，即32个bit，即2**32
无符号最大值为：4294967296-1
有符号最大值：2147483648-1
有符号和无符号的最大数字需要的显示宽度均为10，而针对有符号的最小值则需要11位才能显示完全，所以int类型默认的显示宽度为11是非常合理的
最后：整形类型，其实没有必要指定显示宽度，使用默认的就ok

# 2、浮点型
定点数类型  DEC等同于DECIMAL　　
浮点类型：FLOAT、DOUBLE
区别：三种类型的区别是精度不一样,DECIMAL精度最高。
作用：存储薪资、身高、体重、体质参数等
======================================
#FLOAT[(M,D)] [UNSIGNED] [ZEROFILL]

定义：
    单精度浮点数（非准确小数值），M是数字总个数，最大值为255。D是小数点后个数，最大值为30。整数占225个。

有符号：
    -3.402823466E+38 to -1.175494351E-38,
    1.175494351E-38 to 3.402823466E+38
无符号：
    1.175494351E-38 to 3.402823466E+38

精确度： 
    **** 随着小数的增多，精度变得不准确 ****

======================================
#DOUBLE[(M,D)] [UNSIGNED] [ZEROFILL]

定义：
    双精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。m最大值为255，d最大值为30

有符号：
    -1.7976931348623157E+308 to -2.2250738585072014E-308
    2.2250738585072014E-308 to 1.7976931348623157E+308

无符号：
    2.2250738585072014E-308 to 1.7976931348623157E+308
            
精确度：
    ****随着小数的增多，精度比float要高，但也会变得不准确 ****

======================================
# decimal[(m[,d])] [unsigned] [zerofill]

定义：
    准确的小数值，m是数字总个数（负号不算），d是小数点后个数。 m最大值为65，d最大值为30。

精确度：
    **** 随着小数的增多，精度始终准确 ****
    对于精确数值计算时需要用此类型
    decaimal能够存储精确值的原因在于其内部按照字符串存储。

验证:
mysql> create table t1(x float(256,31));
ERROR 1425 (42000): Too big scale 31 specified for column 'x'. Maximum is 30.

mysql> create table t1(x float(256,30));
ERROR 1439 (42000): Display width out of range for column 'x' (max = 255)

mysql> create table t1(x float(255,30));  # 建表成功
Query OK, 0 rows affected (0.02 sec)

mysql> create table t2(x double(255,30)); # 建表成功
Query OK, 0 rows affected (0.02 sec)

mysql> create table t3(x decimal(66,31));
ERROR 1425 (42000): Too big scale 31 specified for column 'x'. Maximum is 30.

mysql> create table t3(x decimal(66,30));
ERROR 1426 (42000): Too-big precision 66 specified for 'x'. Maximum is 65.

mysql> create table t3(x decimal(65,30)); # 建表成功
Query OK, 0 rows affected (0.02 sec)

mysql> show tables;
+---------------+
| Tables_in_db1 |
+---------------+
| t1            |
| t2            |
| t3            |
+---------------+
rows in set (0.00 sec)

mysql> insert into t1 values(1.1111111111111111111111111111111); #小数点后31个1
Query OK, 1 row affected (0.01 sec)

mysql> insert into t2 values(1.1111111111111111111111111111111);
Query OK, 1 row affected (0.00 sec)

mysql> insert into t3 values(1.1111111111111111111111111111111);
Query OK, 1 row affected, 1 warning (0.01 sec)

mysql> select * from t1; # 随着小数的增多，精度开始不准确
+----------------------------------+
| x                                |
+----------------------------------+
| 1.111111164093017600000000000000 |
+----------------------------------+
row in set (0.00 sec)

mysql> select * from t2; # 精度比float要准确点，但随着小数的增多，同样变得不准确
+----------------------------------+
| x                                |
+----------------------------------+
| 1.111111111111111200000000000000 |
+----------------------------------+
row in set (0.00 sec)

mysql> select * from t3; # 精度始终准确,d为30，于是只留了30位小数
+----------------------------------+
| x                                |
+----------------------------------+
| 1.111111111111111111111111111111 |
+----------------------------------+
row in set (0.00 sec)



# 3、位类型（了解）

BIT(M)可以用来存放多位二进制数，M范围从1~64，如果不写默认为1位。
注意：对于位字段需要使用函数读取
    bin()显示为二进制
    hex()显示为十六进制


验证:

MariaDB [db1]> create table t9(id bit);
MariaDB [db1]> desc t9; #bit默认宽度为1
+-------+--------+------+-----+---------+-------+
| Field | Type   | Null | Key | Default | Extra |
+-------+--------+------+-----+---------+-------+
| id    | bit(1) | YES  |     | NULL    |       |
+-------+--------+------+-----+---------+-------+

MariaDB [db1]> insert into t9 values(8);
MariaDB [db1]> select * from t9; #直接查看是无法显示二进制位的
+------+
| id   |
+------+
|     |
+------+
MariaDB [db1]> select bin(id),hex(id) from t9; #需要转换才能看到
+---------+---------+
| bin(id) | hex(id) |
+---------+---------+
| 1       | 1       |
+---------+---------+

MariaDB [db1]> alter table t9 modify id bit(5);
MariaDB [db1]> insert into t9 values(8);
MariaDB [db1]> select bin(id),hex(id) from t9;
+---------+---------+
| bin(id) | hex(id) |
+---------+---------+
| 1       | 1       |
| 1000    | 8       |
+---------+---------+

# 日期类型
DATE TIME DATETIME TIMESTAMP YEAR 
作用：存储用户注册时间，文章发布时间，员工入职时间，出生时间，过期时间等

YEAR
    YYYY（1901/2155）

DATE
    YYYY-MM-DD（1000-01-01/9999-12-31）

TIME
    HH:MM:SS（'-838:59:59'/'838:59:59'）

DATETIME
    YYYY-MM-DD HH:MM:SS（1000-01-01 00:00:00/9999-12-31 23:59:59    Y）

TIMESTAMP
    YYYYMMDD HHMMSS（1970-01-01 00:00:00/2037 年某时）

验证:
============year=========================
MariaDB [db1]> create table t10(born_year year); # 无论year指定何种宽度，最后都默认是year(4)
MariaDB [db1]> insert into t10 values  
    -> (1900),
    -> (1901),
    -> (2155),
    -> (2156);
MariaDB [db1]> select * from t10;
+-----------+
| born_year |
+-----------+
|      0000 |
|      1901 |
|      2155 |
|      0000 |
+-----------+

============date,time,datetime===========
MariaDB [db1]> create table t11(d date,t time,dt datetime);
MariaDB [db1]> desc t11;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| d     | date     | YES  |     | NULL    |       |
| t     | time     | YES  |     | NULL    |       |
| dt    | datetime | YES  |     | NULL    |       |
+-------+----------+------+-----+---------+-------+

MariaDB [db1]> insert into t11 values(now(),now(),now()); # now() 获取mysql当前时间
MariaDB [db1]> select * from t11;
+------------+----------+---------------------+
| d          | t        | dt                  |
+------------+----------+---------------------+
| 2017-07-25 | 16:26:54 | 2017-07-25 16:26:54 |
+------------+----------+---------------------+

==================timestamp=================
MariaDB [db1]> create table t12(time timestamp);
MariaDB [db1]> insert into t12 values();
MariaDB [db1]> insert into t12 values(null);
MariaDB [db1]> select * from t12;
+---------------------+
| time                |
+---------------------+
| 2017-07-25 16:29:17 |
| 2017-07-25 16:30:01 |
+---------------------+

MariaDB [db1]> create table student(
    -> id int,
    -> name varchar(20),
    -> born_year year,
    -> birth date,
    -> class_time time,
    -> reg_time datetime);

MariaDB [db1]> insert into student values
    -> (1,'alex',"1995","1995-11-11","11:11:11","2017-11-11 11:11:11"),
    -> (2,'egon',"1997","1997-12-12","12:12:12","2017-12-12 12:12:12"),
    -> (3,'wsb',"1998","1998-01-01","13:13:13","2017-01-01 13:13:13");

MariaDB [db1]> select * from student;
+------+------+-----------+------------+------------+---------------------+
| id   | name | born_year | birth      | class_time | reg_time            |
+------+------+-----------+------------+------------+---------------------+
|    1 | alex |      1995 | 1995-11-11 | 11:11:11   | 2017-11-11 11:11:11 |
|    2 | egon |      1997 | 1997-12-12 | 12:12:12   | 2017-12-12 12:12:12 |
|    3 | wsb  |      1998 | 1998-01-01 | 13:13:13   | 2017-01-01 13:13:13 |
+------+------+-----------+------------+------------+---------------------+

============注意啦，注意啦，注意啦===========
1. 单独插入时间时，需要以字符串的形式，按照对应的格式插入
2. 插入年份时，尽量使用4位值
3. 插入两位年份时，<=69，以20开头，比如50,  结果2050      
                >=70，以19开头，比如71，结果1971
MariaDB [db1]> create table t12(y year);
MariaDB [db1]> insert into t12 values  
    -> (50),
    -> (71);
MariaDB [db1]> select * from t12;
+------+
| y    |
+------+
| 2050 |
| 1971 |
+------+


datetime与timestamp的区别:
在实际应用的很多场景中，MySQL的这两种日期类型都能够满足我们的需要，存储精度都为秒，但在某些情况下，会展现出他们各自的优劣。下面就来总结一下两种日期类型的区别。

1.DATETIME 的日期范围是 1001——9999年，TIMESTAMP的时间范围是 1970——2038年。
2.DATETIME 存储时间与时区无关，TIMESTAMP存储时间与时区有关，显示的值也依赖于时区。在mysql服务器，操作系统以及客户端连接都有时区的设置。
3.DATETIME 使用8字节的存储空间，TIMESTAMP的存储空间为4字节。因此，TIMESTAMP比DATETIME的空间利用率更高。
4.DATETIME 的默认值为null；TIMESTAMP的字段默认不为空（not null）,默认值为当前时间（CURRENT_TIMESTAMP），如果不做特殊处理，并且update语句中没有指定该列的更新值，则默认更新为当前时间。

mysql> create table t1(x datetime not null default now()); # 需要指定传入空值时默认取当前时间
Query OK, 0 rows affected (0.01 sec)

mysql> create table t2(x timestamp); # 无需任何设置，在传空值的情况下自动传入当前时间
Query OK, 0 rows affected (0.02 sec)

mysql> insert into t1 values();
Query OK, 1 row affected (0.00 sec)

mysql> insert into t2 values();
Query OK, 1 row affected (0.00 sec)

mysql> select * from t1;
+---------------------+
| x                   |
+---------------------+
| 2018-07-07 01:26:14 |
+---------------------+
row in set (0.00 sec)

mysql> select * from t2;
+---------------------+
| x                   |
+---------------------+
| 2018-07-07 01:26:17 |
+---------------------+
row in set (0.00 sec)

# 字符串类型
#官网：https://dev.mysql.com/doc/refman/5.7/en/char.html

\注意：char 和 varchar括号内的参数指的都是 字符的长度

# char类型：定长，简单粗暴，浪费空间，存取速度快
    字符长度范围：0-255（一个中文是一个字符，是utf8编码的3个字节）
    存储：
        存储char类型的值时，会往右填充空格来满足长度
        例如：指定长度为10，存>10个字符则报错，存<10个字符则用空格填充直到凑够10个字符存储
    检索：
        在检索或者说查询时，查出的结果会自动删除尾部的空格，除非我们打开pad_char_to_full_length SQL模式（SET sql_mode = 'PAD_CHAR_TO_FULL_LENGTH';）

# varchar类型：变长，精准，节省空间，存取速度慢
    字符长度范围：0-65535（如果大于21845会提示用其他类型 。mysql行最大限制为65535字节，字符编码为utf-8：https://dev.mysql.com/doc/refman/5.7/en/column-count-limit.html）
    存储：
        varchar类型存储数据的真实内容，不会用空格填充，如果'ab  ',尾部的空格也会被存起来
        强调：varchar类型会在真实数据前加1-2Bytes的前缀，该前缀用来表示真实数据的bytes字节数（1-2Bytes最大表示65535个数字，正好符合mysql对row的最大字节限制，即已经足够使用）
        如果真实的数据<255bytes则需要1Bytes的前缀（1Bytes=8bit 2**8最大表示的数字为255）
        如果真实的数据>255bytes则需要2Bytes的前缀（2Bytes=16bit 2**16最大表示的数字为65535）
    检索：
        尾部有空格会保存下来，在检索或者说查询时，也会正常显示包含空格在内的内容

Value	    CHAR(4)	Storage Required	VARCHAR(4)	Storage Required
''	        '    '	    4 bytes	           ''	         1 bytes
'ab'	    'ab  '	    4 bytes	           'ab'	         3 bytes
'abcd'	    'abcd'	    4 bytes	           'abcd'	     5 bytes
'abcdefgh'	'abcd'	    4 bytes	           'abcd'	     5 bytes


测试前了解两个函数
length：查看字节数
char_length:查看字符数

1. char填充空格来满足固定长度，但是在查询时却会很不要脸地删除尾部的空格（装作自己好像没有浪费过空间一样），然后修改sql_mode让其现出原形
mysql> create table t1(x char(5),y varchar(5));
Query OK, 0 rows affected (0.26 sec)

#char存5个字符，而varchar存4个字符
mysql> insert into t1 values('你瞅啥 ','你瞅啥 ');
Query OK, 1 row affected (0.05 sec)

mysql> SET sql_mode='';
Query OK, 0 rows affected, 1 warning (0.00 sec)

#在检索时char很不要脸地将自己浪费的2个字符给删掉了，装的好像自己没浪费过空间一样，而varchar很老实，存了多少，就显示多少
mysql> select x,char_length(x),y,char_length(y) from t1; 
+-----------+----------------+------------+----------------+
| x         | char_length(x) | y          | char_length(y) |
+-----------+----------------+------------+----------------+
| 你瞅啥    |              3 | 你瞅啥     |              4 |
+-----------+----------------+------------+----------------+
row in set (0.00 sec)

#略施小计，让char现出原形
mysql> SET sql_mode = 'PAD_CHAR_TO_FULL_LENGTH';
Query OK, 0 rows affected (0.00 sec)

#这下子char原形毕露了......
mysql> select x,char_length(x),y,char_length(y) from t1;
+-------------+----------------+------------+----------------+
| x           | char_length(x) | y          | char_length(y) |
+-------------+----------------+------------+----------------+
| 你瞅啥      |              5 | 你瞅啥     |              4 |
+-------------+----------------+------------+----------------+
row in set (0.00 sec)


#char类型：3个中文字符+2个空格=11Bytes
#varchar类型:3个中文字符+1个空格=10Bytes
mysql> select x,length(x),y,length(y) from t1;
+-------------+-----------+------------+-----------+
| x           | length(x) | y          | length(y) |
+-------------+-----------+------------+-----------+
| 你瞅啥      |        11 | 你瞅啥     |        10 |
+-------------+-----------+------------+-----------+
row in set (0.00 sec)


# 了解concat
mysql> select concat('数据: ',x,'长度: ',char_length(x)),concat(y,char_length(y)) from t1;
+------------------------------------------------+--------------------------+
| concat('数据: ',x,'长度: ',char_length(x))     | concat(y,char_length(y)) |
+------------------------------------------------+--------------------------+
| 数据: 你瞅啥  长度: 5                          | 你瞅啥 4                 |
+------------------------------------------------+--------------------------+
row in set (0.00 sec)


2. 虽然 CHAR 和 VARCHAR 的存储方式不太相同,但是取的时候对于两个字符串的比较,都只比较其值,忽略 CHAR 值存在的右填充空格,即使将 SQL _MODE 设置为 PAD_CHAR_TO_FULL_ LENGTH 也一样,但这不适用于like。

mysql> CREATE TABLE names (myname CHAR(10));
Query OK, 0 rows affected (0.03 sec)

mysql> INSERT INTO names VALUES ('Monty');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT myname = 'Monty', myname = 'Monty  ' FROM names;
+------------------+--------------------+
| myname = 'Monty' | myname = 'Monty  ' |
+------------------+--------------------+
|                1 |                  1 |
+------------------+--------------------+
row in set (0.00 sec)

mysql> SELECT myname LIKE 'Monty', myname LIKE 'Monty  ' FROM names;
+---------------------+-----------------------+
| myname LIKE 'Monty' | myname LIKE 'Monty  ' |
+---------------------+-----------------------+
|                   1 |                     0 |
+---------------------+-----------------------+
row in set (0.00 sec)

3. 总结
#InnoDB存储引擎：建议使用varchar类型
单从数据类型的实现机制去考虑，char数据类型的处理速度更快，有时甚至可以超出varchar处理速度的50%。
但对于InnoDB数据表，内部的行存储格式没有区分固定长度和可变长度列（所有数据行都使用指向数据列值的头指针），
因此在本质上，使用固定长度的CHAR列不一定比使用可变长度VARCHAR列性能要好。因而，主要的性能因素是数据行使用的存储总量。由于CHAR平均占用的空间多于VARCHAR，
因此使用VARCHAR来最小化需要处理的数据行的存储总量和磁盘I/O是比较好的。

#其他字符串系列（效率：char>varchar>text）
TEXT 系列 TINYTEXT TEXT MEDIUMTEXT LONGTEXT
BLOB 系列    TINYBLOB BLOB MEDIUMBLOB LONGBLOB 
BINARY 系列 BINARY VARBINARY

text：text数据类型用于保存变长的大字符串，可以组多到65535 (2**16 − 1)个字符。
mediumtext：A TEXT column with a maximum length of 16,777,215 (2**24 − 1) characters.
longtext：A TEXT column with a maximum length of 4,294,967,295 or 4GB (2**32 − 1) characters.


\枚举类型与集合类型
字段的值只能在给定范围中选择，如单选框，多选框
enum 单选 # 只能在给定的范围内选一个值，如性别 sex 男male/女female
set  多选 # 在给定的范围内可以选择一个或一个以上的值（爱好1,爱好2,爱好3...）

# 枚举类型（enum）
ENUM列最多可以有65535个不同的元素。(实际限制小于3000)
    示例：
        CREATE TABLE shirts (name VARCHAR(40),size ENUM('x-small', 'small', 'medium', 'large', 'x-large'));
        INSERT INTO shirts (name, size) VALUES ('dress shirt','large'), ('t-shirt','medium'),('polo shirt','small');



# 集合类型（set）
A SET column can have a maximum of 64 distinct members.
示例：
    CREATE TABLE myset (col SET('a', 'b', 'c', 'd'));
    INSERT INTO myset (col) VALUES ('a,d'), ('d,a'), ('a,d,a'), ('a,d,d'), ('d,a,d');

验证
MariaDB [db1]> create table consumer( 
    -> name varchar(50),
    -> sex enum('male','female'),
    -> level enum('vip1','vip2','vip3','vip4','vip5'), #在指定范围内，多选一
    -> hobby set('play','music','read','study')        #在指定范围内，多选多
    -> );

MariaDB [db1]> insert into consumer values  
    -> ('egon','male','vip5','read,study'),
    -> ('alex','female','vip1','girl');  # girl不存在所以会存成空

MariaDB [db1]> select * from consumer;
+------+--------+-------+------------+
| name | sex    | level | hobby      |
+------+--------+-------+------------+
| egon | male   | vip5  | read,study |
| alex | female | vip1  |            |
+------+--------+-------+------------+





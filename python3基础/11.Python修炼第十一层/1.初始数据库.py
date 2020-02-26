\mysql介绍
MySQL是一个关系型数据库管理系统，由瑞典MySQL AB 公司开发，目前属于 Oracle 旗下公司。MySQL 最流行的关系型数据库管理系统，在 WEB 应用方面MySQL是最好的 RDBMS (Relational Database Management System，关系数据库管理系统) 应用软件之一。

\mysql是什么
#mysql就是一个基于socket编写的C/S架构的软件

#客户端软件
　　mysql自带：如mysql命令，mysqldump命令等
　　python模块：如pymysql

\数据库管理软件分类
#分两大类：
　　关系型：如sqllite，db2，oracle，access，sql server，MySQL，注意：sql语句通用
　　非关系型：mongodb，redis，memcache

#可以简单的理解为：
    关系型数据库需要有表结构
    非关系型数据库是key-value存储的，没有表结构

\下载安装
# 源码安装mysql
1.解压tar包
cd /software
tar -xzvf mysql-5.6.21-linux-glibc2.5-x86_64.tar.gz
mv mysql-5.6.21-linux-glibc2.5-x86_64 mysql-5.6.21

2.添加用户与组
groupadd mysql
useradd -r -g mysql mysql
chown -R mysql:mysql mysql-5.6.21

3.安装数据库
su mysql
cd mysql-5.6.21/scripts
./mysql_install_db --user=mysql --basedir=/software/mysql-5.6.21 --datadir=/software/mysql-5.6.21/data

4.配置文件
cd /software/mysql-5.6.21/support-files
cp my-default.cnf /etc/my.cnf
cp mysql.server /etc/init.d/mysql
vim /etc/init.d/mysql   #若mysql的安装目录是/usr/local/mysql,则可省略此步
修改文件中的两个变更值
basedir=/software/mysql-5.6.21
datadir=/software/mysql-5.6.21/data

5.配置环境变量
vim /etc/profile
export MYSQL_HOME="/software/mysql-5.6.21"
export PATH="$PATH:$MYSQL_HOME/bin"
source /etc/profile

6.添加自启动服务
chkconfig --add mysql
chkconfig mysql on

7.启动mysql
service mysql start

8.登录mysql及改密码与配置远程访问
mysqladmin -u root password 'your_password'     #修改root用户密码
mysql -u root -p     #登录mysql,需要输入密码
mysql>GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'your_password' WITH GRANT OPTION;     #允许root用户远程访问
mysql>FLUSH PRIVILEGES;     #刷新权限




# 源码安装mariadb
1. 解压
tar zxvf  mariadb-5.5.31-linux-x86_64.tar.gz   
mv mariadb-5.5.31-linux-x86_64 /usr/local/mysql //必需这样，很多脚本或可执行程序都会直接访问这个目录

2. 权限
groupadd mysql             //增加 mysql 属组 
useradd -g mysql mysql     //增加 mysql 用户 并归于mysql 属组 
chown mysql:mysql -Rf  /usr/local/mysql    // 设置 mysql 目录的用户及用户组归属。 
chmod +x -Rf /usr/local/mysql    //赐予可执行权限 

3. 拷贝配置文件
cp /usr/local/mysql/support-files/my-medium.cnf /etc/my.cnf     //复制默认mysql配置 文件到/etc目录 

4. 初始化
/usr/local/mysql/scripts/mysql_install_db --user=mysql          //初始化数据库 
cp  /usr/local/mysql/support-files/mysql.server    /etc/init.d/mysql    //复制mysql服务程序 到系统目录 
chkconfig  mysql on     //添加mysql 至系统服务并设置为开机启动 
service  mysql  start  //启动mysql

5. 环境变量配置
vim /etc/profile   //编辑profile,将mysql的可执行路径加入系统PATH
export PATH=/usr/local/mysql/bin:$PATH 
source /etc/profile  //使PATH生效。

6. 账号密码
mysqladmin -u root password 'yourpassword' //设定root账号及密码
mysql -u root -p  //使用root用户登录mysql
use mysql  //切换至mysql数据库。
select user,host,password from user; //查看系统权限
drop user ''@'localhost'; //删除不安全的账户
drop user root@'::1';
drop user root@127.0.0.1;
select user,host,password from user; //再次查看系统权限，确保不安全的账户均被删除。
flush privileges;  //刷新权限

7. 一些必要的初始配置
1）修改字符集为UTF8
vi /etc/my.cnf
在[client]下面添加 default-character-set = utf8
在[mysqld]下面添加 character_set_server = utf8
2）增加错误日志
vi /etc/my.cnf
在[mysqld]下面添加：
log-error = /usr/local/mysql/log/error.log
general-log-file = /usr/local/mysql/log/mysql.log
3) 设置为不区分大小写，linux下默认会区分大小写。
vi /etc/my.cnf
在[mysqld]下面添加：
lower_case_table_name=1

修改完重启：#service  mysql  restart

# 登录，设置密码
初始状态下，管理员root，密码为空，默认只允许从本机登录localhost
设置密码
[root@egon ~]# mysqladmin -uroot password "123"        设置初始密码 由于原密码为空，因此-p可以不用
[root@egon ~]# mysqladmin -uroot -p"123" password "456"        修改mysql密码,因为已经有密码了，所以必须输入原密码才能设置新密码

命令格式:
[root@egon ~]# mysql -h172.31.0.2 -uroot -p456
[root@egon ~]# mysql -uroot -p
[root@egon ~]# mysql                    以root用户登录本机，密码为空

# 忘记密码
linux平台下，破解密码的两种方式
[root@egon ~]# rm -rf /var/lib/mysql/mysql #所有授权信息全部丢失！！！
[root@egon ~]# systemctl restart mariadb
[root@egon ~]# mysql

方法二：启动时，跳过授权库
[root@egon ~]# vim /etc/my.cnf    # mysql主配置文件
[mysqld]
skip-grant-table
[root@egon ~]# systemctl restart mariadb
[root@egon ~]# mysql
MariaDB [(none)]> update mysql.user set password=password("123") where user="root" and host="localhost";
MariaDB [(none)]> flush privileges;
MariaDB [(none)]> \q
[root@egon ~]# #打开/etc/my.cnf去掉skip-grant-table,然后重启
[root@egon ~]# systemctl restart mariadb
[root@egon ~]# mysql -u root -p123 #以新密码登录

\在windows下，为mysql服务指定配置文件
强调：配置文件中的注释可以有中文，但是配置项中不能出现中文
#在mysql的解压目录下，新建my.ini,然后配置
#1. 在执行mysqld命令时，下列配置会生效，即mysql服务启动时生效
[mysqld]
;skip-grant-tables
port=3306
character_set_server=utf8
default-storage-engine=innodb
innodb_file_per_table=1


#解压的目录
basedir=E:\mysql-5.7.19-winx64
#data目录
datadir=E:\my_data #在mysqld --initialize时，就会将初始数据存入此处指定的目录，在初始化之后，启动mysql时，就会去这个目录里找数据



#2. 针对客户端命令的全局配置，当mysql客户端命令执行时，下列配置生效
[client]
port=3306
default-character-set=utf8
user=root
password=123

#3. 只针对mysql这个客户端的配置，2中的是全局配置，而此处的则是只针对mysql这个命令的局部配置
[mysql]
;port=3306
;default-character-set=utf8
user=egon
password=4573


#！！！如果没有[mysql],则用户在执行mysql命令时的配置以[client]为准


\统一字符编码
#1. 修改配置文件
[mysqld]
default-character-set=utf8 
[client]
default-character-set=utf8 
[mysql]
default-character-set=utf8

#mysql5.5以上：修改方式有所改动
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8

#2. 重启服务
#3. 查看修改结果：
\s
show variables like '%char%'

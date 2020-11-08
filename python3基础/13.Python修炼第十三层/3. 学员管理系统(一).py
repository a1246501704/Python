
\学员管理: day65
	表结构：班级\学生\老师
		
		班级表（第一天）:
			id    title
			 1    全栈4期
			 2    全栈5期

		学生表:
			 id     name      班级ID（FK）
			  1     张英杰      1
			 
		老师表（第一天）:
			id       name
			 1       林海峰
			 2       林狗
			 3       苑日天

		老师班级关系表：
			id     老师ID    班级ID
			 1       1          1
			 2       1          2
			 3       2          2

	创建表:
	CREATE TABLE class (
  id int(11) NOT NULL AUTO_INCREMENT,
  title varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
INSERT INTO class VALUES(01,'class1');
INSERT INTO class VALUES(02,'class2');


	CREATE TABLE student (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(255) DEFAULT NULL,
  class_cid int(11) DEFAULT NULL,
  PRIMARY KEY (id),
  KEY fk_student_class (cid)
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;
INSERT INTO student VALUES(01,'student1',01);
INSERT INTO student VALUES(02,'student2',01);
INSERT INTO student VALUES(03,'student3',01);
INSERT INTO student VALUES(04,'student4',01);
INSERT INTO student VALUES(05,'student5',02);
INSERT INTO student VALUES(06,'student6',02);
INSERT INTO student VALUES(07,'student7',02);
INSERT INTO student VALUES(08,'student8',02);

	CREATE TABLE teacher (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;
INSERT INTO teacher VALUES(01,'teacher1');
INSERT INTO teacher VALUES(02,'teacher2');
INSERT INTO teacher VALUES(03,'teacher3');
INSERT INTO teacher VALUES(04,'teacher4');

	CREATE TABLE teacher2class (
  id int(11) NOT NULL AUTO_INCREMENT,
  teacher_id int(11) DEFAULT NULL,
  class_id int(11) DEFAULT NULL,
  PRIMARY KEY (id),
  KEY fk_teacher2class_teacher (teacher_id),
  KEY fk_teacher2class_class (class_id)
)ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;
INSERT INTO teacher2class VALUES(01,01,01);
INSERT INTO teacher2class VALUES(02,02,01);
INSERT INTO teacher2class VALUES(03,03,01);
INSERT INTO teacher2class VALUES(04,04,01);
INSERT INTO teacher2class VALUES(05,05,02);
INSERT INTO teacher2class VALUES(06,06,02);
INSERT INTO teacher2class VALUES(07,07,02);
INSERT INTO teacher2class VALUES(08,08,02);

select * from teacher2class;
+----+------------+----------+
| id | teacher_id | class_id |
+----+------------+----------+
| 1  | 1          | 1        |
| 2  | 2          | 1        |
| 3  | 3          | 1        |
| 4  | 4          | 1        |
| 5  | 5          | 2        |
| 6  | 6          | 2        |
| 7  | 7          | 2        |
| 8  | 8          | 2        |
+----+------------+----------+

	单表操作：
		- 增
		- 删
		- 改
		- 查
	一对多操作：
		- 增
		- 删
		- 改
		- 查
	多对多操作：
		- 增
		- 删
		- 改
		- 查
		
Django基础


前端知识（复习）
	- HTML
	- CSS


今日作业：
	- 老师管理
	- 对话框：添加、删除 【可选】

















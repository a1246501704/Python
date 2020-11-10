
\学员管理: day65
	# 表结构：班级\学生\老师
		
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

	# 创建表:
	CREATE TABLE class (
  id int(11) NOT NULL AUTO_INCREMENT,
  title varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
INSERT INTO class VALUES(1,'班级1');
INSERT INTO class VALUES(2,'班级2');
INSERT INTO class VALUES(3,'班级3');
INSERT INTO class VALUES(4,'班级4');
INSERT INTO class VALUES(5,'班级5');
INSERT INTO class VALUES(6,'班级6');


	CREATE TABLE student (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(255) DEFAULT NULL,
  class_id int(11) DEFAULT NULL,
  PRIMARY KEY (id),
  KEY fk_student_class (id)
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;
INSERT INTO student VALUES(1,'学生1',1);
INSERT INTO student VALUES(2,'学生2',1);
INSERT INTO student VALUES(3,'学生3',1);
INSERT INTO student VALUES(4,'学生4',1);
INSERT INTO student VALUES(5,'学生5',2);
INSERT INTO student VALUES(6,'学生6',2);
INSERT INTO student VALUES(7,'学生7',2);
INSERT INTO student VALUES(8,'学生8',2);

	CREATE TABLE teacher (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=2000 DEFAULT CHARSET=utf8;
INSERT INTO teacher VALUES(1,'老师1');
INSERT INTO teacher VALUES(2,'老师2');
INSERT INTO teacher VALUES(3,'老师3');
INSERT INTO teacher VALUES(4,'老师4');

	CREATE TABLE teacher2class (
  id int(11) NOT NULL AUTO_INCREMENT,
  teacher_id int(11) DEFAULT NULL,
  class_id int(11) DEFAULT NULL,
  PRIMARY KEY (id),
  KEY fk_teacher2class_teacher (teacher_id),
  KEY fk_teacher2class_class (class_id)
)ENGINE=InnoDB AUTO_INCREMENT=3000 DEFAULT CHARSET=utf8;
INSERT INTO teacher2class VALUES(1,1,1);
INSERT INTO teacher2class VALUES(2,2,1);
INSERT INTO teacher2class VALUES(3,3,1);
INSERT INTO teacher2class VALUES(4,4,1);
INSERT INTO teacher2class VALUES(5,5,2);
INSERT INTO teacher2class VALUES(6,6,2);
INSERT INTO teacher2class VALUES(7,7,2);
INSERT INTO teacher2class VALUES(8,8,2);

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

















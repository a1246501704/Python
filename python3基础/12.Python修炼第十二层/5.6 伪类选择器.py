\六 伪类选择器
#1、作用：常用的几种伪类选择器。

#1.1 没有访问过的超链接a标签样式：
a:link {
  color: blue;
}

#1.2 访问过以后的超链接a标签样式：
a:visited {
  color: gray;
}

#1.3 鼠标悬浮在元素上应用样式：
a:hover {
  background-color: #eee; 
}

#1.4 鼠标点击瞬间的样式：
a:active {
  color: green;
}

#1.5 input输入框获取焦点时样式：
input:focus {
  outline: none;
  background-color: #eee;
}

#2 注意：
a标签的伪类选择器可以单独出现，也可以一起出现
a标签的伪类选择器如果一起出现，有严格的顺序要求，否则失效
    link，visited，hover，active
hover是所有其他标签都可以使用的
focus只给input标签使用


# 示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后代选择器</title>

    <style type="text/css">
        a:link {
            color: #cccccc;
        }
        a:visited {
            color: #55BBBB;
        }
        a:hover {
            color: green;
        }
        a:active {
            color: red;
        }

        input:hover {
            outline: none;
            background-color: #cccccc;

        }

    </style>
</head>
<body>
<a href="https://www.baidu.com/a/b/c/d.html">点击我</a>
<input type="text">
</body>
</html>
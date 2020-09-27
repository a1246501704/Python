\七 伪元素选择器
#1、常用的伪元素。

#1.1 first-letter（首字母）
# 杂志类文章首字母样式调整
例如：
p:first-letter {
  font-size: 48px;
}

#1.2 before（前面）
# 用于在元素的内容前面插入新内容。
例如：
在所有p标签的内容前面加上一个红色的*。
p:before {
  content: "*";
  color: red;
}

#1.3 after（后面）
# 用于在元素的内容后面插入新内容。
例如：
在所有p标签的内容后面加上一个蓝色的?。
p:after {
  content: "?";
  color: red;
}

# 示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后代选择器</title>

    <style type="text/css">
        p:first-letter {
            font-size: 50px;
        }
        /*两个冒号与一个是一样的，老版本用的是一个冒号，考虑到兼容性推荐使用一个冒号*/
        a::after {
            content: "?";
            color: red;
        }
        a:before {
            content: "-";
            color: green;
        }
    </style>

</head>
<body>
    <p>英雄不问出处，流氓不论岁数</p>
    <a href="#" class="help">老男孩是干什么的</a>
    <a href="#" class="help">老男孩是干什么的</a>
    <a href="#" class="help">老男孩是干什么的</a>
</body>
</html>
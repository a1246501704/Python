\三 交集选择器与并集选择器
\1、交集选择器（不常用）
#1、作用：给所有选择器选中的标签中，相交的那部分标签设置属性

#2、格式：
    选择器1选择器2 {
        属性：值;
    }

#3、注意：
1、选择器与选择器之间没有任何链接符号
2、选择器可以使用标签名称、id、class
3、交集选择器在企业开发中并不多见，了解即可 因为：p.part1 完全可以用.part1取代

# 示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>

        <style type="text/css">
            p.part1 {
                color: red;
            }
            p#p1{
                font-size: 100px;
            }
        </style>
    </head>
    <body>
        <p class="part1">我是段落</p>
        <p id="p1">我是段落</p>
        <p class="part1">我是段落</p>
        <p>我是段落</p>
        <p>我是段落</p>
        <p>我是段落</p>
    </body>
</html>

\2、并集选择器
#1、作用：给所有满足条件的标签设置属性

#2、格式：
    选择器1,选择器2 {
        属性：值;
    }

#3、注意：
1、选择器与选择器之间必须用逗号来链接
2、选择器可以使用标签名称、id、class

# 示例  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后代选择器</title>

    <style type="text/css">
        .part1,h1,a {
            color: red;
        }
    </style>
</head>
<body>
    <h1>哈哈啊</h1>
    <p class="part1">我是段落</p>
    <p id="p1">我是段落</p>
    <p class="part1">我是段落</p>
    <a href="#">我是我</a>
    <p>我是段落</p>
    <p>我是段落</p>
    <p>我是段落</p>
</body>
</html>
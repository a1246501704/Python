\一 基本选择器
# 选择器用于定位哪段HTML代码，定位到以后给其添加上CSS样式。
    # id选择器
    # 类选择器
    # 标签选择器
    # 通配符选择器

\1、id（类似与关键字）选择器
#1、作用：根据指定的id名称，在当前界面中找到对应的唯一一个的标签，然后设置属性。命名id时避免使用html中的其他标签名称或关键字。

#2、格式
id名称 {
    属性：值;
}

#3、注意点：
1、在企业开发中如果仅仅只是为了设置样式，通常不会使用id，在前端开发中id通常是留给js使用的。
2、每个标签都可以设置唯一一个id，id就相当于人/标签的身份证，因此在同一界面内id绝不能重复。
3、引用id一定要加#
4、id的命名只能由字符、数字、下划线组成，且不能以数字开头，更不能是html关键字如p，a，img等。

# 示例
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
    <title>id选择器</title>
    <style>
        #p1 {
            color: red;
        }
        #p2 {
            color: green;
        }
        #p3 {
            color: blue;
        }
    </style>
</head>

<body>
<p id="p1">大多数人的帅，都是浮在表面的，是外表的帅</p>
<p id="p2">而EGON，不仅具备外表帅，内心更是帅了一逼</p>
<p id="p3">EGON就是我，我就是EGON</p>
</body>

</html>

\2、类选择器（写项目使用这个）
#1、作用：根据指定的类名称，在当前界面中找到对应的标签，然后设置属性。

#2、格式：
.类名称 {
    属性：值;
}

#3、注意点：
1、类名就是专门用来给某个特定的标签设置样式的
2、每个标签都可以设置一个或多个不同的class（空格分隔），class就相当于人/标签的名称，因此同一界面内class可以重复。
3、引用class一定要加点.
4、类名的命名规则与id的命名规则相同

# 示例
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
    <title>id选择器</title>
    <style>
        .p1 {
            color: red;
        }
        .p2 {
            color: green;
        }
        .p3 {
            color: blue;
        }
    </style>
</head>

<body>
<p class="p1">大多数人的帅，都是浮在表面的，是外表的帅</p>
<p class="p2">而EGON，不仅具备外表帅，内心更是帅了一逼</p>
<p class="p3">EGON就是我，我就是EGON</p>
</body>

</html>


#练习
第一行与第三行的颜色都是红色
第一行与第二行的字体大小都是50px
第二行与第三行内容有个下划线

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
    <title>id选择器</title>
    <style>
        .p1 {
            color: red;
        }
        .p2 {
            font-size: 50px;
        }
        .p3 {
            text-decoration: underline;
        }

    </style>
</head>

<body>
<p class="p1 p2">第一行内容</p>
<p class="p2 p3">第二行内容</p>
<p class="p1 p3">第三行内容</p>
</body>

</html>



\3、标签选择器（只要一设置涉及的面太大，不好控制。）
#1、作用：根据指定的标签名称，在当前界面中找到所有该名称的标签，然后设置属性

#2、格式：
标签名称 {
    属性：值;
}

#3、注意点：
1、只要是HTML的标签都能当做标签选择器。
2、标签选择器选中的是当前界面中的所有标签,而不能单独选中某一标签。
3、标签选择器，无论嵌套多少层都能选中。

# 示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标签选择器</title>

    <style type="text/css">
        p {
            color: red;
        }
    </style>
</head>
<body>
    <p>zhy美丽的外表下其实隐藏着一颗骚动的心</p>
    <ul>
        <li>
            <ul>
                <li>
                    <ul>
                        <li>
                            <p>这颗心叫做七巧玲珑心，男人吃了会流泪，女人吃了会怀孕</p>
                        </li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>

</body>
</html>

\4、通配符选择器
#1、作用：选择所有标签

#2、格式：
* {
    属性：值；
}

#3、注意点：
1、在企业开发中一般不会使用通配符选择器
    理由是：
    由于通配符选择器是设置界面上所有的标签的属性，
    所以在设置之前会遍历所有的标签
    如果当前界面上的标签比较多，那么性能就会比较差

# 示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>通配符选择器</title>

    <style type="text/css">

        * {
            color: red;
        }

    </style>
</head>
<body>
    <h1 >我是标题</h1>
    <p >我是段落</p>
    <a href="#">我是超链接</a>
</body>
</html>

\二 组合选择器
\1、后代选择器
#1、作用：找到指定标签的所有后代（儿子，孙子，重孙子、、、）标签，设置属性
# 修改某个标签或id下的多个同级和子级下的某个级别的样式

#2、格式：
    标签名1 xxx {
        属性：值;
    }

#3、注意：
1、后代选择器必须用空格隔开
2、后代不仅仅是儿子，也包括孙子、重孙子
3、后代选择器不仅仅可以使用标签名称，还可以使用其他选择器比如id或class
4、后代选择器可以通过空格一直延续下去

# 示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后代选择器</title>

    <style type="text/css">
        /*
        .part1 p  {
            color: red;
        }
        */
        div p {
            color: red;
        }
        #id1 li p {
            font-size: 50px;
        }

        div ul li a {
            font-size: 100px;
            color: green;
        }
    </style>
</head>
<body>
    <p>我是body下的段落1</p>
    <!--如果想为div内所有标签都设置属性，无论用id还是class都不合理，因为当div内的标签过多，我们无法加那么多id或者class-->
    <div id="id1" class="part1">
        <p>我是div下的段落1</p>
        <p>我是div下的段落2</p>
        <ul>
            <li class="aaa">
                <p class="ccc">我是ul>li下的段落1</p>
                <p class="ddd">我是ul>li下的段落</p>
                <a href="">点我啊1</a>
            </li>
            <li>
                <a href="#">点我啊2</a>
            </li>
        </ul>
    </div>
    <p>我是body下的段落2</p>
</body>
</html>

\2、子元素选择器
#1、作用：找到指定标签的所有特定的直接子元素，然后设置属性。

#2、格式：
    标签名称1>标签名称2 {
        属性：值;
    }
先找到名称叫做"标签名称1"的标签，然后在这个标签中查找所有直接子元素名称叫做"标签名称2"的元素，注意是用 > 大于号连接。

#3、注意：
1、子元素选择器之间需要用>符号链接，并且不能有空格
    比如div >p会找div标签的所有后代标签，标签名为">p"
2、子元素选择器只会查找儿子，不会查找其他嵌套的标签
3、子元素选择器不仅可以用标签名称，还可以使用其他选择器,比如id或class
4、子元素选择器可以通过 > 符号一直延续下去

# 示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后代选择器</title>

    <style type="text/css">
        body>p {
            color: green;
        }

        div>p {
            color: red;
        }

        .aaa>a {
            font-size: 100px;
        }

        div>ul>li>.ddd {
            color: blue;
        }
    </style>
</head>
<body>
    <p>我是body下的段落1</p>
    <!--如果想为div内所有标签都设置属性，无论用id还是class都不合理，因为当div内的标签过多，我们无法加那么多id或者class-->
    <div id="id1" class="part1">
        <p>我是div下的段落1</p>
        <p>我是div下的段落2</p>
        <ul>
            <li class="aaa">
                <p class="ccc">我是ul>li下的段落1</p>
                <p class="ddd">我是ul>li下的段落2</p>
                <a href="">点我啊1</a>
            </li>
            <li>
                <a href="#">点我啊2</a>
            </li>
        </ul>
    </div>
    <p>我是body下的段落2</p>
</body>
</html>

后代选择器vs子元素选择器

\3、毗邻选择器，CSS2推出（又称相邻兄弟选择器）
#1、作用：选定紧跟其后的那个标签

#2、格式 
选择器1+选择器2 {
    属性：值;
}

#3、注意点：
1、毗邻选择器必须通过+号链接，选择器1标签相邻的是选择器2标签才会被选中。
2、毗邻选择器只能选中紧跟其后的那个标签，不能选中被隔开的标签



\4、弟弟选择器，CSS3推出（又称通用兄弟选择器）
#1、作用：给指定选择器后面的所有选择器中的所有标签设置属性

#2、格式： 
选择器1~选择器2 {
    属性：值;
}

#3、注意点：
1、通用兄弟选择器必须用~来链接
2、通用兄弟选择器选中的是指选择器后面的某个选择器选中的所有标签，匹配到 选择器1 下面所有的 选择器2这标签。
3、无论有没有被隔开，都可以被选中

# 示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后代选择器</title>

    <style type="text/css">
        h1+p {
            font-size: 50px;
        }
        h1~p {
            color: red;
        }

    </style>
</head>
<body>
    <h1 >我是标题1</h1>
    <a href="">有了这个标签，p就不再是紧跟h1标签了,但通用兄弟选择器仍然能选中</a>
    <p>我是段落</p>
    <p>我是段落</p>
    <p>我是段落</p>
    <p>我是段落</p>
    <p>我是段落</p>
    <p>我是段落</p>
    <p>我是段落</p>
    <p>我是段落</p>
    <p>我是段落</p>
    <h1>我是标题2</h1>
    <p>我是段落</p>

</body>
</html>


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

\四 序列选择器
#1、作用：
css3中新推出的选择器中，最具代表性的的9个，又称为序列选择器，过去的选择器中要选中某个必须加id或class，学习了这9个后，不用加id或class，想选中同级别的第几个就选第几个

#2、格式
#2.1 同级别
:first-child    p:first-child    同级别的第一个
:last-child     p:last-child     同级别的最后一个
:nth-child(n)                    同级别的第n个
:nth-last-child(n)               同级别的倒数第n个

#2.2 同级别同类型
:first-of-type                   同级别同类型的第一个
:last-of-type                    同级别同类型的最后一个
:nth-of-type(n)                  同级别同类型的第n个
:nth-last-of-type(n)             同级别同类型的倒数第n个

#2.3 其他
:only-of-type                    同类型的唯一一个
:only-child                      同级别的唯一一个

\示例：同级别
#1、同级别的第一个
#1.1 示范一
p:first-child { 
    color: red;
}
代表：同级别的第一个标签，并且要求第一个是一个p标签

<p>我是段落1</p>
<p>我是段落2</p>
<p>我是段落3</p>
<p>我是段落4</p>
<p>我是段落5</p>
<div>
    <p>我是段落6</p>
</div>

这样的话第一个p和div中的第一个p都变成红色，

#1.2 示范二
p:first-child {
    color: red;
}
代表：同级别的第一个，并且第一个要求是一个p标签

<h1>w我是标题</h1>
<p>我是段落1</p>
<p>我是段落2</p>
<p>我是段落3</p>
<p>我是段落4</p>
<p>我是段落5</p>
<div>
    <p>我是段落6</p>
</div>

这样的话只有div中的第一个p变红，因为在有在div内同一级别的第一个才是p

注意点：
    :fist-child就是第一个孩子，不区分类型

#2、同级别的最后一个
p:last-child {
    color: red;
}
代表：同级别的最后一个，并且最后一个要求是一个p标签

<h1>我是标题</h1>
<p>我是段落1</p>
<p>我是段落2</p>
<p>我是段落3</p>
<p>我是段落4</p>
<p>我是段落5</p>
<div>
    <p>我是段落6</p>
</div>
<p>我是段落7</p>
这样的话只有6跟7都变红

#3、同级别的第n个
p:nth-child(3) {
    color: red;
}
代表：同级别的第3个，并且第3个要求是一个p标签

<h1>我是标题</h1>
<p>我是段落1</p>
<p>我是段落2</p>
<p>我是段落3</p>
<p>我是段落4</p>
<p>我是段落5</p>
<div>
    <p>我是段落6.1</p>
    <p>我是段落6.2</p>
    <h1>我是标题</h1>
</div>
<p>我是段落7</p>
这样的话只有“我是段落2”变红

#4、同级别的倒数第n个
p:nth-last-child(3) {
    color: red;
}
代表：同级别的倒数第3个，并且第3个要求是一个p标签
<h1>我是标题</h1>
<p>我是段落1</p>
<p>我是段落2</p>
<p>我是段落3</p>
<p>我是段落4</p>
<p>我是段落5</p>
<div>
    <p>我是段落6.1</p>
    <p>我是段落6.2</p>
    <h1>我是标题</h1>
</div>
<p>我是段落7</p>
这样的话只有“我是段落6.1”和“我是段落5”被选中



\示例:同级同类型
<h1>我是标题</h1>
<p>我是段落1</p>
<p>我是段落2</p>
<p>我是段落3</p>
<p>我是段落4</p>
<p>我是段落5</p>
<div>
    <p>我是段落6.1</p>
    <p>我是段落6.2</p>
    <h1>我是标题</h1>
</div>
<p>我是段落7</p>
#1、同级别同类型的第一个
p:first-of-type {
    color: red;
}
“我是段落1”和“我是段落6.1”被选中


#2、同级别同类型的最后一个
p:last-of-type {
    color: red;
}
“我是段落7”和“我是段落6.2”被选中


#3、同级别同类型的第n个
p:nth-of-type(2) {
    color: red;
}
“我是段落2”和“我是段落6.2”被选中


#4、同级别同类型的倒数第n个
p:nth-last-of-type(2) {
    color: red;
}
“我是段落5”和“我是段落6.1”被选中




\示例：其他
#1、同级别同类型的唯一一个，同级别中其他类型的标签不影响。
p:only-of-type {
    color: red;
}

<h1>我是标题</h1>
<div>
    <p>我是段落6.1</p>
    <p>我是段落6.2</p>
    <h1>我是标题</h1>
</div>
<p>我是段落7</p>

“我是段落7“被选中

#2、同级别的唯一一个该标签，不能有同类型及其他。
p:only-child {
    color: red;
}

<h1>我是标题</h1>
<div>
    <p>我是段落6.1</p>
</div>
<p>我是段落7</p>
“我是段落6.1”被选中



\五 属性选择器
#1、作用：根据指定的属性名称找到对应的标签，然后设置属性。
       该选择器，最常用于input标签
 
#2、格式与具体用法：
    [属性名]
    其他选择器[属性名]
    [属性名=值]
    [属性名^=值] # 以什么开头
    [属性名$=值] # 
    [属性名*=值]


    例1：找到所有包含id属性的标签
        [id]
    
    例2：找到所有包含id属性的p标签
        p[id]
    
    例3：找到所有class属性值为part1的p标签
        p[class="part1"]
    
    例4：找到所有href属性值以https开头的a标签
        a[href^="https"]
        
    例5：找到所有src属性值以png结尾的img标签
        img[src$="png"]
        
    例6：找到所有class属性值中包含part2的标签
        [class*="part"]
    

# 示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后代选择器</title>

    <style type="text/css">
        [id] {
            color: red;
        }
        p[id] {
            font-size: 30px;
        }
        p[class="part1"] {
            color: green;
        }
        a[href^="https"] {
            font-size: 50px;
        }
        img[src$="png"] {
            width: 100px;
        }
        [class*="part"] {
            text-decoration: line-through;
        }

    </style>
</head>
<body>
    <h1 id="id1">哈哈啊</h1>
    <p id="id2">我是段落</p>
    <p class="part1">我是段落</p>
    <p class="xxx part2 yyy">我是段落</p>
    <a href="#">我是我</a>
    <a href="http://www.baidu.com">http://www.baidu.com</a>
    <a href="https://www.baidu.com">https://www.baidu.com</a>
    <img src="1.png" alt="">
    <img src="2.jpg" alt="">
    <p>我是段落</p>
    <p>我是段落</p>

</body>
</html>


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



\八 CSS三大特性
\1、继承性
#1、定义：给某一个元素设置一些属性，该元素的后代也可以使用，这个我们就称之为继承性

#2、注意：
    1、只有以color、font-、text-、line-开头的属性才可以继承
    2、a标签的文字颜色和下划线是不能继承别人的
    3、h标签的文字大小是不能继承别人的，会变大，但是会在原来字体大小的基础上变大
    
    ps:打开浏览器审查元素可以看到一些inherited from。。。的属性
#3、应用场景：
    通常基于继承性统一设置网页的文字颜色，字体，文字大小等样式

# 示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后代选择器</title>

    <style type="text/css">

        div {
            color: red;
            font-size: 50px;
        }


    </style>
</head>
<body>

<div>
    <h1>我是标题</h1>
    <p><a href="#">偶的博爱</a></p>
    <ul>
        <li>导航1</li>
        <li>导航2</li>
        <li>导航2</li>
    </ul>
</div>

<div>
    <div>
        <p>aaaa</p>
    </div>
    <div>
        <p>bbbb</p>
    </div>
</div>


</body>
</html>

\2、层叠性
#1、定义：CSS全称：Cascading StyleSheet层叠样式表，层叠性指的就是CSS处理冲突的一种能力，即如果有多个选择器选中了同一个标签那么会有覆盖效果

#2、注意：
1、层叠性只有在多个选择器选中了同一个标签，然后设置了相同的属性，才会发生层叠性
ps：通过谷歌浏览器可以查看到，一些属性被划掉了

# 示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>
        <style type="text/css">
            p {
                color: red;
            }
            .ppp {
                color: green;
            }
        </style>
    </head>
    <body>
        <p class="ppp">我是段落</p>
    </body>
</html>


\3、优先级
#1、定义：当多个选择器选中同一个标签，并且给同一个标签设置相同的属性时，如何层叠就由优先级来确定。

#2、优先级
    整体优先级从高到底：行内样式 > 嵌入样式 > 外部样式
    行内样式并不推荐使用，所以我们以嵌入为例来介绍优先级

1、大前提：直接选中 > 间接选中(即继承而来的)
#1、以下为直接选中
    <style type="text/css">
        #id1 {
            color: red;
        }

        .ppp {
            color: green;
        }

        p {
            color: blue;
        }
    </style>

#2、以下为间接选中
    <style type="text/css">
        ul {
            color: yellow;
        }
    </style>

    <ul>
        <li>
            <p id="id1" class="ppp">我是span</p>
        </li>
    </ul>


2、如果都是间接选中，那么谁离目标标签比较近，就听谁的
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>
        <style type="text/css">
            /*离目标近*/
            li {
                color: red;
            }
            /*离目标远*/
            ul {
                color: yellow;
            }
        </style>
    </head>
    <body>
        <ul>
            <li>
                <p id="id1" class="ppp">我是span</p>
            </li>
        </ul>
    </body>
</html>


3、如果都是直接选中，并且都是同类型的选择器，那么就是谁写的在后面就听谁的
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>

        <style type="text/css">
            p {
                color: red;
            }
            /*同样都是标签选择器，谁写在后面谁生效*/
            p {
                color: yellow;
            }
        </style>
    </head>
    <body>
        <ul>
            <li>
                <p id="id1" class="ppp">我是span</p>
            </li>
        </ul>
    </body>
</html>



4、如果都是直接选中，并且是不同类型的选择器，那么就会按照选择器的优先级来层叠
    id > 类 > 标签 > 通配符(也算直接选中) > 继承 > 浏览器默认（即没有设置任何属性）
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>
        <style type="text/css">
            /*打开浏览器依次去掉优先级高的来进行验证*/
            #id1 {
                color: red;
            }
            .ppp {
                color: green;
            }
            p {
                color: blue;
            }
            * {
                color: yellow;
            }
            li {
                color: #7e1487;
            }
        </style>
    </head>
    <body>
        <ul>
            <li>
                <p id="id1" class="ppp">我是span</p>
            </li>
        </ul>
    </body>
</html>


5、优先级之!important
#1、作用：还有一种不讲道理的!import方式来强制指定的属性的优先级提升为最高，但是不推荐使用。因为大量使用!import的代码是无法维护的。
  
#2、注意：
    1、!important只能用于直接选中，不能用于间接选中
    2、!important只能用于提升被指定的属性的优先级，其他属性的优先级不会被提升
    3、!important必须写在属性值分号的前面

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后代选择器</title>

    <style type="text/css">
        /*打开浏览器依次去掉优先级高的来进行验证*/
        #id1 {
            color: red;
        }
        .ppp {
            color: green;
        }
        p {
            color: blue;
        }
        * {
            color: yellow !important;
        }
        li {
            color: #7e1487;
        }

    </style>
</head>
<body>

    <ul>
        <li>
            <p id="id1" class="ppp">我是span</p>
        </li>
    </ul>
</body>
</html>


6、优先级之权重计算
#1、强调
如果都是直接选中，并且混杂了一系列其他的选择器一起使用时，则需要通过计算机权重来判定优先级

#2、计算方式（到达目标标签的距离相同时）
    #1、id数多的优先级高
    #2、id数相同，则判定类数多的优先级高
    #3、id数、class数均相同，则判定标签数多的优先级高
    #4、若id数、class数、标签数均相同，则无需继续往下计算了，谁写在后面谁的优先级高
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后代选择器</title>

    <style type="text/css">
        #id1 #id2 #id3 .ppp{
            color: red;
        }
        #id2 #id3.aaa p{
            color: purple;
        }

        #id1.ccc>.bbb>.aaa>p {
            color: pink;
        }

        #id1 .aaa .ppp {
            color: green;
        }

        #id2 .aaa p {
            color: yellow;
        }

        div ul li p {
            color: blue;
        }

        div ul p {
            color: cyan;
        }

    </style>
</head>
<body>
    <div id="id1" class="ccc">
        <ul id="id2" class="bbb">
            <li id="id3" class="aaa">
                <p class="ppp">我是段落</p>
            </li>
        </ul>
    </div>
</body>
</html>



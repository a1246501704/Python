\一 什么是CSS
CSS全称Cascading Style Sheet层叠样式表，是专用用来为HTML标签添加样式的。
样式 # 指的是HTML标签的显示效果，比如换行、宽高、颜色等等
层叠 # 属于CSS的三大特性之一，我们将在后续内容中介绍
表  # 指的是我们可以将样式统一收集起来写在一个地方或者一个CSS文件里


\二 为何要用CSS
在没有CSS之前，我们想要修改HTML标签的样式则需要为每个HTML标签单独定义样式属性，如下
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1 align="center">
            <font color="pink" size="5">天净沙·秋思</font>
        </h1>
        <p align="center">
            <font color="pink" size="5">锦瑟无端五十弦，一弦一柱思华年。</font>
        </p>
        <p align="center">
            <font color="pink" size="5">庄生晓梦迷蝴蝶，望帝春心托杜鹃。</font>
        </p>
        <p align="center">
            <font color="pink" size="5">沧海月明珠有泪，蓝田日暖玉生烟。</font>
        </p>
        <p align="center">
            <font color="pink" size="5">此情可待成追忆，只是当时已惘然。</font>
        </p>
    </body>
</html>

这么做的缺点是
#1、记忆困难：需要记忆每个标签的所有样式相关属性，如果标签没有某个样式相关的属性，那么设置了也没有效果
#2、代码耦合度高：HTML语义与样式耦合到一起
#3、扩展性差：当某一类样式需要修改时，我们需要找到所有设置了该样式标签进行修改
于是CSS应运而生，很好地解决了以上三个问题
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <style>
            h1,p {
                color: pink;
                font-size: 24px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>天净沙·秋思</h1>
        <p>锦瑟无端五十弦，一弦一柱思华年。</p>
        <p>庄生晓梦迷蝴蝶，望帝春心托杜鹃。</p>
        <p>沧海月明珠有泪，蓝田日暖玉生烟。</p>
        <p>此情可待成追忆，只是当时已惘然。</p>
    </body>
</html>

\三 如何使用CSS
1、如何使用CSS之CSS的语法
CSS语法可以分为两部分：
#1、选择器
#2、声明
声明由属性和值组成，多个声明之间用分号分隔，如下图

    见图  CSS语法
        <style>
            h1,p {
                color: pink;
                font-size: 24px;
                text-align: center;
            }
        </style>
'''
h1,p  称为选择器，用于body中哪些标签
{}    为定位到的标签设置样式
'''

2、如何使用CSS之CSS的四种引入方式
#1、内联式（下载一点html代码就立即添加上样式）
<p style="color: red;font-size: 50px;text-align: center">Egon是一个非常了不起的人</p>

#2、嵌入式
<head>
    <style>
        p {
            color: red;
            font-size: 50px;
            text-align: center
        }
    </style>
</head>

#3、导入式（先下载html再加载样式）
<head>
    <style>
        /*形式一：*/
        /*@import "css/mystyle.css";*/
        /*形式二：*/
        @import url("css/mystyle.css");
    </style>
</head>

#4、外联式（企业开发中使用这种方式），鼠标拖着css文件往head里放就可以自动生成。
<head>
    <link rel="stylesheet" href="css/mystyle.css">
</head>



详细解释
#1、行内式
行内式是在标签的style属性中设定CSS样式。这种方式没有体现出CSS的优势，不推荐使用。
<p style="color: red;font-size: 50px;text-align: center">Egon是一个非常了不起的人</p>

#2、嵌入式
嵌入式是将CSS样式集中写在网页<head></head>标签内的的<style></style>标签对中。格式如下：
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        p {
            color: red;
            font-size: 50px;
            text-align: center
        }
    </style>
</head>
<body>

<p>Egon是一个非常了不起的人</p>

</body>
</html>


#新建外部样式表，然后使用导入式和链接式引入
首先在与html文件同级目录下有一个css文件夹，该文件夹下新建一个外部样式表mystyle.css,内容为
p {
    color: red;
    font-size: 50px;
    text-align: center
}

#3、导入式
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        /*形式一：*/
        /*@import "css/mystyle.css";*/
        /*形式二：*/
        @import url("css/mystyle.css");

    </style>
</head>
<body>

<p>Egon是一个非常了不起的人</p>

</body>
</html>

#4、链接式（推荐使用） 
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/mystyle.css">
</head>
<body>

<p>Egon是一个非常了不起的人</p>

</body>
</html>


#导入式与链接式的区别:
1、<link/>标签属于XHTML,@import是属于CSS2.1特有的，对于不兼容CSS2.1的浏览器来说就是无效的
2、导入式的缺点：
导入式会在整个网页装载完后再装载CSS文件，因此这就导致了一个问题，如果网页比较大则会儿出现先显示无样式的页面，闪烁一下之后，再出现网页的样式。这是导入式固有的一个缺陷，用户体验差。
3、链接式的优点：
使用链接式时与导入式不同的是它会在网页文件主体装载前装载CSS文件，因此显示出来的网页从一开始就是带样式的效果的，它不会象导入式那样先显示无样式的网页，然后再显示有样式的网页，这是链接式的优点。


#！！！注意点！！！
1、style标签必须放到head内 ,type="text/css"代表文本类型的css
2、type属性其实可以不用写，默认就是type="text/css"
3、设置样式时必须按照固定的格式来设置，key:value;
    其中;不能省略，最后一个属性其实可以省略，但我们可以简单地统一记成不 
    能省略就行了





3、css注释
/*这是注释*/
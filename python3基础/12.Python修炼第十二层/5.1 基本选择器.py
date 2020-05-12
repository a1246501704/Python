\一 基本选择器
# 选择器用于定位哪段HTML代码，定位到以后给其添加上CSS样式。
    # id选择器
    # 类选择器
    # 标签选择器
    # 通配符选择器

\1、id（类似与关键字）选择器-不可重复
#1、作用：根据指定的id名称，在当前界面中找到对应的使用了此id名称的标签，然后设置属性。命名id时避免使用html中的其他标签名称或关键字。

#2、格式
id名称 {
    属性：值;
}

#3、注意点：
1、在企业开发中如果仅仅只是为了设置样式，通常不会使用id，在前端开发中id通常是留给js使用的。
2、每个标签都可以设置唯一一个id，id就相当于人/标签的身份证，因此在同一界面内id绝不能重复。
3、引用id一定要加#
4、id的命名只能由字符、数字、下划线组成，且不能以数字开头（字下美人其后数），更不能是html的关键字如p，a，img等。

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

\2、类选择器（写项目使用这个，专门为标签设置样式的选择器）
#1、作用：根据指定的类名称，在当前界面中找到对应的标签，然后设置属性。

#2、格式：
.类名称 {
    属性：值;
}

#3、注意点：
1、类名就是专门用来给某个特定的标签设置样式的
2、每个标签都可以设置一个或多个不同的class（空格分隔），class就相当于人名，因此同一界面内class可以重复。
3、定义class一定要加点.
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
                font-size: 50px;
            }
            .p3 {
                text-decoration: underline;
                /*下划线*/
            }
        </style>
    </head>
    <body>
        <p class="p1 p2">大多数人的帅，都是浮在表面的，是外表的帅</p>
        <p class="p2 p3">而EGON，不仅具备外表帅，内心更是帅了一逼</p>
        <p class="p1 p3">EGON就是我，我就是EGON</p>
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
   理由是：由于通配符选择器是设置界面上所有的标签的属性，所以在设置之前会遍历所有的标签。如果当前界面上的标签比较多，那么性能就会比较差。

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
        <h1>我是标题</h1>
        <p>我是段落</p>
        <a href="#">我是超链接</a>
    </body>
</html>
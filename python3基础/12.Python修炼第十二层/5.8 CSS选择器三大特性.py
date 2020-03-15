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
2、后面的覆盖前面的
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

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>
        <style type="text/css">
            #id1 {
                color: red;
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
    内联 > id > 类 > 标签 > 通配符(也算直接选中) > 继承 > 浏览器默认（即没有设置任何属性）
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

内联样式选择器权重  1000
id选择器权重       100
类选择器权重       10
元素选择器权重     1

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



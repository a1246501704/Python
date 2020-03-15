\二 层级选择器
    # 后代选择器
    # 子元素选择器
    # 相邻兄弟选择器
    # 通用兄弟选择器
\1、后代选择器
#1、作用：找到指定标签的所有后代（儿子，孙子，重孙子、、、）标签，设置属性
# 修改某个标签或id下的多个同级和子级下的某种标签的样式

#2、格式：
    标签名1 xxx {
        属性：值;
    }

#3、注意：
1、后代选择器必须用空格隔开
2、后代不仅仅是儿子，也包括孙子、重孙子
3、后代选择器不仅仅可以使用标签名称，还可以使用其他选择器比如id或class
4、后代选择器可以通过空格一直延续下去
5、如果有多个选择器匹配到了相同的标签，以层级写的最长的优先。

# 示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>

        <style type="text/css">
            # /*
            # .part1 p  {
            #     color: red;
            # }
            # */
            div p {
                color: red;
            }
            # #id1 li p {
            #     font-size: 50px;
            # }

            # div ul li a {
            #     font-size: 100px;
            #     color: green;
            # }
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

\2、子元素选择器（儿子选择器）
#1、作用：找到指定标签下的所有特定的直接子元素（不匹配子子元素），然后设置属性。

#2、格式：
    标签名称1>标签名称2 {
        属性：值;
    }
先找到名称叫做"标签名称1"的标签，然后在这个标签中查找所有直接子元素名称叫做"标签名称2"的元素，注意是用 > 大于号连接。

#3、注意：
1、子元素选择器之间需要用>符号链接，并且不能有空格
    比如 div>p 会找div标签层的所有后代标签名为"p"的标签
2、子元素选择器只会查找儿子，不会查找其他嵌套的标签
3、子元素选择器不仅可以用标签名称，还可以使用其他选择器,比如id或class
4、子元素选择器可以通过 > 符号一直延续下去

# 示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <style>
            /*
            #id1>p {
                color: red;
            }

            div p {
                color: red;
            }
            */
            .part1 ul .aaa>a {
                color: red;
            }
        </style>
    </head>
    <body>
      <p>我是body下的段落1</p>
        <div id="id1" class="part1">
            <p>我是div下的段落1</p>
            <p>我是div下的段落2</p>
            <a href="">点我啊1</a>
            <ul>
                <li class="aaa">
                    <p class="ccc">我是ul>li下的段落1</p>
                    <p class="ddd">我是ul>li下的段落</p>
                    <a href="">点我啊1</a>
                    <p>
                        <a href="">点我啊2</a>
                    </p>
                </li>
                <li>
                    <a href="#">点我啊3</a>
                </li>
            </ul>
        </div>
        <div>
            <p>hahahahah</p>
            <p>hahahahah</p>
        </div>
        <p>我是body下的段落2</p>
      <a href="#">百度一下</a>
    </body>
</html>


\3、相邻兄弟选择器，CSS2推出
#1、作用：选定紧跟其后的那个标签

#2、格式 
选择器1+选择器2 {
    属性：值;
}

#3、注意点：
1、毗邻选择器必须通过+号链接，选择器1标签相邻的是选择器2标签才会被选中。
2、毗邻选择器只能选中紧跟其后的那个标签，不能选中被隔开的标签。

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>

        <style type="text/css">
            /*相邻兄弟选择器*/
            h1+p {
            color: red;
            }
        </style>
    </head>
    <body>
        <h1>我是标题1</h1>
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

\4、通用兄弟选择器，CSS3推出
#1、作用：给指定选择器后面的所有选择器中的所有标签设置属性

#2、格式： 
选择器1~选择器2 {
    属性：值;
}

#3、注意点：
1、通用兄弟选择器必须用~来链接
2、通用兄弟选择器选中的是指选择器1后面同级的所有 选择器2的标签会被选中，匹配到 选择器1 同级所有的标签为 选择器2的标签。
3、无论有没有被隔开，都可以被选中。非本级的不会被选中。

# 示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>

        <style type="text/css">
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
        <div>
            <p>我是段落xxxxx</p>
        </div>
    </body>
</html>
\1、什么是CSS盒子模型？
HTML文档中的每个元素都被比喻成矩形盒子， 盒子模型通过四个边界来描述：
    margin（外边距）    # 用于控制元素与元素之间的距离；margin的最基本用途就是控制元素周围空间的间隔，从视觉角度上达到相互隔开的目的。
    border（边框）      # 用于控制内容与边框之间的距离；
    padding（内填充）   # 围绕在内边距和内容外的边框。可以用来把标签撑起来。
    content（内容区域） # 盒子的内容，显示文本和图像。
    
    如果把一个盒子比喻成一个壁挂相片，那么
        # 外边距margin ===== 一个相框与另外一个相框之间的距离
        # 边框border   ===== 边框指的就是相框
        # 内边距padding ===== 内容/相片与边框的距离
        # 宽度width/高度height ===== 指定可以存放内容/相片的区域
提示：可以通过谷歌开发者工具查看盒子的各部分属性
#如图所示：
   盒子模型：内容 —— 内填充 —— 边框 —— 外边距
        想要调整内容和边框之间的距离用： padding
        想要调整不同标签之间的距离用：margin


# margin 外边距
<style type="text/css">
    .margin-test {
        margin-top:5px;
        margin-right:10px;
        margin-bottom:15px;
        margin-left:20px;
    }
</style>

四个值简写：顺序（上右下左）
<style type="text/css">
    .margin-test {
        margin: 5px 10px 15px 20px;
    }
</style>

三个值简写：顺序（上 左右 下）
<style type="text/css">
    .margin-test {
        margin: 5px 10px 20px;
    }
</style>

常见居中简写：顺序（上下 右左）
<style type="text/css">
    .mycenter {
        margin: 0 auto;  # 0是上下   auto是左右
    }
</style>

# padding 内填充
<style type="text/css">
    .padding-test {
        padding-top: 5px;
        padding-right: 10px;
        padding-bottom: 15px;
        padding-left: 20px;
    }
</style>

推荐使用简写：
<style type="text/css">
    .padding-test {
        padding: 5px 10px 15px 20px;
    }
</style>

顺序：上右下左
补充padding的常用简写方式：
    提供一个，用于四边；
    提供两个，第一个用于上－下，第二个用于左－右；
    如果提供三个，第一个用于上，第二个用于左－右，第三个用于下；
    提供四个参数值，将按上－右－下－左的顺序作用于四边；


\2、盒子模型的宽度和高度
    1、内容的宽度和高度
        通过标签的width和height属性设置

    2、元素/盒子模型的宽度和高度
        宽度= 左边框 + 左内边距 + width(内容的宽) + 右内边距 + 右边框高度
        高度= 。。。。

    3、元素/盒子模型空间的宽度和高度
        宽度= 左外边距 + 左边框 + 左内边距 + width(内容的宽) + 右内边距 + 右边框高度 + 右外边距
        高度= 。。。。

# 示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>盒子模型宽度和高度</title>
        <style>
            span,a,b,strong {
                display: inline-block;
                width: 100px;
                height: 100px;
                border: 6px solid #000;
                padding: 20px;
                margin: 20px;
            }
        </style>
    </head>
    <body>
        <span>我是span</span>
        <a href="#"> 我是草链接</a>
        <b>我是加粗</b>
        <strong>我是强调</strong>
    </body>
</html>

# 补充：为什么 height:100%; 不起作用？
如何让 height:100% 起作用：你需要给这个元素的所有父元素的高度设定一个有效值。换句话说，你需要这样做：
现在你给div的高度为100%，它有两个父元素<body>和<html>。为了让你的div的百分比高度能起作用，你必须设定<body>和<html>的高度。

<html style="height: 100%;">
  <body style="height: 100%;">
    <div style="height: 100%;">
      <p>
        这样这个div的高度就会100%了
      </p>
    </div>
  </body>
</html>

相似的例子：可以查看qq注册界面https://ssl.zc.qq.com/v3/index-chs.html


\3、！！！css显示模式:块级、行内、行内块级
在HTML中HTML将所有标签分为两类，分别是 容器级 和 文本级
在CSS中CSS也将所有标签分为两类，分别是容器级是 块级元素 和 行内元素

1、HTML中容器级与文本级
    容器级标签：可以嵌套其他的所有标签
    div、h、ul>li、ol>li、dl>dt+dd

    文本级标签：只能嵌套文字、图片、超链接
    span、p、buis、strong、em、ins、del

2、CSS中块级与行内
    块级：块级元素会独占一行，所有的容器类标签都是块级，文本标签中的p标签也是块级
    div、h、ul、ol、dl、li、dt、dd   还有标签p

    行内：行内元素不会独占一行，所有除了p标签以外的文本标签都是行内
    span、buis、strong、em、ins、del

3、块级元素与行内元素的区别
    1、块级元素block
        独占一行
        可以设置宽高
            若没有设置宽度，那么默认和父元素一样宽（比如下例中的div的父元素是body，默认div的宽就是body的宽）
            若没有设置宽高，那么就按照设置的来显示

    2、行内元素inline
        不会独占一行
        不可以设置宽高
            盒子宽高默认和内容一样

    3、行内块级元素inline-block
        不会独占一行
        可以设置宽高
# 示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style>
            /*块级元素*/
            div,p,h1 {
                background-color: red;
                width: 200px;
                height: 100px;
            }

            /*行内元素*/
            span,b,strong {
                background-color: blue;
                width: 200px;
                height: 100px;
            }

            /*行内块级元素*/
            img {
                width: 100px;
                height: 100px;
            }

        </style>
    </head>
    <body>
        <!--块级-->
        <div>我是div</div>
        <p>我是段落 </p>
        <h1>我是标题</h1>
        <hr>

        <!--行内-->
        <span>我是span</span>
        <b>我是加粗</b>
        <strong>我是强调</strong>
        <hr>

        <!--行内块级-->
        <img src="../imags/1.png" alt="">
        <img src="../imags/1.png" alt="">
    </body>
</html>


\4、！！！CSS显示模式转换
属性	            描述	                                        值
display     可以通过标签的display属性设置显示模式        none HTML文档中元素存在，但是在浏览器中不显示。一般用于配合JavaScript代码使用
                                                    block 块级
                                                    inline 行内
                                                    inline-block 行内块级
display:"none"与visibility:hidden的区别：           visibility:hidden: 可以隐藏某个元素，但隐藏的元素仍需占用与未隐藏之前一样的空间。也就是说，该元素虽然被隐藏了，但仍然会影响布局。
                                                  display:none: 可以隐藏某个元素，且隐藏的元素不会占用任何空间。也就是说，该元素不但被隐藏了，而且该元素原本占用的空间也会从页面布局中消失。


\5、div与span
布局都是用块级元素，而行内元素是控制内容显示的。
1、div标签
   一般用于配合css完成网页的基本布局

2、span标签
  一般用于配合css修改网页中的一些局部信息，比如一行文字我们只为一部分加颜色<p>我是<span>egon</span></p>

3、div和span有什么区别？
    div一般用于排版，而span一般用于局部文字的样式
    1、站在HTML的角度：div是一个块级元素、独占一行，而span是一个行内元素、不会单独占一行
    2、站在CSS的角度：div是一个容器级标签，而span是一个文本级标签

示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>div与span标签</title>

        <style>
            .header {
                margin: 0 auto;

                width: 980px;
                height: 100px;
                background: pink;

                margin-bottom: 10px;
            }

            .content {
                margin: 0 auto;

                width: 980px;
                height: 500px;
                background: #e9ca37;

                margin-bottom: 10px;

            }

            .footer {
                margin: 0 auto;

                width: 980px;
                height: 100px;
                background: #7e1487;
            }

            .logo {
                width: 200px;
                height: 50px;
                background: #bfccdb;
                float: left;
                margin: 20px;
            }

            .nav {
                width: 600px;
                height: 50px;
                background: palegreen;
                float: right;
                margin: 20px;
            }

            .aside {
                width: 250px;
                height: 460px;
                background: #cccccc;
                float: left;
                margin: 20px;
            }

            .article {
                width: 650px;
                height: 460px;
                background: green;
                float: right;
                margin: 20px;
            }

            span {
                color: red;
            }

        </style>
    </head>
    <body>
        <div class="header">
            <div class="logo"></div>
            <div class="nav"></div>
        </div>
        <div class="content">
            <div class="aside">
                <p>
                    我是<span>EGON</span>，一个最接近<span>神的男人</span>
                </p>
            </div>
            <div class="article"></div>
        </div>
        <div class="footer"></div>
    </body>
</html>

\6、盒子模型各部分详解
# 1、border边框
同时设置四条边的边框	  border:边框的宽度 边框的样式 边框的颜色

分别设置四条边的边框	  border-left:边框的宽度 边框的样式 边框的颜色
                       border-top:边框的宽度 边框的样式 边框的颜色
                       border-right:边框的宽度 边框的样式 边框的颜色
                       border-bottom:边框的宽度 边框的样式 边框的颜色

分别指定宽度、格式、颜色   1、连写：（分别设置四条边的边框）
                        border-width: 上 右 下 左
                        border-style:上 右 下 左
                        border-color：上 右 下 左
                        2 、注意点：
                            1、这三个属性时按照顺时针，即上、右、下、左来赋值的
                            2、这三个属性的取值省略时的规律
                                省略右面，右面默认同左面一样
                                省略下面，下面默认跟上面一样
                                只留一个，那么其余三边都跟这一个一样

了解非连写                border-left-width: ;
                        border-left-style: ;
                        border-left-color: #000;

                        border-top-width: ;
                        border-top-style: ;
                        border-top-color: #000;

                        border-right-width: ;
                        border-right-style: ;
                        border-right-color: #000;

                        border-bottom-width: ;
                        border-bottom-style: ;
                        border-bottom-color: #000;

                        其他：
                        http://www.w3school.com.cn/cssref/pr_border-style.asp

边框的样式	              none 无边框。
                        dotted 点状虚线边框。
                        dashed 矩形虚线边框。
                        solid 实线边框。

border-radius	        /* 单独设置一个角：数值越大，弧度越大*/
                        border-top-left-radius: 20px;
                        border-top-right-radius: 20px;
                        border-bottom-left-radius: 20px;
                        border-bottom-right-radius: 20px;

                        /* 缩写设置 */
                        border-radius: 20px;/* 所有角设置相同值 */
                        border-radius: 20px 10px 10px 20px; /* 顺时针顺序：上左 上右 下左 下右*/

                        /* 百分比设置 */
                        border-radius: 50%;

                        /* 椭圆圆弧设置 */
                        border-radius: 25%/50%; /* 前面一个值代表水平方向的半径占总宽度的，后面一个值代表垂直方向 */
边框练习
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>边框属性</title>
        <style>
            div {
                width: 100px;;
                height: 100px;
            }

            .box1 {
                /*border: 5px solid black;*/

                /*border-left: 5px solid black;*/
                /*border-top: 5px solid black;*/
                /*border-right: 5px solid black;*/
                /*border-bottom: 5px solid black;*/

                border-width: 5px;
                border-style: solid;
                border-color: black;
            }

            .box2 {
                /*border-left: 5px solid purple;*/
                /*border-top: 5px solid red;*/
                /*border-right: 5px solid green;*/
                /*border-bottom: 5px solid blue;*/

                border-width: 5px;
                border-style: solid;
                border-color: red green blue purple;

            }

            .box3 {
                /*border: 5px solid red;*/
                /*border-right: 5px dashed red;*/


                border-width: 5px;
                border-style: solid dashed solid solid;
                border-color: red;
            }

            .box4 {
                border-width: 5px;
                border-style: solid dashed solid dashed;
                border-color: red;
            }

            .box5 {
                border:5px solid black;
                border-bottom: none;
            }

            /*！！！在企业开发中要尽量降低网页的体积，图片越多，体积肯定越大，访问速度肯定越慢，所以针对简单的图形，可以只用用边框画出来
            使用下面的方法制作就可以
            */
            .box6 {
                    width: 0px;
                    height: 0px;
                    border-width:25px;
                    border-style: solid;
                    border-color: black white skyblue white;
                    border-bottom: none;
                }
        </style>
    </head>
    <body>
        <div class="box1"></div>
        <hr>
        <div class="box2"></div>
        <hr>
        <div class="box3"></div>
        <hr>
        <div class="box4"></div>
        <hr>
        <div class="box5"></div>
        <hr>
        <div class="box6"></div>
    </body>
</html>


# border-radius练习1
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>

        <style type="text/css">
            .box1 {
                margin: 0 auto;
                height: 100px;
                width: 920px;
                border-radius: 5px 5px 0px 0px;
                background-color: blue;
            }
        </style>
    </head>
    <body>
        <div class="box1"></div>
    </body>
</html>


# border-radius练习
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style type="text/css">
            img {
                width: 185px;
                border-radius: 50%;
            }
        </style>
    </head>
    <body>
        <img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180511163924274-1737036731.png" alt="">
    </body>
</html>




# 2、padding内边距：边框与内容的距离就是内边距
非连写          padding-top：20px；
               padding-right：20px；
               padding-bottom：20px；
               padding-left：20px；
连写            padding：上 右 下 左;

注意	    1 给标签设置内边距后，标签内容占有的宽度和高度会发生变化，设置padding之后标签内容的宽高是在原宽高的基础上加上padding值。如果不想改变实际大小，那就在用宽高减掉padding对应方向的值
           2 padding是添加给父级的，改变的是父级包含的内容的位置
           3 内边距也会有背景颜色

# 内边距练习
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>内边距属性</title>
        <style>
            div {
                width: 100px;
                height: 110px;
                border: 1px solid red;
            }

            .box1 {
                padding-top: 30px;
            }

            .box2 {
                padding-right: 40px;
            }

            .box3 {
                padding-bottom: 50px;
            }

            .box4 {
                padding-left: 60px;
            }

            .box5 {

                /*只留一个。全都相等*/
                padding: 70px;
                background-color: red;
            }
        </style>
    </head>
    <body>

        <div class="box1">
            我是文字我是文字我是文字我是文字我是文字我是文字我是文字
        </div>

        <hr>
        <div class="box2">
            我是文字我是文字我是文字我是文字我是文字我是文字我是文字
        </div>

        <hr>
        <div class="box3">
            我是文字我是文字我是文字我是文字我是文字我是文字我是文字
        </div>

        <hr>
        <div class="box4">
            我是文字我是文字我是文字我是文字我是文字我是文字我是文字
        </div>

        <hr>
        <div class="box5">
            我是文字我是文字我是文字我是文字我是文字我是文字我是文字
        </div>

    </body>
</html>


# 添加边框与padding后保持盒子大小不变：方式一 做减法
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style type="text/css">

            .box1 {
                /*width: 100px;*/
                /*height: 100px;*/
                background-color: red;
                border: 10px solid #000;
                padding: 10px;

                width: 60px;
                height: 60px;
            }
        </style>
    </head>
    <body>
        <div class="box1">我是文字</div>
    </body>
</html>

# 添加边框与padding后保持盒子大小不变：方式二 box-sizing
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style type="text/css">

            .box1 {
                width: 100px;
                height: 100px;
                background-color: red;
                border: 10px solid #000;
                padding: 10px;

                /*本质原理就是做减法*/
                box-sizing: border-box;
            }
        </style>
    </head>
    <body>
        <div class="box1">我是文字</div>
    </body>
</html>


# 3、外边距：标签与标签之间的距离就是外边距
非连写           margin-top：20px；
                margin-right：20px；
                margin-bottom：20px；
                margin-left：20px；
连写            margin：上 右 下 左;
注意	        1、外边距的那一部分是没有背景颜色的
                2、外边距合并现象
                    在默认布局的水平方向上，默认两个盒子的外边距会叠加
                    而在垂直方向上，默认情况下两个盒子的外边距是不会叠加的，会出现合并现象，谁的外边距比较大，就听谁的

# 外边距合并现象
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>外边距合并现象
        </title>
        <style>
            span {
                display: inline-block;
                width: 100px;
                height: 100px;
                border: 1px solid #000;
            }

            div {
                height: 100px;
                border: 1px solid #000;
            }

            /*水平方向上。外边距会叠加*/
            .hezi1 {
                margin-right: 50px;
            }

            .hezi2 {
                margin-left: 100px;
            }

            /*垂直方向上。外边距不会叠加，会合并成一个，谁比较大就听谁的*/
            .box1 {
                margin-bottom: 50px;
            }

            .box2 {
                margin-top: 100px;
            }
        </style>
    </head>
    <body>
        <!--
        快捷创建
        span.hezi${我是span}*2
        -->
        <span class="hezi1">我是span</span><span class="hezi2">我是span</span>
        <div class="box1">我是div</div>
        <div class="box2">我是div</div>
    </body>
</html>

# margin-top塌陷
两个嵌套的盒子，内层盒子设置margin-top后会将外层盒子一起顶下来，解决方法如下：
    1、外部盒子设置一个边框
    2、外部盒子设置 overflow: hidden; 当子元素的尺寸超过父元素的尺寸时，内容会被修剪，并且其余内容是不可见的，此属性还有清除浮动、清除margin-top塌陷的功能。
    3、使用伪元素类：
    .clearfix:before{
        content: '';
        display:table;
    }

#示范
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>盒子模型宽度和高度</title>
        <style>
            .outter {
                background-color: green;
                width: 300px;
                height: 300px;

                /*方式一*/
                /*border: 1px solid #000;*/

                /*方式二*/
                /*overflow: hidden;*/
            }
            .inner {
                background-color: red;
                width: 200px;
                height: 200px;

                margin-top: 100px;
            }

            /*方式三*/
            .clearfix:before {
                display: table;
                content: "";
            }

        </style>
    </head>
    <body>
        <div class="outter clearfix">
            <div class="inner"></div>
        </div>
    </body>
</html>



# 4、内边距vs外边距
#1、在企业开发中，一般情况下如果需要控制嵌套关系盒子之间的距离
       应该首先考虑padding
       其次再考虑margin
       margin本质上是用于控制兄弟直接的关系的，padding本质才是控制父子关系的关系 

示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style>
            .egon {
                width: 300px;
                height: 300px;
                background-color: yellow;
                padding: 50px;
                box-sizing: border-box;
            }

            .alex {
                width: 100px;
                height: 100px;
                background-color: green;
            }

            .linhaifeng {
                width: 300px;
                height: 300px;
                background-color: purple;
                padding: 50px;
                box-sizing: border-box;

                margin-top: 100px;
            }

            .liuqingzheng {
                width: 100px;
                height: 100px;
                background-color: blue;
            }
        </style>
    </head>
    <body>
        <div class="egon">
            <div class="alex"></div>
        </div>

        <div class="linhaifeng">
            <div class="liuqingzheng"></div>
        </div>
    </body>
</html>

#2、如果两个盒子是嵌套关系，那么设置了里面一个盒子顶部的外边距，那么外面一个盒子也会被顶下来
       如果外面的盒子不想被遗弃顶下来，，那么可以给外面的盒子设置一个边框属性

示范
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>

        <style>

            .egon {
                width: 300px;
                height: 300px;
                background-color: yellow;
                box-sizing: border-box;

                border: 1px solid #000;
            }

            .alex {
                width: 100px;
                height: 100px;
                background-color: green;

                margin-top: 50px;
            }

        </style>
    </head>
    <body>
        <div class="egon">
            <div class="alex"></div>
        </div>
    </body>
</html>

# 5、盒子居中与内容居中
内容居中
1、让一行内容在盒子中水平且垂直居中
    /*水平居中*/
    text-align: center;
    /*垂直居中*/
    line-height: 500px;

2、让多行内容在盒子中垂直居中（水平居中与单行内容一样）
让行高与盒子高度一样，只能让一行内容垂直居中，如果想让多行内容垂直居中，

比如下面这种，想让div中的多行内容垂直居中，一看div中的文字是两行，每一行
的行高为20，加起来就是40，80-40=40，需要让文字距离顶部pading为20，底部padding为20
*/
height: 80px;
line-height: 20px;

padding-top: 20px;
padding-bottom: 20px;
box-sizing: border-box;

示范
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>盒子居中和内容居中</title>
        <style>
            div {
                width: 300px;
                height: 300px;
                background-color: red;

                /*多行内容水平居中与单行一样*/
                text-align: center;

                /*多行内容垂直居中*/
                line-height: 30px;
                padding-top: 120px;
                box-sizing: border-box;
            }
        </style>
    </head>
    <body>
        <div>
            我是文字我是文字我是文字我是文字我是文字我是文字我是文字
        </div>
    </body>
</html>

盒子居中
text-align center；只能让盒子中存储的文字、图片水平居中
如果想让盒子自己相对于父元素水平居中，需要用到
margin: 0 auto;

示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>盒子居中和内容居中</title>
        <style>
            .son {
                width: 300px;
                height: 300px;
                background-color: red;

                /*多行内容水平居中与单行一样*/
                text-align: center;

                /*多行内容垂直居中*/
                line-height: 30px;
                padding-top: 120px;
                box-sizing: border-box;

                /*盒子本身水平居中*/
                margin: 0 auto;

            }

            .father {
                width: 500px;
                height: 500px;
                background-color: yellow;
            }
        </style>
    </head>
    <body>
        <div class="father">
            <div class="son">
                我是文字我是文字我是文字我是文字我是文字我是文字我是文字
            </div>
        </div>
    </body>
</html>


# 6、防止文字溢出word-break: break-all;
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>欢迎界面</title>
        <style type="text/css">

            div {
                width: 200px;
                height: 200px;

                /*字母、数字溢出，可以用下列属性控制自动换行：允许在单词内换行。
                http://www.w3school.com.cn/cssref/pr_word-break.asp
                */
                word-break: break-all;
            }

            .box1 {
                background-color: red;

            }
            .box2 {
                background-color: green;
            }

            .box3 {
                background-color: blue;
            }
        </style>
    </head>
    <body>
        <div class="box1">
            <p>asdfasdfsadfasdfasdfasdfad sfasdfsadasDSfafsafaasdfasdfasfdqwerqwerwqersdfqerwrsdf你好我的啊啊啊啊啊啊啊啊啊啊啊啊</p>
        </div>
        <div class="box2">遗憾白鹭上青天两个黄鹂鸣翠柳啊哈哈哈
        </div>
        <div class="box3">我是12312312312312312312312312312312312312312312312312312312312我
        </div>
    </body>
</html>


# 7、清除默认边距
#1、为什么要清空默认边距（外边距和内边距）
浏览器会自动附加边距，在企业开发中为了更好的控制盒子的宽高和计算盒子的宽高等等
编写代码之前的第一件事情就是清空默认的边距，不同的浏览器可能默认的边距大小不太一样。

#2、如何清空默认的边距
        * {
            margin: 0px;
            padding: 0px;
        }

#3、注意点：
    通配符选择器会找到（遍历）当前界面中所有的标签，所以性能不好，参考：https://yuilibrary.com/yui/docs/cssreset/
    拷贝代码：
    body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,code,form,fieldset,legend,input,textarea,p,blockquote,th,td{margin:0;padding:0}
    可以查看京东，bat主页也是这么做的，在企业开发中也应该像上面这么写

示范
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>清除默认边距</title>
        <style>

            /*
            * {
                margin: 0px;
                padding: 0px;
            }
            */

            body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,code,form,fieldset,legend,input,textarea,p,blockquote,th,td{margin:0;padding:0}
            
            .box1 {
                width: 100px;
                height: 100px;
                background-color: green;
            }
            .box2 {
                width: 100px;
                height: 100px;
                background-color: yellow;
            }
            .box3 {
                width: 100px;
                height: 100px;
                background-color: blue;
            }
        </style>
    </head>
    <body>
        <div class="box1"></div>
        <div class="box2"></div>
        <div class="box3"></div>
    </body>
</html>









 







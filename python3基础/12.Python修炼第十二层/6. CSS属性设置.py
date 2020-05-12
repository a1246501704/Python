\CSS属性设置
# 字体属性
# 文本属性
# 背景属性
# 盒子模型
# 盒子模型各部分详解


\一 字体属性
# 1、font-weight：文字粗细
取值	 描述
normal	# 默认值，标准粗细
bord	# 粗体
border	# 更粗
lighter	# 更细
100~900	# 设置具体粗细，400等同于normal，而700等同于bord
inherit	# 继承父元素字体的粗细值


# 2、font-style：文字风格
 normal  # 正常，默认就是正常的
 italic  # 倾斜 

# 3、font-size：文字大小
fs：一般是12px或13px或14px
注意：
1、通过font-size设置文字大小一定要带单位，即一定要写px
2、如果设置成inherit表示继承父元素的字体大小值。


# 4、font-family：文字字体
font-family: "Microsoft Yahei", "微软雅黑", "Arial", sans-serif

常见字体：
serif      # 衬线字体
sans-serif # 非衬线字体
中文：宋体，微软雅黑，黑体

注意：
    1、设置的字体必须是用户电脑里已经安装的字体，浏览器会使用它可识别的第一个值。
    2、如果取值为中文，需要用单或双引号扩起来

# 5、文字属性简写 
font-weight: bolder;
font-style:  italic;
font-size:   50px;
font-family: 'serif','微软雅黑';
简写为
font: bolder italic 50px 'serif','微软雅黑'; 

# 6、color：文字颜色
取值	            格式	                                描述
英文单词           color：red;            大多数颜色都有对应的英文单词描述，但英文单词终究有其局限性:无法表示所有颜色

                                        什么是三原色？
                                        red，green，blue
                                        什么是像素px？
                                        对于光学显示器，一整个屏幕是有一个个点组成，每一个点称为一个像素
                                        点，每个像素点都是由一个三元色的发光元件组成，该元件可以发出三种颜
rgb	            color：rgb(255,0,0)	    色，red，green，blue。
                                        发光元件协调三种颜色发光的明亮度可以调节出其他颜色
                                        格式：rgb(255,0,0);
                                        参数1控制红色显示的亮度
                                        参数2控制绿色显示的亮度
                                        参数3控制蓝色色显示的亮度

                                        数字的范围0-255，0代表不发光，255代表发光，值越大越亮

                                        红色：rgb(255,0,0)
                                        绿色：rgb(0,255,0)
                                        蓝色：rgb(0,0,255)
                                        黑色：rgb(0,0,0) # 所有都不亮
                                        白色：rgb(255,255,255) # 所有都最亮
                                        灰色：只要让红色/绿色/蓝色的值都一样就是灰色，而且三个值越小，越偏
                                        黑色，越大越偏白色

rgba	        color：rgba(255,0,0,0.1);	rgba到css3中才推出，比起rgb多了一个a，a代表透明度
                                            a取值0-1，取值越小，越透明

十六进制	     color: #FF0000;	     #FFEE00 其中FF代表R，EE代表G，00代表B
                                        只要十六进制的颜色每两位都是一样的，那么就可以简写为一个，
                                        例如#F00 等同于#FF0000



\二 文本属性
# 1、text-align：规定元素中的文本的水平对齐方式。
值	            描述
left	    # 左边对齐 默认值
right	    # 右对齐
center	    # 居中对齐
justify	    # 两端对齐

# 2、text-decoration：文本装饰
值	                描述
none	        # 默认。定义标准的文本，通常用来去掉a标签的下划线
underline	    # 定义文本下的一条线。
overline	    # 定义文本上的一条线。
line-through	# 定义穿过文本下的一条线。
inherit	        # 继承父元素的text-decoration属性的值。

# 3、text-indent：首行缩进
#将段落的第一行缩进 32像素,16px;=1em;
p {
  text-indent: 32px;
}

# 4、line-height：行高
        见图

# 示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>

        <style type="text/css">
            p {
                width: 500px;
                height: 200px;
                background-color: yellow;
                text-align: center;
                text-decoration: underline;
                line-height: 200px;
            }
            a {
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div>
            <p>hello英雄不问出处，流氓不论岁数</p>
            <a href="#">点我啊</a>
        </div>
    </body>
</html>


\三 背景属性
注意：没有宽高的标签，即便设置背景也无法显示

        属性	                描述	                    值
background-color	        设置标签的背景颜色的       background-color: red;
                                                    background-color: rgb(0,255,0);
                                                    background-color: rgba(0,255,0,0.1);
                                                    background-color: #00ffff;

background-image	        设置标签的背景图片         background-image: url("images/2.jpg");
                                                    background-image: url("图片网址");
                                                    注意：如果图片的大小没有标签的大小大，那么会自动在水平和锤子方向平铺和填充

background-size	            设置标签的背景图片的宽、高  background-size: 300px 300px;
                                                    background-size: 100% 100%;

ckground-repeat	            设置标签的背景图片的平铺方式 background-repeat: repeat;    # 默认值，在垂直和水平方向都重复
                                                    background-repeat: no-repeat; # 不重复，背景图片将仅显示一次
                                                    background-repeat: repeat-x;  # 背景图片将在水平方向平铺
                                                    background-repeat: repeat-y;  # 背景图片将在垂直方向平铺
                                                    应用：可以在服务端将一个大图片截成小图片，然后在客户端基于平铺属性将小图重复
                                                    这样用户就以为是一张大图，如此，既节省了流量提升了速度，又不影响用户访问
                                                    例如很多网站的导航条都是用这种手法制作的

background-attachment	    设置标签的背景图片在标签中固定或随着页面滚动而滚动  background-attachment: scroll; # 默认值，背景图片会随着滚动条的滚动而滚动
                                                                        background-attachment: fixed;  # 背景图片固定不动，不会随着滚动条的滚动而滚动

ackground-position	        前端的坐标系"：                                             background-position：水平方向的值，垂直方向的值
                            -------------------->x轴                                  1、具体的方位名词
                            |                                                           水平方向：left，center，right
                            |                                                           垂直方向：top，center，bottom
                            |                                                           如果只设置了一个关键词，那么第二个值就是"center"。
                            |                                                         2、百分比
                            |                                                            第一个值是水平位置，第二个值是垂直位置。
                            |                                                            左上角是 0% 0%。右下角是 100% 100%。
                            y轴                                                          如果只设置了一个值，另一个值就是50%。
                            图片默认都是在盒子的左上角，                                   3、具体的像素（一定要加px单位）
                            background-position：属性，就是专门用于控制背景图片的位置           例如：30px，50px等等
                                                                                          第一个值是水平位置，第二个值是垂直位置。
                                                                                          左上角是 0 0。单位是像素 (0px 0px) 或任何其他的 CSS 单位。
                                                                                          如果只设置了一个值，另一个值就是50%。
                                                                                          可以混合使用%和position值。
# 1、背景属性缩写
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>

        <style type="text/css">
            div {
                width: 500px;
                height: 500px;
                /*background-color: red;*/
                /*background-image: url("https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180510215639652-367382094.jpg");*/
                /*background-repeat: no-repeat;*/
                /*background-position: right bottom;*/
                /*background-size: 100px 100px;*/
                background: red url("https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180510215639652-367382094.jpg") no-repeat right bottom/100px 100px;
            }
        </style>
    </head>
    <body>
        <div></div>
    </body>
</html>

# 2、背景图片和插入图片的区别
#1、
背景图片仅仅只是一个装饰，不会占用位置，
插入图片会占用位置

#2、
背景图片有定位属性，可以很方便地控制图片的位置，
而插入图片则不可以

#3、
插入图片语义比背景图片的语义要强，所以在企业开发中如果你的图片
想被搜索引擎收录，那么推荐使用插入图片


# 练习
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>后代选择器</title>

        <style type="text/css">
            .box1 {
                width: 200px;
                height: 200px;
                background-color: red;
                background-image: url("https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180510214613754-737636530.jpg");
                background-repeat: no-repeat;
                background-position: right bottom;
            }
            .box2{
                width: 300px;
                height: 300px;
                background-color: green;
            }
        </style>
    </head>
    <body>
        <div class="box1">
        </div>
        <div class="box2">
            <img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180510214613754-737636530.jpg" alt="">
        </div>
    </body>
</html>


# 3、背景图片练习

<!--背景图片居中显示-->
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>图片居中显示</title>

        <style type="text/css">
            div {
                height: 500px;
                background-image: url("bg2.jpg");
                background-position: top center;
            }
        </style>
    </head>
    <body>
        <div></div>
    </body>
</html>


<!--图片拼接-->
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>图片拼接</title>

        <style type="text/css">
            div {
                height: 720px;
                background-image: url("bg1.jpg");

            }
            .box2 {
                background-image: url("ksyx.png");
                background-position: bottom center;
                background-repeat: no-repeat;
            }
        </style>
    </head>
    <body>
        <div class="box1">
            <div class="box2"></div>
        </div>
    </body>
</html>


<!--导航条-->
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>导航条</title>

        <style type="text/css">
             .navbar {
                 margin: 0 auto;
                 width: 920px;
                 height: 50px;
                 background-image: url("dht.png");
                 background-repeat: repeat-x;
            }
        </style>
    </head>
    <body>
        <div class="navbar"></div>
    </body>
</html>

# 4、rgba与opacity
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style>
            .c1 {
                width: 200px;
                height: 200px;
                /*只能给背景设置透明度*/
                /*background-color: rgba(0,0,0,0.65);*/
                background-color: rgb(0,0,0);
                opacity: 0.65; /*改变整个标签的透明度*/
            }
        </style>
    </head>
    <body>
        <div class="c1">我是我啊啊啊啊</div>
    </body>
</html>


<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
        <style>
            .c1 {
                height: 800px;
                /*背景颜色不能与背景颜色同时使用，如果想给背景图片设置透明度，则必须使用opacity*/
                background-image: url("https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180516225809591-1990809146.jpg");
                background-size:300px auto;
                opacity: 0.55; /*改变整个标签的透明度*/
            }
        </style>
    </head>
    <body>
        <div class="c1"></div>
    </body>
</html>
　　 
# 5、精灵图
#1、什么是CSS精灵图（可以通过浏览器抓包分析：微博，京东都有精灵图）
    CSS精灵图是一种图像合成技术

#2、CSS精灵图的作用
    一个电商网站可能有很多图片，比如有10张图片，这就要求客户端发10次请求给服务端
    但其实一次请求的带宽就足够容纳10张图片的大小
    精灵图的作用就是用来较少请求次数，以及降低服务器处理压力

#3、如何使用CSS精灵图
    CSS的精灵图需要配合背景图片和背景定位来使用

#4、强调：切图需要用到frameworks软件，可以知道每个图片具体宽多少个像素高多少个像素，该软件与ps属于一个家族
    在右面，图层-》位图-》出一把锁固定住图片
    然后左侧，有一个切片工具，框住图片

　　

\边框
边框属性 
    border-width  # 边框宽度
    border-style  # 边框样式
    border-color  # 边框颜色
#d1 {
  border-width: 2px;   
  border-style: solid; 
  border-color: red;   
}

通常使用简写方式：
#d1 {
  border: 2px solid red;
}

边框样式
值	      描述
none	# 无边框。
dotted	# 点状虚线边框。
dashed	# 矩形虚线边框。
solid	# 实线边框。

除了可以统一设置边框外还可以单独为边框某一个边设置样式，如下所示：
#d1 {
  border-top-style:dotted;
  border-top-color: red;
  border-right-style:solid;
  border-bottom-style:dotted;
  border-left-style:none;
}

# border-radius
用这个属性能实现圆角边框的效果。将border-radius设置为长或高的一半即可得到一个圆形。

# display属性
用于控制HTML元素的显示效果。
    值	                                意义
display:"none"	        # HTML文档中元素存在，但是在浏览器中不显示。一般用于配合JavaScript代码使用。
display:"block"	        # 按块级标签显示 默认占满整个页面宽度，如果设置了指定宽度，则会用margin填充剩下的部分。按照块级就可以设置宽和高了
display:"inline"	    # 按行内元素显示，此时再设置元素的width、height、margin-top、margin-bottom和float属性都不会有什么影响。
display:"inline-block"	# 使元素同时具有 行内元素和块级元素的特点。

display:"none" 与 visibility:hidden 的区别：
visibility:hidden:  # 可以隐藏某个元素，但隐藏的元素仍需占用与未隐藏之前一样的空间。也就是说，该元素虽然被隐藏了，但仍然会影响布局。
display:none:       # 可以隐藏某个元素，且隐藏的元素不会占用任何空间。也就是说，该元素不但被隐藏了，而且该元素原本占用的空间也会从页面布局中消失。



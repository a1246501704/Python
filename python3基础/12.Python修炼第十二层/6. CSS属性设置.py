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
100~900	# 设置具体粗细，400等同于normal，而700等同于bold
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

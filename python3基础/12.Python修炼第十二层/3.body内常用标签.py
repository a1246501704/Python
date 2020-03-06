\HTML常用标签

\标签分类:
	块儿级标签            <h1> ~ <h6>,<div>,<p>,<hr>,<ul>,<li>, <ol>, <h1>, <table>
		默认占浏览器宽度
		能设置长和宽
	内联标签(行内标签)     <a>,<img> ,<u>, <s>, <i>, <b>,<td>, <span>     
		根据内容决定长度
		不能设置长和宽
\标签的嵌套规则
	1. 行内标签不能嵌套块级标签
	2. p标签不能嵌套块级标签

\HTML语义化
# 对于那些只用来修改样式的标签将会被淘汰掉，比如以下标签都是没有语义的，都是用来修改样式的。统统使用CSS加样式。
#1、<br> 换行
    我是帅气逼人的Egon老师
    <br>
    我是帅气逼人的Egon老师
    我是帅气逼人的Egon老师
    我是帅气逼人的Egon老师

#2、<hr> 分割线

#3、<font> 修改文字大小，颜色
    <font color="red" size="10px">我是哈哈哈</font>

#4、<b>加粗</b> 加粗
    <b>论颜值，我秒杀宇宙</b>

#5、<u>下划线</u> 下划线

#6、<i>斜体</i> 倾斜

#7、<s>删除</s> 删除线

html5中推出了一些新的标签
        strong == b
        ins    == u
        em     == i
        del    == s

新的标签是有语义的，而老的只是单纯的添加样式（这是CSS干的事）
        strong的语义：定义重要性强调的文字
        ins的语义（inserted）：定义插入的文字
        em的语义（emphasized）：定义强调的文字
        del的语义（deleted）：定义被删除的文字

\字符实体
#1、在HTML中对空格／回车／tab不敏感，会把多个空格／回车／tab当作一个空格来处理
#2、字符实体指的是
在HTML中
有的字符是被HTML保留的比如大于号小于号
有的HTML字符，在HTML中是有特殊含义的，是不能在浏览器中直接显示出来的，那么这些东西想显示出来就必须通过字符实体，如下

注释：实体名称对大小写敏感！
# 内容	对应代码
  空格	&nbsp;
  >	    &gt;
  <	    &lt;
  &	    &amp;
  ¥	    &yen;
  版权	&copy;
  注册	&reg;
# 特殊符号对照表：http://tool.chinaz.com/Tools/HtmlChar.aspx


\h系列标签 标题
# 语义：标记内容为一个标题，全称headline
h系列标签从h1-h6共6个，没有h7标签，标记内容为1~6级标题，h1用作主标题（代表最重要的），其实是h2。。。
虽然h1-h6标签的显示样式是从大到小，但再次强调：记忆HTML标签的显示样式是没有意义的

<!DOCTYPE HTML>
<html>
    <head lang='en'>
        <meta charset="utf-8">
        <title>Egon才华无敌</title>
    </head>
    <body>
        <h1>一级标题</h1><h2>二级标题</h2>
        <h3>三级标题</h3>
        <h4>四级标题</h4>
        <h5>五级标题</h5>
        <h6>六级标题</h6>
        <h7>没有七级标题</h7>
        没有七级标题
    </body>
</html>

<h1> 定义标题的开始。
<h1 align="center">      # 拥有关于对齐方式的附加信息。居中排列标题
<body bgcolor="yellow">  # 拥有关于背景颜色的附加信息。

注意：在企业开发中一定要慎用h系列标签，特别是h1标签，在企业开发中一般一个界面中只能出现一个h1标签（出于SEO考虑，搜索引擎会使用标题将网页的结构和内容编制索引）,比如www.163.com。

\p标签 段落
# 语义：标记内容为一个段落，全称paragraph段落

注释：浏览器会自动地在段落的前后添加空行。（<p> 是块级元素）
提示：使用空的段落标记 <p></p> 去插入一个空行是个坏习惯。用 <br /> 标签代替它！（但是不要用 <br /> 标签去创建列表。不要着急，您将在稍后的篇幅学习到 HTML 列表。）
<!DOCTYPE HTML>
<html>
    <head lang='en'>
        <meta charset="utf-8">
        <title>Egon无敌</title>
    </head>
    <body>
        <h1>Egon</h1>
        <p>论颜值，鹤立鸡群</p>
        <p>论才华，天下无敌</p>
    </body>
</html>

\img标签 图像  https://www.w3school.com.cn/html/html_images.asp
# 语义：标记一个图片，全称image
# 用法
<img src="本地或网络图片地址" alt="图片加载失败时显示的内容" title = "鼠标悬停到图片上时显示的内容" />
<img src="本地或网络图片地址" alt="图片加载失败时显示的内容" title = "鼠标悬浮时提示信息" width="宽" height="高(宽高两个属性只用一个会自动等比缩放)">

#2、注意
2.1 src指定的图片地址可以是网络地址，也可以是一个本地地址，本地地址可以用绝对或相对路径，但通常用相对路径，相对路径是以html文件当前所在路径为基准进行的
  <img src="/images/a.jpg" alt="图片加载失败时显示的内容" title = "鼠标悬停到图片上时显示的内容" />
2.2 图片的格式可以是png、jpg和gif
2.3 alt="图片加载失败时显示的内容"  为img标签加上该属性可用于支持搜索引擎和盲人读屏软件。
2.4 title = "鼠标悬停到图片上时显示的内容"
2.5 如果没有指定图片的width和height则按照图片默认的宽高显示，如果指定图片的width和height则可能让图片变形，那如果又想指定宽度和高度，又不想让图片变形，我们可以只指定宽度和高度的一个值即可
只要指定了一个值，浏览器会根据该值计算另外一个值，并且都是等比拉伸的，图片将不会变形



\a标签 超链接  https://www.w3school.com.cn/html/html_links.asp
# 语义：标记一个内容为超链接，全称anchor，锚
# 超链接标签是超文本文件的精髓，可以控制页面与页面之间的跳转。 
# HTML 链接是通过 <a> 标签进行定义的，在 href 属性中指定链接的地址。
所谓的超链接是指从一个网页指向一个目标的连接关系，这个目标可以是另一个网页，也可以是相同网页上的不同位置，还可以是一个图片，一个电子邮件地址，一个文件，甚至是一个应用程序。
  <a href="跳转到的目标页面地址" target="是否在新页面中打开" title="鼠标悬浮显示的内容">需要展现给用户查看的内容/也可以是图片</a>
  <a href="http://www.oldboyedu.com" target="_blank" >点我</a>
  <a href="http://www.w3school.com.cn/">Visit W3School</a>
  <p><a href="/index.html">本文本</a> 是一个指向本网站中的一个页面的链接。</p>
  <p><a href="http://www.microsoft.com/">本文本</a> 是一个指向万维网上的页面的链接。</p>
  # 将图像作为链接
  <p>您也可以使用图像来作链接：<a href="/example/html/lastpage.html"><img border="0" src="/i/eg_buttonnext.gif" /></a></p>

href属性指定目标网页地址。该地址可以有几种类型：
    绝对URL - 指向另一个站点（比如 href="http://www.jd.com）
    相对URL - 指当前站点中确切的路径（href="index.htm"）
    锚URL   - 指向页面中的锚（href="#top"）

target：
    _blank # 表示在新标签页中打开目标网页
    _self  # 表示在当前标签页中打开目标网页，默认的

name 属性：
    name 属性规定锚（anchor）的名称。
    您可以使用 name 属性创建 HTML 页面中的书签。
    书签不会以任何特殊方式显示，它对读者是不可见的。
    当使用命名锚（named anchors）时，我们可以创建直接跳至该命名锚（比如页面中某个小节）的链接，这样使用者就无需不停地滚动页面来寻找他们需要的信息了。
    命名锚的语法：
        <a name="label">锚（显示在页面上的文本）</a>
        提示：锚的名称可以是任何你喜欢的名字。
        提示：您可以使用 id 属性来替代 name 属性，命名锚同样有效。

    实例
        首先，我们在 HTML 文档中对锚进行命名（创建一个书签）：
        <a name="tips">基本的注意事项 - 有用的提示</a>
        然后，我们在同一个文档中创建指向该锚的链接：
        <a href="#tips">有用的提示</a>


#2、注意：
2.1 a标签不仅可以标记文字，也可以标记图片
    <a href="https://www.baidu.com"><img src="mv.png" />百度一下，你就知道</a>

2.2 a标签必须有href属性，href的值必须是http://或https://开头

2.3 a标签还可以跳转到自己的页面
    <a href="template/aaa.html">锤你胸口</a>

2.4 target="_blank"代表在新页面中打开，其余的值均无需记忆，
    如果页面中大量的a标签都需要设置target="_blank",那么我们可以在head标签内新增一个base标签进行统一设置
    <base target="_blank">
    如果a标签自己设置了target，那么就以自己的为准，否则就会参照base的设置

2.5 title="鼠标悬浮显示的内容"

假链接
#1、什么是假链接？
    就是点击之后不会跳转的链接，我们称之为假链接

#2、假链接存在的意义：
    在企业开发前期，其他界面都还没有写出来，
    那么我们就不知道应该跳转到什么地方，所以就只能使用假链接来代替

#3、假链接的定义格式
    1、href="#"   :会自动回到网页的顶部
    2、href="javascript:" ：不会返回顶部

页面内锚点
#1、要想通过a标签跳转到指定的位置，那么必须告诉a标签一个独一无二的身份证号码，
这样a标签才能在当前界面中找到需要跳转到的目标位置

#2、如何为html中的标签绑定一个独一无二的身份证号码呢？
在html中，每一个标签都有一个名称叫做id的属性
这个属性就是用来给标签指定一个独一无二的身份证号码的

#3、所以要想实现通过a标签跳转到指定的位置，分为两步
3.1、给目标位置的标签添加一个id属性，然后指定一个独一无二的值
3.2、告诉a标签你需要跳转到的目标标签对应的独一无二的身份证号码是多少

#4、a标签除了可以跳转当前页面，还可以跳转到其他页面的指定位置
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <a href="#">新闻页</a>
        <a href="#">hao123</a>
        <a href="#">地图</a>
        <a href="javascript:">学术</a>
        <a href="#egon">美丽的EGON到底在哪里</a>
        <p>我是段落</p>
        <p id="egon">我是英俊潇洒的EGON老师</p>
        <p>我是段落</p>
    </body>
</html>

跳到首页
#1、跳到首页
<a href="">刷新页面，回到顶部，人类感觉不出来区别</a> 
<a href="#">回到顶部</a>

#2、注意点：
    通过我们的a标签跳转到指定的位置，是没有过度动画的
    是直接一下子就跳转到了指定位置,比如京东主页
    如果跳到首页需要过渡动画，则不用a标签做，比如天猫主页


\HTML div  span
# div标签和span标签
div  # 标签用来定义一个块级元素，并无实际的意义。主要通过CSS样式为其赋予不同的表现。
span # 标签用来定义内联(行内)元素，并无实际的意义。主要通过CSS样式为其赋予不同的表现。

块级元素与行内元素的区别：
所谓块元素，是以另起一行开始渲染的元素，行内元素则不需另起一行。如果单独在网页中插入这两个元素，不会对页面产生任何的影响。
这两个元素是专门为定义CSS样式而生的。

注意：
关于标签嵌套：通常块级元素可以包含内联元素或某些块级元素，但内联元素不能包含块级元素，它只能包含其它内联元素。
p标签不能包含块级标签，p标签也不能包含p标签。

比喻：div和span没有自己的什么特点，就像一张白纸。可以往上面画任何东西，比较干净。


\HTML 列表     https://www.w3school.com.cn/html/html_lists.asp
语义：标记一堆数据是一个整体/列表
html中列表标签分为三种
# ul通常应该只嵌套li标签
# 而li标签却可以嵌套任意其他标签

\小技巧：在pycharm中输入 ul>li*5  按下tab键就会快速生成表结构。

1、无序列表（列表标签中使用最多的一种，非常重要）：unordered list
#1、作用：制作导航条、商品列表、新闻列表等
#2、组合使用ul>li
    <ul>
        <li>秒杀</li>
        <li>优惠券</li>
        <li>PLUS会员</li>
        <li>闪购</li>
        <li>拍卖</li>
        <li>京东服饰</li>
        <li>京东超市</li>
        <li>生鲜</li>
        <li>全球购</li>
        <li>京东金融</li>
    </ul>

#3、ul标签的属性type（这属于列表的样式，所以了解即可）
type：列表标识的类型
        disc：实心圆(默认值)
        circle：空心圆
        square：实心矩形
        none：不显示标识

可以通过css直接去掉小圆点
<style type="text/css">
            ul {
                list-style: none;
            }
</style>

#4、注意
ul与li是组合标签应该一起出现，并且ul的子标签只应该是li，而li的子标签则可以是任意其他标签

# 无序列表练习
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>物品清单</h1>
    <ul>
        <li>
            <h2>蔬菜</h2>
            <ul>
                <li>西红柿</li>
                <li>花瓜</li>
                <li>芹菜</li>
            </ul>
        </li>
        <li>
            <h2>水果</h2>
            <ul>
                <li>香蕉</li>
                <li>菠萝</li>
                <li>火龙果</li>
            </ul>
        </li>
    </ul>
</body>
</html>



2、有序列表（极少使用），前面带序号
<h1>智商排名</h1>
    <ol>
        <li>Egon</li>
        <li>刘清正</li>
        <li>武佩奇</li>
        <li>alex</li>
        <li>元昊</li>
    </ol>

    <!--有序列表能干的事，完全可以用无序列表取代-->
    <h1>智商排名</h1>
    <ul style="list-style: none">
        <li>1. Egon</li>
        <li>2. 刘清正</li>
        <li>3. 武佩奇</li>
        <li>4. alex</li>
        <li>5. 元昊</li>
    </ul>



3、自定义列表（也会经常使用）
#1、作用分析
选择用什么标签的唯一标准，是看文本的实际语义，而不是看长什么样子
无序列表：内容是并列的,没有先后顺序
有序列表：内容是有先后顺序的
自定义列表：对一个题目进行解释说明的时候，用自定义列表,可以做网站尾部相关信息，网易注册界面的输入框

#2、自定义列表也是一个组合标签：dl>dt+dd
dl: defination list，自定义列表
dt：defination title，自定义标题
dd：defination description，自定义描述
<dl>
    <dt>自定义标题1<dt>
    <dd>描述1<dd>
    <dd>描述2<dd>
    <dd>描述3<dd>

    <dt>自定义标题2<dt>
    <dd>描述1<dd>
    <dd>描述2<dd>
    <dd>描述3<dd>

    <dt>自定义标题3<dt>
    <dd>描述1<dd>
    <dd>描述2<dd>
    <dd>描述3<dd>
</dl>
 #3、注意: 3.1 dl>dt+dd应该组合出现，dl中只应该存放dt和dd，而可以在dt和dd中添加任意其他标签 
 #        3.2 一个dt可以可以没有对应的dd，也可以有多个，但建议一个dt对应一个dd


\table 标签 表格  https://www.w3school.com.cn/html/html_tables.asp
# 语义：标记一段数据为表格
表格是一个二维数据空间，一个表格由若干行组成，一个行又有若干单元格组成，单元格里可以包含文字、列表、图案、表单、数字符号、预置文本和其它的表格等内容。
表格最重要的目的是显示表格类数据。表格类数据是指最适合组织为表格格式（即按行和列组织）的数据。
表格的基本结构：
  表格由 <table> 标签来定义。每个表格均有若干行（由 <tr> 标签定义），每行被分割为若干单元格（由 <td> 标签定义）。字母 td 指表格数据（table data），即数据单元格的内容。
  数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。
<table border="1" cellpadding="10" cellspacing="10">
  <thead>
    <tr>
      <th>序号</th>
      <th>姓名</th>
      <th>爱好</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">1</td>
      <td>Egon</td>
      <td rowspan="2">杠娘 </td>
    </tr>
    <tr>
      <td>2</td>
      <td>Yuan</td>
      <td>日天</td>
    </tr>
  </tbody>
</table>

属性:
    border:  # 表格边框.
    cellpadding: # 内边距
    cellspacing: # 外边距.
    width:   # 像素 百分比.（最好通过css来设置长宽）
    rowspan: # 单元格竖跨多少行
    colspan: # 单元格横跨多少列（即合并单元格）

\表格属性
#1、宽度和高度
    可以给table和td设置width和height属性
    
    1.1 默认情况下表格的宽高是按照内容的尺寸来调整的，也可以通过给table标签设置widht和height来手动指定表格的宽高

    1.2 如果给td标签设置width和height属性，会修改当前单元格的宽度和高度，只要不超过table的宽高，则不会影响整个表格的宽度和高度


#2、水平对齐和垂直对齐
    水平对齐align可以给table、tr、td标签设置
    垂直对齐valign只能给tr、td标签设置

    ========水平对齐===========
    取值
    align=“left”
    align=“center”
    align=“right”

    2.1 给table标签设置水平对齐，可以让表格在水平方向上对齐
          强调：table只能设置水平方向

    2.2 给tr设置水平对齐，可以控制当前行所有单元格内容都水平对齐

    2.3 给td设置水平对齐，可以控制当前单元格内容水平对齐，tr与td冲突的情况下，以td为准

    ========垂直对齐===========
    取值
    valign=“top”
    valign=“center”
    valign=“bottom”
    
    2.4 给tr设置垂直对齐可以让当前行所有单元格内容都垂直对齐
    2.5 给td设置垂直对齐可以让当前单元格内容垂直对齐

#3、外边距和内边距
    只能给table设置

    3.1 外边距：单元格与单元格之间的间隔，cellspacing="3px"，默认值为2px
    3.2 内边距：单元格边框与文字之间的距离:cellpadding="200px"


\三种方式细线表格
#1、方式一
    在标签中，想通过指定外边距为0来实现细线表格是不靠谱的，其实他是将2条线合成了一条线.所以看上去很不舒服,如下实现
<table width="200px" height="200px" bgcolor="black" border="1" cellspacing="0px">
    <tr bgcolor="white">
        <td>姓名</td>
        <td>性别</td>
        <td>年龄</td>
    </tr>

    <tr bgcolor="white" >
        <td>Egon</td>
        <td>male</td>
        <td>18</td>
    </tr>

    <tr bgcolor="white">
        <td>ALex</td>
        <td>male</td>
        <td>73</td>
    </tr>

    <tr bgcolor="white">
        <td>Wxx</td>
        <td>female</td>
        <td>84</td>
    </tr>
</table>
#2、方式二
 细线表格的制作方式：
        1、给table标签设置bgcolor
        2、给tr标签设置bgcolor
        3、给table标签设置cellspacing="1px"

      注意：
      table、tr、td标签都支持bgcolor属性

<table width="200px" height="200px" bgcolor="black" cellspacing="1px">
    <tr bgcolor="white">
        <td>姓名</td>
        <td>性别</td>
        <td>年龄</td>
    </tr>

    <tr bgcolor="white" >
        <td>Egon</td>
        <td>male</td>
        <td>18</td>
    </tr>

    <tr bgcolor="white">
        <td>ALex</td>
        <td>male</td>
        <td>73</td>
    </tr>

    <tr bgcolor="white">
        <td>Wxx</td>
        <td>female</td>
        <td>84</td>
    </tr>
</table>

#3、方式三（style="border-collapse: collapse;border: 1px solid red"）
<table border="1px" style="border-collapse: collapse;border: 1px solid red">
    <tr>
        <td>姓名</td>
        <td>性别</td>
        <td>年龄</td>
    </tr>
    <tr>
        <td>egon</td>
        <td>male</td>
        <td>18</td>
    </tr>
    <tr>
        <td>alex</td>
        <td>female</td>
        <td>19</td>
    </tr>
</table>


\表格结构详解
为了方便管理维护以及提升语义，我们将表格中存储的数据分为四类：
#1、表格的标题:caption
    特点:相对于表格宽度自动居中对齐
    注意:
        1.1 该标签一定要写在table标签里，否则无效
        1.2 caption一定要紧跟在table标签内的第一个

#2、表格的表头信息:thead
    特点：专门用来存储每一列的标题，只要将当前列的标题存储在这个标签中就会自动居中+加粗文字

#3、表格的主体信息:tbody
    注意：
        3.1 如果没有添加tbody，浏览器会自动添加
        3.2 如果指定了thread和tfoot，那么在修改整个表格的高度时，thead和tfoot有自己默认的高度，不会随着
            表格的高度变化而变化

#4、表尾信息:tfoot


<html>
<head>
    <meta charset="utf-8"/>
</head>
<body>
    <table bgcolor="black" border="1" width="300px" height="300px" cellspacing="1px">

        <caption>学员信息统计</caption>
        <thead>
            <tr bgcolor="white">
                <th>姓名</th>
                <th>性别</th>
                <th>年龄</th>
            </tr>
        </thead>

        <tbody>
            <tr bgcolor="white">
                <td>egon</td>
                <td>male</td>
                <td>18</td>
            </tr>

            <tr bgcolor="white">
                <td>egon</td>
                <td>male</td>
                <td>18</td>
            </tr>

            <tr bgcolor="white">
                <td>egon</td>
                <td>male</td>
                <td>18</td>
            </tr>
        </tbody>

        <tfoot>
            <tr bgcolor="white">
                <td>3</td>
                <td>3</td>
                <td>3</td>
            </tr>
        </tfoot>
    </table>

</body>
</html>

  
\单元格合并
#1、水平向上的单元格colspan
    可以给td标签添加一个colspan属性，来把水平方向的单元格当做多个单元格来看待
    <td colspan="2"></td>

#2、垂直向上的单元格rowspan
    可以给td标签设置一个rowspan属性，来把垂直方向的的单元格当成多个去看待

#注意注意注意:
1、由于把某一个单元格当作了多个单元格来看待，所以就会多出一些单元格，所以需要删掉一些单元格
2、一定要记住，单元格合并永远是向后或者向下合并，而不能向前或向上合并

\传统布局
传统的布局方式就是使用table来做整体页面的布局，布局的技巧归纳为如下几点：
#1、定义表格宽高，将border、cellpadding、cellspacing全部设置为0
#2、单元格里面嵌套表格
#3、单元格中的元素和嵌套的表格用align和valign设置对齐方式
#4、通过属性或者css样式设置单元格中元素的样式

传统布局目前应用：
#1、快速制作用于演示的html页面
#2、商业推广EDM制作(广告邮件)

<!DOCTYPE HTML>
<html>
    <head lang='en'>
        <meta charset="utf-8">
        <title>Egon无敌</title>
        <base target="_blank">
    </head>
    <body>

    <table border="0" cellspacing="1" bgcolor="blue"  width="500px" height="200px">
        <caption>课程表</caption>
        <tr bgcolor="white" align="center">
            <td>项目</td>
            <td colspan="6">上课</td>
            <td align="center">休息</td>
        </tr>
        <tr bgcolor="white" align="center">
            <td>星期</td>
            <td>星期一</td>
            <td>星期二</td>
            <td>星期三</td>
            <td>星期四</td>
            <td>星期五</td>
            <td>星期六</td>
            <td>星期日</td>
        </tr>
        <tr bgcolor="white" align="center">
            <td rowspan="4">上午</td>
            <td>语文</td>
            <td>数学</td>
            <td>英语</td>
            <td>英语</td>
            <td>物理</td>
            <td>计算机</td>
            <td rowspan="4">休息</td>
        </tr>
        <tr bgcolor="white" align="center">
            <td>数学</td>
            <td>数学</td>
            <td>地理</td>
            <td>历史</td>
            <td>化学</td>
            <td>计算机</td>
        </tr>
        <tr bgcolor="white" align="center">
            <td>化学</td>
            <td>语文</td>
            <td>体育</td>
            <td>计算机</td>
            <td>英语</td>
            <td>计算机</td>
        </tr>
        <tr bgcolor="white" align="center">
            <td>语文</td>
            <td>数学</td>
            <td>英语</td>
            <td>英语</td>
            <td>物理</td>
            <td>计算机</td>
        </tr>
        <tr bgcolor="white" align="center">
            <td rowspan="2">下午</td>
            <td>数学</td>
            <td>数学</td>
            <td>地理</td>
            <td>历史</td>
            <td>化学</td>
            <td>计算机</td>
            <td rowspan="2">休息</td>
        </tr>
        <tr bgcolor="white" align="center">
            <td>数学</td>
            <td>数学</td>
            <td>地理</td>
            <td>历史</td>
            <td>化学</td>
            <td>计算机</td>
        </tr>
    </table>
    
    </body>
</html>
    




\form 标签 表单
# 思维导图：https://www.processon.com/view/link/5aeea789e4b084d6e4bf6911#map
# 语义：标记表单
# form ：前后端有数据交互的时候用form表单
#1、什么是表单？
    表单就是专门用来接收用户输入或采集用户信息的，最后将输入的数据交给action去提交
    表单元素指的是不同类型的 input 元素、复选框、单选按钮、提交按钮等等。

#2、表单的格式
    <form>
        <表单元素>
    </form>

form表单提交数据的几个注意事项:
    1. 所有获取用户输入的标签都必须放在form表单里面
    2. action控制着往哪儿提交
    3. input\select\textarea 都需要有name属性
    4. 提交按钮 <input type="submit">
功能：
    表单用于向服务器传输数据，从而实现用户与Web服务器的交互
    表单能够包含input系列标签，比如文本字段、复选框、单选框、提交按钮等等。
    表单还可以包含textarea、select、fieldset和 label标签。

# Form 属性
HTML <form> 元素，已设置所有可能的属性，是这样的：
实例
<form action="action_page.php" method="GET" target="_blank" accept-charset="UTF-8"
ectype="application/x-www-form-urlencoded" autocomplete="off" novalidate>
.
form elements
.
</form> 

# 1、下面是 <form> 属性的列表：
属性	                      描述
accept-charset # 规定在被提交表单中使用的字符集（默认：页面字符集）。
action	       # 规定向何处提交表单的地址（URL）（提交页面）。
autocomplete   # 规定浏览器应该自动完成表单（默认：开启）。
enctype	       # 规定被提交数据的编码（默认：url-encoded）。
method	       # 规定在提交表单时所用的 HTTP 方法（默认：GET）。
name	       # 规定识别表单的名称（对于 DOM 使用：document.forms.name）。
novalidate	   # 规定浏览器不验证表单。
target	       # 规定 action 属性中地址的目标（默认：_self）。

# action 属性
action 属性定义在提交表单时执行的动作。向服务器提交表单的通常做法是使用提交按钮。
通常，表单会被提交到 web 服务器上的网页。在上面的例子中，指定了某个服务器脚本来处理被提交表单：
<form action="action_page.php">
如果省略 action 属性，则 action 会被设置为当前页面。

# method 属性
method 属性规定在提交表单时所用的 HTTP 方法（GET 或 POST）：
<form action="action_page.php" method="GET">
或：
<form action="action_page.php" method="POST">
    # 何时使用 GET？
    您能够使用 GET（默认方法）：如果表单提交是被动的（比如搜索引擎查询），并且没有敏感信息。

    当您使用 GET 时，表单数据在页面地址栏中是可见的：
    action_page.php?firstname=Mickey&lastname=Mouse
    注释：GET 最适合少量数据的提交。浏览器会设定容量限制。

    # 何时使用 POST？
    您应该使用 POST：如果表单正在更新数据，或者包含敏感信息（例如密码）。
    POST 的安全性更加，因为在页面地址栏中被提交的数据是不可见的。

# enctype 属性



# 2、表单元素
基本概念：
    HTML表单是HTML元素中较为复杂的部分，表单往往和脚本、动态页面、数据处理等功能相结合，因此它是制作动态网站很重要的内容。
    表单一般用来收集用户的输入信息
表单工作原理：
    访问者在浏览有表单的网页时，可填写必需的信息，然后按某个按钮提交。这些信息通过Internet传送到服务器上。
    服务器上专门的程序对这些数据进行处理，如果有错误会返回错误信息，并要求纠正错误。当数据完整无误后，服务器反馈一个输入完成的信息。

# <input> 元素
<input> 元素是最重要的表单元素。
<input> 元素有很多形态，根据不同的 type 属性。


# label 元素  定义：<label> 标签为 input 元素定义标注（标记）。
说明：
    label 元素不会向用户呈现任何特殊效果。
    <label> 标签的 for 属性值应当与相关元素的 id 属性值相同。

当点到"用户名“字样上时也就选中了，无须点到圈里
<form action="">
  <input type="text"  name="username" id="username"><label for="username">用户名</label>
</form>


# select 元素  下拉列表
<option> 元素定义待选择的选项。
列表通常会把首个选项显示为被选选项。
您能够通过添加 selected 属性来定义预定义选项。

实例
<form action="" method="post">
    <select name="city" id="" style="width: 200px">
        <optgroup label="一线城市">
            <option value="BJ">北京</option>
            <option value="SH">上海</option>
            <option value="SZ" selected="selected">深圳</option>
            <option value="GZ">广州</option>
        </optgroup>
        <optgroup label="二线城市">
            <option value="BJ">济南</option>
            <option value="SH">苏州</option>
            <option value="SZ" selected="selected">南京</option>
            <option value="GZ">成都</option>
        </optgroup>

    </select>
</form>

属性说明：
    multiple：# 布尔属性，设置后为多选，否则默认单选
    disabled：# 禁用
    selected：# 默认选中该项
    value：   # 定义提交时的选项值
    size：    # 同一时间显示几条
    optgroup:#  分组


# textarea 元素 定义多行文本输入字段（文本域）
<textarea name="memo" id="memo" cols="30" rows="10">
  默认内容
  ....
</textarea>

属性说明：
    name：# 名称
    rows：# 行数
    cols：# 列数
    disabled：# 禁用


# <option> 元素 定义待选择的选项。
列表通常会把首个选项显示为被选选项。您能够通过添加 selected 属性来定义预定义选项。
实例
<option value="fiat" selected>Fiat</option>


# <button> 元素 定义可点击的按钮
实例
<button type="button" onclick="alert('Hello World!')">Click Me!</button>


# <datalist> 元素 为 <input> 元素规定预定义选项列表
用户会在他们输入数据时看到预定义选项的下拉列表。
<input> 元素的 list 属性必须引用 <datalist> 元素的 id 属性。

实例
通过 <datalist> 设置预定义值的 <input> 元素：
<form action="action_page.php">
<input list="browsers">
<datalist id="browsers">
   <option value="Internet Explorer">
   <option value="Firefox">
   <option value="Chrome">
   <option value="Opera">
   <option value="Safari">
</datalist> 
</form>

# <fieldset> 元素 组合表单数据，给表单加个框
<fieldset> 元素组合表单中的相关数据
<legend> 元素为 <fieldset> 元素定义标题。

实例
<form action="action_page.php">
    <fieldset>
        <legend>Personal information:</legend>
        First name:<br>
        <input type="text" name="firstname" value="Mickey">
        <br>
        Last name:<br>
        <input type="text" name="lastname" value="Mouse">
        <br><br>
        <input type="submit" value="Submit">
    </fieldset>
</form> 


# 练习
<html>
    <head>
        <title>表单练习</title>
        <meta charset="utf-8"/>
    </head>
    <body>
        <form action="http://www.baidu.com">
            <fieldset>
                <legend>注册页面</legend>
                <p>
                    账号：<input type="text" placeholder="请输入你的用户名" name="user">
                </p>

                <p>
                    密码：<input type="password" placeholder="请输入你的密码" name="password">
                </p>

                <p>
                    性别：
                    <input type="radio" name="gender" value="male">男
                    <input type="radio" name="gender" value="female">女
                    <input type="radio" name="gender" checked="checked" value="none">保密
                </p>

                <p>
                    <!--注意点：单选框or复选框都需要指定相同的name值-->
                    爱好：
                    <input type="checkbox" name="sport" value="basketball">篮球
                    <input type="checkbox" name="sport" value="football">足球
                    <input type="checkbox" checked="checked" name="sport" value="crazy">足浴
                </p>

                <p>
                    简介：
                    <textarea name="" id="" cols="30" rows="10" name="desc"></textarea>
                </p>

                <p>
                    生日：
                    <input type="date" name="birth">
                </p>

                <p>
                    邮箱：
                    <input type="email" name="email">
                </p>

                <p>
                    电话：
                    <input type="number" name="phone">
                </p>

                <p>
                    <input type="submit" value="注册">&nbsp;&nbsp;&nbsp;&nbsp;
                    <input type="reset" value="清空">
                </p>

            </fieldset>
        </form>

    </body>
</html>

# Django接收上传文件代码
from django.conf.urls import url
from django.shortcuts import HttpResponse


def upload(request):
    print("request.GET:", request.GET)
    print("request.POST:", request.POST)

    if request.FILES:
        filename = request.FILES["file"].name
        with open(filename, 'wb') as f:
            for chunk in request.FILES['file'].chunks():
                f.write(chunk)
            return HttpResponse('上传成功')
    return HttpResponse("收到了！")

urlpatterns = [
    url(r'^upload/', upload),
]



\form 中  input 标签（类型+属性）
<input> 元素会根据不同的 type 属性，变化为多种形态。

#type属性值	    表现形式	    对应代码
text	       单行输入文本	 <input type=text" />
password	   密码输入框	 <input type="password"  />
date	       日期输入框	 <input type="date" />
checkbox	   复选框	    <input type="checkbox" checked="checked"  />
radio	       单选框	    <input type="radio"  />
submit	       提交按钮	    <input type="submit" value="提交" />
reset	       重置按钮	    <input type="reset" value="重置"  />
button	       普通按钮	    <input type="button" value="普通按钮"  />
hidden	       隐藏输入框	 <input type="hidden"  />
file	       文本选择框	 <input type="file"  />

# 属性说明:
    name： # 表单提交时的“键”，注意和id的区别
    value：# 表单提交时对应项的值
        type="button", "reset", "submit"时，# 为按钮上显示的文本年内容
        type="text","password","hidden"时， # 为输入框的初始值
        type="checkbox", "radio", "file"时，# 为输入相关联的值
    checked： # radio和checkbox默认被选中的项
    readonly：# text和password设置只读
    disabled：# 所有input均适用

\Input 标签的类型
# 输入类型：https://www.w3school.com.cn/html/html_form_input_types.asp
    
    # 文本输入 https://www.w3school.com.cn/tiy/t.asp?f=html_input_text
    <input type="text"> 定义用于文本输入的单行输入字段：

    # 定义按钮 https://www.w3school.com.cn/tiy/t.asp?f=html_input_button
    <input type="button> 定义按钮。
    实例
    <body>
        <button type="button" onclick="alert('Hello World!')">Click Me!</button>
    </body>


    # 单选按钮输入（选择多个选择之一） https://www.w3school.com.cn/tiy/t.asp?f=html_input_radio
    <input type="radio"> 定义单选按钮。
    单选按钮允许用户在有限数量的选项中选择其中之一：name属性值同名就会产生互斥的效果、checked 设置默认被选中项
    <form action="/demo/demo_form.asp">
        <input type="radio" name="sex" value="male" checked="checked">Male
        <br>
        <input type="radio" name="sex" value="female">Female
        <br><br>
        <input type="submit">
    </form> 

    # 定义复选框checkbox https://www.w3school.com.cn/tiy/t.asp?f=html_input_checkbox
    <input type="checkbox"> 定义复选框。
    复选框允许用户在有限数量的选项中选择零个或多个选项。
    实例
    <form action="/demo/demo_form.asp">
            <input type="checkbox" name="hobbies" value="basketball">篮球
            <input type="checkbox" name="hobbies" value="football" checked>足球
            <input type="checkbox" name="hobbies" value="pingpang" checked>乒乓球
            <br><br>
            <input type="submit">
    </form> 


    # 提交按钮（提交表单） https://www.w3school.com.cn/tiy/t.asp?f=html_input_submit
    <input type="submit"> 定义用于向表单处理程序（form-handler）提交表单的按钮。
    表单处理程序通常是包含用来处理输入数据的脚本的服务器页面。
    表单处理程序在表单的 action 属性中指定：

    # name 属性
    如果要正确地被提交，每个输入字段必须设置一个 name 属性。
    本例只会提交 "Last name" 输入字段：

    实例
    <form action="action_page.php">
        First name:<br>
        <input type="text" value="Mickey"><br>
        Last name:<br>
        <input type="text" name="lastname" value="Mouse">
        <br><br>
        <input type="submit" value="Submit">
    </form> 
    
    # 输入类型：reset 重置 将填写好的表单清空
        <input type="reset" value="重置" >

    # 输入类型：file 上传文件
        <input type="file" name="uploadfile">

    # 输入类型：number
    <input type="number"> 用于应该包含数字值的输入字段。
    您能够对数字做出限制。根据浏览器支持，限制可应用到输入字段。

    实例
    <form>
        Quantity (between 1 and 5):
        <input type="number" name="quantity" min="1" max="5">
    </form>

    # 输入类型：date
    <input type="date"> 用于应该包含日期的输入字段。
    根据浏览器支持，日期选择器会出现输入字段中。

    实例
    <form>
        Birthday:
        <input type="date" name="bday">
    </form>

    您可以向输入添加限制：
    实例
    <form>
        Enter a date before 1980-01-01:
        <input type="date" name="bday" max="1979-12-31"><br>
        Enter a date after 2000-01-01:
        <input type="date" name="bday" min="2000-01-02"><br>
    </form>

    # 输入类型：color
    <input type="color"> 用于应该包含颜色的输入字段。
    根据浏览器支持，颜色选择器会出现输入字段中。

    实例
    <form>
        Select your favorite color:
        <input type="color" name="favcolor">
    </form>

    # 输入类型：range
    <input type="range"> 用于应该包含一定范围内的值的输入字段。
    根据浏览器支持，输入字段能够显示为滑块控件。

    实例
    <form>
        <input type="range" name="points" min="0" max="10">
    </form>
    您能够使用如下属性来规定限制：min、max、step、value。

    # 输入类型：month
    <input type="month"> 允许用户选择月份和年份。

    根据浏览器支持，日期选择器会出现输入字段中。

    实例
    <form>
    Birthday (month and year):
        <input type="month" name="bdaymonth">
    </form>

    # 输入类型：week
    <input type="week"> 允许用户选择周和年。

    根据浏览器支持，日期选择器会出现输入字段中。

    实例
    <form>
        Select a week:
        <input type="week" name="week_year">
    </form>

    # 输入类型：time
    <input type="time"> 允许用户选择时间（无时区）。
    根据浏览器支持，时间选择器会出现输入字段中。

    实例
    <form>
        Select a time:
        <input type="time" name="usr_time">
    </form>

    # 输入类型：datetime
    <input type="datetime"> 允许用户选择日期和时间（有时区）。
    根据浏览器支持，日期选择器会出现输入字段中。

    实例
    <form>
        Birthday (date and time):
        <input type="datetime" name="bdaytime">
    </form>

    # 输入类型：datetime-local
    <input type="datetime-local"> 允许用户选择日期和时间（无时区）。
    根据浏览器支持，日期选择器会出现输入字段中。

    实例
    <form>
        Birthday (date and time):
        <input type="datetime-local" name="bdaytime">
    </form>

    # 输入类型：email
    <input type="email"> 用于应该包含电子邮件地址的输入字段。
    根据浏览器支持，能够在被提交时自动对电子邮件地址进行验证。
    某些智能手机会识别 email 类型，并在键盘增加 ".com" 以匹配电子邮件输入。

    实例
    <form>
        E-mail:
        <input type="email" name="email">
    </form>

    # 输入类型：search
    <input type="search"> 用于搜索字段（搜索字段的表现类似常规文本字段）。

    实例
    <form>
        Search Google:
        <input type="search" name="googlesearch">
    </form>


    # 输入类型：tel
    <input type="tel"> 用于应该包含电话号码的输入字段。
    目前只有 Safari 8 支持 tel 类型。

    实例
    <form>
        Telephone:
        <input type="tel" name="usrtel">
    </form>


    # 输入类型：url
    <input type="url"> 用于应该包含 URL 地址的输入字段。
    根据浏览器支持，在提交时能够自动验证 url 字段。
    某些智能手机识别 url 类型，并向键盘添加 ".com" 以匹配 url 输入。

    实例
    <form>
        Add your homepage:
        <input type="url" name="homepage">
    </form>

    # 输入限制
    这里列出了一些常用的输入限制（其中一些是 HTML5 中新增的）：
    属性	        描述
    disabled	规定输入字段应该被禁用。
    max	        规定输入字段的最大值。
    maxlength	规定输入字段的最大字符数。
    min	        规定输入字段的最小值。
    pattern	    规定通过其检查输入值的正则表达式。
    readonly	规定输入字段为只读（无法修改）。
    required	规定输入字段是必需的（必需填写）。
    size	    规定输入字段的宽度（以字符计）。
    step	    规定输入字段的合法数字间隔。
    value	    规定输入字段的默认值。
    您将在下一章学到更多有关输入限制的知识。

\Input 标签的属性
# 输入属性：https://www.w3school.com.cn/html/html_form_attributes.asp
# 属性是给上面类型使用的

    # value 属性
    value 属性规定输入字段的初始值：

    实例
    <form action="">
    First name:<br>
    <input type="text" name="firstname" value="John">
    <br>
    Last name:<br>
    <input type="text" name="lastname">
    </form> 

    # readonly 属性
    readonly 属性规定输入字段为只读（不能修改）：

    实例
    <form action="">
    First name:<br>
    <input type="text" name="firstname" value="John" readonly>
    <br>
    Last name:<br>
    <input type="text" name="lastname">
    </form> 
    # readonly 属性不需要值。它等同于 readonly="readonly"。

    # disabled 属性
    disabled 属性规定输入字段是禁用的。
    被禁用的元素是不可用和不可点击的。
    被禁用的元素不会被提交。

    实例
    <form action="">
    First name:<br>
    <input type="text" name="firstname" value="John" disabled>
    <br>
    Last name:<br>
    <input type="text" name="lastname">
    </form> 
    # disabled 属性不需要值。它等同于 disabled="disabled"。

    # size 属性
    size 属性规定输入框字段的尺寸（以字符计）：

    实例
    <form action="">
    First name:<br>
    <input type="text" name="firstname" value="John" size="40">
    <br>
    Last name:<br>
    <input type="text" name="lastname">
    </form> 

    # maxlength 属性
    maxlength 属性规定输入字段允许的最大长度：

    实例
    <form action="">
    First name:<br>
    <input type="text" name="firstname" maxlength="10">
    <br>
    Last name:<br>
    <input type="text" name="lastname">
    </form> 
    如设置 maxlength 属性，则输入控件不会接受超过所允许数的字符。
    该属性不会提供任何反馈。如果需要提醒用户，则必须编写 JavaScript 代码。
    注释：输入限制并非万无一失。JavaScript 提供了很多方法来增加非法输入。如需安全地限制输入，则接受者（服务器）必须同时对限制进行检查。

    # autocomplete 属性
    autocomplete 属性规定表单或输入字段是否应该自动完成。当自动完成开启，浏览器会基于用户之前的输入值自动填写值。
    提示：您可以把表单的 autocomplete 设置为 on，同时把特定的输入字段设置为 off，反之亦然。
    autocomplete 属性适用于 <form> 以及如下 <input> 类型：text、search、url、tel、email、password、datepickers、range 以及 color。

    实例
    自动完成开启的 HTML 表单（某个输入字段为 off）：

    <form action="action_page.php" autocomplete="on">
    First name:<input type="text" name="fname"><br>
    Last name: <input type="text" name="lname"><br>
    E-mail: <input type="email" name="email" autocomplete="off"><br>
    <input type="submit">
    </form> 

    # novalidate 属性
    novalidate 属性属于 <form> 属性。
    如果设置，则 novalidate 规定在提交表单时不对表单数据进行验证。

    实例
    指示表单在被提交时不进行验证：
    <form action="action_page.php" novalidate>
        E-mail: <input type="email" name="user_email">
        <input type="submit">
    </form> 

    # autofocus 属性
    autofocus 属性是布尔属性。
    如果设置，则规定当页面加载时 <input> 元素应该自动获得焦点。

    实例
    使 "First name" 输入字段在页面加载时自动获得焦点：
    First name:<input type="text" name="fname" autofocus>

    # formaction 属性
    formaction 属性规定当提交表单时处理该输入控件的文件的 URL。
    formaction 属性覆盖 <form> 元素的 action 属性。
    formaction 属性适用于 type="submit" 以及 type="image"。

    实例
    拥有两个两个提交按钮并对于不同动作的 HTML 表单：
    <!DOCTYPE HTML>
    <html>
        <body>
        <form action="/example/html5/demo_form.asp" method="get">
            First name: <input type="text" name="fname" /><br />
            Last name: <input type="text" name="lname" /><br />
            <input type="submit" value="提交" /><br />
            <input type="submit" formaction="/example/html5/demo_admin.asp" value="以管理员身份提交" />
        </form>
        </body>
    </html>

    # formenctype 属性
    formenctype 属性规定当把表单数据（form-data）提交至服务器时如何对其进行编码（仅针对 method="post" 的表单）。
    formenctype 属性覆盖 <form> 元素的 enctype 属性。
    formenctype 属性适用于 type="submit" 以及 type="image"。

    实例
    发送默认编码以及编码为 "multipart/form-data"（第二个提交按钮）的表单数据（form-data）：
    <!DOCTYPE HTML>
    <html>
        <body>

        <form action="/example/html5/demo_post_enctype.asp" method="post">
        First name: <input type="text" name="fname" /><br />
        <input type="submit" value="提交" />
        <input type="submit" formenctype="multipart/form-data" value="以 Multipart/form-data 编码提交" />
        </form>

        </body>
    </html>

    # formmethod 属性 https://www.w3school.com.cn/tiy/t.asp?f=html5_input_formmethod
    formmethod 属性定义用以向 action URL 发送表单数据（form-data）的 HTTP 方法。
    formmethod 属性覆盖 <form> 元素的 method 属性。
    formmethod 属性适用于 type="submit" 以及 type="image"。

    实例
    第二个提交按钮覆盖表单的 HTTP 方法：
    <form action="action_page.php" method="get">
        First name: <input type="text" name="fname"><br>
        Last name: <input type="text" name="lname"><br>
        <input type="submit" value="Submit">
        <input type="submit" formmethod="post" formaction="demo_post.asp"
        value="Submit using POST">
    </form> 

    # formnovalidate 属性 https://www.w3school.com.cn/tiy/t.asp?f=html5_input_formnovalidate
    novalidate 属性是布尔属性。
    如果设置，则规定在提交表单时不对 <input> 元素进行验证。
    formnovalidate 属性覆盖 <form> 元素的 novalidate 属性。
    formnovalidate 属性可用于 type="submit"。

    实例
    拥有两个提交按钮的表单（验证和不验证）：
    <form action="action_page.php">
    E-mail: <input type="email" name="userid"><br>
    <input type="submit" value="Submit"><br>
    <input type="submit" formnovalidate value="Submit without validation">
    </form> 

    # formtarget 属性  https://www.w3school.com.cn/tiy/t.asp?f=html5_input_formtarget
    formtarget 属性规定的名称或关键词指示提交表单后在何处显示接收到的响应。
    formtarget 属性会覆盖 <form> 元素的 target 属性。
    formtarget 属性可与 type="submit" 和 type="image" 使用。

    实例
    这个表单有两个提交按钮，对应不同的目标窗口：

    <form action="action_page.php">
    First name: <input type="text" name="fname"><br>
    Last name: <input type="text" name="lname"><br>
    <input type="submit" value="Submit as normal">
    <input type="submit" formtarget="_blank"
    value="Submit to a new window">
    </form> 

    # height 和 width 属性  https://www.w3school.com.cn/tiy/t.asp?f=html5_input_height_width
    height 和 width 属性规定 <input> 元素的高度和宽度。
    height 和 width 属性仅用于 <input type="image">。
    注释：请始终规定图像的尺寸。如果浏览器不清楚图像尺寸，则页面会在图像加载时闪烁。

    实例
    把图像定义为提交按钮，并设置 height 和 width 属性：
    <input type="image" src="img_submit.gif" alt="Submit" width="48" height="48">


    # list 属性  https://www.w3school.com.cn/tiy/t.asp?f=html5_datalist
    list 属性引用的 <datalist> 元素中包含了 <input> 元素的预定义选项。

    实例
    使用 <datalist> 设置预定义值的 <input> 元素：

    <input list="browsers">

    <datalist id="browsers">
    <option value="Internet Explorer">
    <option value="Firefox">
    <option value="Chrome">
    <option value="Opera">
    <option value="Safari">
    </datalist> 

    # min 和 max 属性 https://www.w3school.com.cn/tiy/t.asp?f=html5_input_max_min
    min 和 max 属性规定 <input> 元素的最小值和最大值。
    min 和 max 属性适用于如需输入类型：number、range、date、datetime、datetime-local、month、time 以及 week。

    实例
    具有最小和最大值的 <input> 元素：
    Enter a date before 1980-01-01:
    <input type="date" name="bday" max="1979-12-31">

    Enter a date after 2000-01-01:
    <input type="date" name="bday" min="2000-01-02">

    Quantity (between 1 and 5):
    <input type="number" name="quantity" min="1" max="5">


    # multiple 属性 https://www.w3school.com.cn/tiy/t.asp?f=html5_input_multiple
    multiple 属性是布尔属性。
    如果设置，则规定允许用户在 <input> 元素中输入一个以上的值。
    multiple 属性适用于以下输入类型：email 和 file。

    实例
    接受多个值的文件上传字段：
    Select images: <input type="file" name="img" multiple>

    # pattern 属性 https://www.w3school.com.cn/tiy/t.asp?f=html5_input_pattern
    pattern 属性规定用于检查 <input> 元素值的正则表达式。
    pattern 属性适用于以下输入类型：text、search、url、tel、email、and password。
    提示：请使用全局的 title 属性对模式进行描述以帮助用户。
    提示：请在我们的 JavaScript 教程中学习更多有关正则表达式的知识。

    实例
    只能包含三个字母的输入字段（无数字或特殊字符）：
    Country code: 
    <input type="text" name="country_code" pattern="[A-Za-z]{3}" title="Three letter country code">

    # placeholder 属性 https://www.w3school.com.cn/tiy/t.asp?f=html5_input_placeholder
    placeholder 属性规定用以描述输入字段预期值的提示（样本值或有关格式的简短描述）。
    该提示会在用户输入值之前显示在输入字段中。
    placeholder 属性适用于以下输入类型：text、search、url、tel、email 以及 password。

    实例
    拥有占位符文本的输入字段：
    <input type="text" name="fname" placeholder="First name">

    # required 属性 https://www.w3school.com.cn/tiy/t.asp?f=html5_input_required
    required 属性是布尔属性。
    如果设置，则规定在提交表单之前必须填写输入字段。
    required 属性适用于以下输入类型：text、search、url、tel、email、password、date pickers、number、checkbox、radio、and file.

    实例
    必填的输入字段：
    Username: <input type="text" name="usrname" required>

    # step 属性  https://www.w3school.com.cn/tiy/t.asp?f=html5_input_step
    step 属性规定 <input> 元素的合法数字间隔。
    示例：如果 step="3"，则合法数字应该是 -3、0、3、6、等等。
    提示：step 属性可与 max 以及 min 属性一同使用，来创建合法值的范围。
    step 属性适用于以下输入类型：number、range、date、datetime、datetime-local、month、time 以及 week。

    示例
    拥有具体的合法数字间隔的输入字段：
    <input type="number" name="points" step="3">



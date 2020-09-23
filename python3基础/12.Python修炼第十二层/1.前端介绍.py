\HTTP协议
    1、什么是HTTP协议：
        超文本传输协议

    2、为何要用HTTP协议
        是应用层测协议，用于浏览器与web服务端之间传输数据
    
    3、如何用HTTP协议
        1、HTTP是基于TCP协议
        2、HTTP协议的特点
            I：无连接
                HTTP协议本身是没有连接的，但每进行一次HTTP协议的通信必先建立TCP连接，该TCP连接会在通信完毕后关闭，如果短时间内再次发起HTTP请求
                则必须重新建立连接，这么做的缺点是：1、对服务端造成过大的压力 2、数据传输速度慢。

                解决方法：
                    keepalive
            II：无状态
                cookie与session，cookie离开session无法工作。
        3、HTTP之request
            GET url HTTP/1.1\r\n
            k1:v1\r\n
            k2:v2\r\n
            ....
            请求体（只有post方法才有请求体）

            请求URL：
                https://www.baidu.com/test/aaaaa/bbbbb.html?a=1&b=1#anc1
            请求方法：
                GET
                    请注意，查询字符串（名称/值对）是在 GET 请求的 URL 中发送的
                    GET 请求可被缓存
                    GET 请求保留在浏览器历史记录中
                    GET 请求可被收藏为书签
                    GET 请求不应在处理敏感数据时使用（不安全）
                    GET 请求有长度限制
                    GET 请求只应当用于取回数据

                POST
                    请注意，查询字符串（名称/值对）是在 POST 请求的 HTTP 消息主体中发送的
                    POST 请求不会被缓存
                    POST 请求不会保留在浏览器历史记录中
                    POST 不能被收藏为书签
                    POST 请求对数据长度没有要求


            请求头：
                user-agent
                referer
                cookie

        4、HTTP之response
            HTTP/1.1 200 Ok\r\n
            k1:v1\r\n
            k2:v2\r\n
            ...
            \r\n
            相应体（即我们要从服务端下载的内容）
        5、HTTP 状态消息
           https://www.w3school.com.cn/tags/html_ref_httpmessages.asp
           
2、HTML
    1、是什么？
        超文本标记语言，即学习这门语言就是在一堆标记

    2、为何要用？
        标记文本

    3、如何用？
        HTML标签就是用来做记号的，虽然这些记号自带一些样式，但务必忽略掉记号的样式，样式会专用用css来做

        标签/元素

        <标签名 属性名="属性值">包含的文本内容</标签名>
        <标签名 属性名="属性值" />

        只站在html角度，按照能否嵌套子标签，可以将标签分为两大类：
            容器类标签：可以嵌套任意其他类型的标签
            文本类标签：只能嵌套文字、图片、超链接

\Web服务本质
import socket
sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

sk.bind(("127.0.0.1", 8080))
sk.listen(5)

while True:
    conn, addr = sk.accept()
    data = conn.recv(8096)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"<h1>Hello world!</h1>")
    conn.close()
浏览器发请求 --> HTTP协议 --> 服务端接收请求 --> 服务端返回响应 --> 服务端把HTML文件内容发给浏览器 --> 浏览器渲染页面

\前端语言
HTML       # 内容
CSS        # 样式
JavaScript # 动态（雷锋和雷锋塔，名字上沾边。本质上没关系。）

\框架
CSS # Bootstrap
JS  # jQuery

\每部分需要学习的内容
HTML  # 标签
CSS   # 选择器、属性
JS    # 基础语法、BOM & DOM



\HTML文档结构
<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>css样式优先级</title>
    </head>
    <body>

    </body>
</html>

1、<!DOCTYPE html>  # 声明为HTML5文档。\<!DOCTYPE> 标签.声明必须是 HTML 文档的第一行，位于 <html> 标签之前。声明不是 HTML 标签；它是指示 web 浏览器关于页面使用哪个 HTML 版本进行编写的指令。
2、<html>、</html>  # 是文档的开始标记和结束的标记。是HTML页面的根元素，在它们之间是文档的头部（head）和主体（body）。
3、<head>、</head>  # 定义了HTML文档的开头部分。它们之间的内容不会在浏览器的文档窗口显示。包含了文档的元（meta）数据。
4、<title>、</title># 定义了网页标题，在浏览器标题栏显示。
5、<body>、</body>  # 之间的文本是可见的网页主体内容。
注意：对于中文网页需要使用 <meta charset="utf-8"> 声明编码，否则会出现乱码。有些浏览器会设置 GBK 为默认编码，则你需要设置为 <meta charset="gbk">。

\各部分解释
#1、<!DOCTYPE HTML>是文档声明，必须写在HTML文档的第一行，位于<html>标签之前，表明该文档是HTML5文档。
#2、<html></html> 称为根标签，所有的网页标签都在<html></html>中。
    HTML的lang属性可用于网页或部分网页的语言。通常用于搜索引擎和浏览器的统计分析,不定义也没什么影响
    根据 W3C 推荐标准，您应该通过 <html> 标签中的 lang 属性对每张页面中的主要语言进行声明，比如：<html lang="en"></html>,用于搜索引擎识别
#3、<head></head> 标签用于定义文档的头部，它是所有头部元素的容器。常见的头部元素有<title>、<script>、<style>、<link>和<meta>等标签，头部标签在下一节中会有详细介绍，<head>与</head>之间的内容不会在浏览器的文档窗口显示，但是其间的元素有特殊重要的意义。
#4、在<body>和</body>标签之间的内容是网页的主要内容，最终会在浏览器中显示出来。

\标签间关系
#1、并列（兄弟／平级）
    head与body
#2、嵌套（父子／上下级）
    html内 有head 有body 

\HTML标签格式
# 双标签
    HTML标签是由尖括号包围的关键字，比如<html>, <div>等
    HTML标签通常是成对出现的， 比如：<div>和</div>，第一个标签是开始，第二个标签是结束。结束标签会有斜线。
# 单标签
    也有一部分标签是单独呈现的，比如：<br/>、<hr/>、<img src="1.jpg" />等。

标签里面可以有若干属性，也可以不带属性。


\标签的语法
    <标签名 属性1=“属性值1” 属性2=“属性值2”……>内容部分</标签名>
    <标签名 属性1=“属性值1” 属性2=“属性值2”…… />

\HTML中标签分类
单从是否可以嵌套子标签的角度去分，标签分为两类
#1、容器类标签
    容器类标签可以简单的理解为能嵌套其它所有标签的标签。
    常见容器级的标签: 
        h系列 
        ul>li
        ol>li
        dl>dt+dd
        div

#2、文本类标签
    文本级的标签对应容器级标签，只能嵌套文字/图片/超链接的标签。
    常见文本级的标签:
        p
        span
        strong
        em
        ins
        del

#3、块级标签、行内标签和行内块标签
块级标签：
div、h1-h6、p、ol、ul、li、dd、dt、dl、form、table、menu、address、dir、fieldset、noframe、hr、pre

行内标签：
a、label、select、span、b/strong、br、img、input、font、bdo、big、small、cite、em、i、kbd、sub、sup、textarea

行内块标签
img、input

控制标签类型的样式
display：block块级 、inline行内 、inline-block行内块 、none隐藏

给标签设置基点
vertical-align：top/middle/bottom

内联元素是指本身属性为 display:inline的元素，其宽度随元素的内容而变化。因为他自身的特点，我们通常使用内联元素来进行文字、小图片（小结构）的搭建。
内联元素的特点：
内联元素会和其他元素从左到右显示在一行。
内联元素不能直接控制宽度、高度以及盒子模型的相关css属性，但是可以设置内外边距的水平方向的值。也就是说对于内联元素的margin和padding，只有margin-left/margin-right和padding-left/padding-right是有效的，但是竖直方向的margin和padding无效果。
内联元素的宽高是由内容本身的大小决定的（文字、图片等）。
内联元素只能容纳文本或者其他内联元素（不要在内联元素中嵌套块级元素）。

\标签中几个很重要的属性
    id：   # 规定元素的唯一 id
    class：# 为html元素定义一个或多个类名（classname）(CSS样式类名)
    style：# 规定元素的行内样式（CSS样式）
    title  # 规定元素的额外信息（可在工具提示中显示）,已知title标签没有title属性。

\HTML注释
<!--注释内容-->  # 注释是代码之母。--摘自哪吒语录
无论我们学习什么编程语言，一定要重视的就是注释，HTML中注释的格式:

<!--这里是注释的内容-->
# 注意： 注释中可以直接使用回车换行。

并且我们习惯用注释的标签把HTML代码包裹起来。如：
<!-- xx部分 开始 -->
    这里放你xx部分的HTML代码
<!-- xx部分 结束 -->

HTML注释的注意事项：
#1、HTML注释不支持嵌套。
#2、HTML注释不能写在HTML标签中。




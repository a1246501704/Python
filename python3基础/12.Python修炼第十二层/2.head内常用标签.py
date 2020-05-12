\head内 Meta相关标签
Meta标签介绍：
    <meta> 元素可提供有关页面的元信息（mata-information）,针对搜索引擎和更新频度的描述和关键词。
    <meta> 标签位于文档的头部，不包含任何内容。
    <meta> 提供的信息是用户不可见的。
meta标签的组成：meta标签共有两个属性，它们分别是http-equiv属性和name 属性，不同的属性又有不同的参数值，这些不同的参数值就实现了不同的网页功能。 

0.指定字符集
<meta charset="gbk">

1.http-equiv属性：相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确地显示网页内容，与之对应的属性值为content，content中的内容其实就是各个参数的变量值。
<!--2秒后跳转到对应的网址，注意引号-->
    <meta http-equiv="refresh" content="2;URL=https://www.oldboyedu.com">
<!--三秒刷新,如果同时写多个则最后一个生效。-->
    <meta http-equiv="refresh" content="3">

<!--指定文档的编码类型-->
    <meta http-equiv="content-Type" charset="UTF8">

<!--告诉IE以最高级模式渲染文档-->
    <meta http-equiv="x-ua-compatible" content="IE=edge">

# Expires(期限)
说明：可以用于设定网页的到期时间。一旦网页过期，必须到服务器上重新传输。
用法：
<meta http-equiv="expires"content="Fri,12Jan200118:18:18GMT">

# Pragma(cache模式)
说明：禁止浏览器从本地计算机的缓存中访问页面内容。
用法：
<meta http-equiv="Pragma"content="no-cache">
注意：这样设定，访问者将无法脱机浏览。

# Refresh(刷新)
说明：自动刷新并指向新页面。
用法：
<meta http-equiv="Refresh"content="2;URL=http://www.haorooms.com"> //(注意后面的引号，分别在秒数的前面和网址的后面) 
注意：其中的2是指停留2秒钟后自动刷新到URL网址。

# Set-Cookie(cookie设定)
说明：如果网页过期，那么存盘的cookie将被删除。
用法：
<meta http-equiv="Set-Cookie"content="cookie value=xxx;expires=Friday,12-Jan-200118:18:18GMT；path=/">

# Window-target(显示窗口的设定)
说明：强制页面在当前窗口以独立页面显示。
用法：
<meta http-equiv="Window-target"content="_top">
注意：用来防止别人在框架里调用自己的页面。

# content-Type(显示字符集的设定)
说明：设定页面使用的字符集。
用法：
<meta http-equiv="content-Type"content="text/html;charset=gb2312">
具体如下：
meta标签的charset的信息参数如GB2312时，代表说明网站是采用的编码是简体中文；
meta标签的charset的信息参数如BIG5时，代表说明网站是采用的编码是繁体中文；
meta标签的charset的信息参数如iso-2022-jp时，代表说明网站是采用的编码是日文；
meta标签的charset的信息参数如ks_c_5601时，代表说明网站是采用的编码是韩文；
meta标签的charset的信息参数如ISO-8859-1时，代表说明网站是采用的编码是英文；
meta标签的charset的信息参数如UTF-8时，代表世界通用的语言编码；


2.name属性: 主要用于描述网页，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的。
#关键字：有助于搜索引擎SEC优化，再怎么优化也抵不过竞价排名
    <meta name="Keywords" content="网易，邮箱，游戏，新闻">
        说明：keywords用来告诉搜索引擎你网页的关键字是什么。
    <meta name="description" content="老男孩教育Python学院">
        说明：description用来告诉搜索引擎你的网站主要内容。
    <meta name="robots"content="none">
        说明：robots用来告诉搜索机器人哪些页面需要索引，哪些页面不需要索引。
        content的参数有all,none,index,noindex,follow,nofollow。默认是all。
        具体参数如下：
        信息参数为all：文件将被检索，且页面上的链接可以被查询；
        信息参数为none：文件将不被检索，且页面上的链接不可以被查询；
        信息参数为index：文件将被检索；
        信息参数为follow：页面上的链接可以被查询；
        信息参数为noindex：文件将不被检索，但页面上的链接可以被查询；
        信息参数为nofollow：文件将被检索，但页面上的链接不可以被查询；
    <meta name="author"content="root,root@xxxx.com">
        说明：标注网页的作者
    <meta name="generator"content="信息参数"/>
        说明：meta标签的generator的信息参数，代表说明网站的采用的什么软件制作。
    <META NAME="COPYRIGHT"CONTENT="信息参数">
        说明：meta标签的COPYRIGHT的信息参数，代表说明网站版权信息。
    <META name="revisit-after"CONTENT="7days">
        说明：revisit-after代表网站重访,7days代表7天，依此类推。

3.content属性: 页面描述
<meta name="Description" content="具体描述。。。">


\head内 非Meta相关标签
<title></title>	    # 定义网页标题
<link/>	            # 引入外部样式表文件  https://www.w3school.com.cn/tags/tag_link.asp
<style></style>	    # 定义body内部样式
<meta/>	            # 定义网页原信息
<script></script>	# 定义JS代码或引入外部JS文件

#1、定义网页标题
<title>百度一下，你就知道</title>

#2、网站的图标
<link rel="icon" href="https://www.baidu.com/favicon.ico">

#3、引入外部样式文件，层叠样式。引入css样式
<link rel="stylesheet" href="mystyle.css">

#4、定义内部样式
<style></style>

#4、定义JavaScript代码或引入JavaScript文件
<script src="hello.js"></script>

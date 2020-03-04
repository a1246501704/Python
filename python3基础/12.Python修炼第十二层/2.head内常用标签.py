\head内 非Meta相关标签
#1、定义网页标题
<title>百度一下，你就知道</title>

#2、网站的图标
<link rel="icon" href="https://www.baidu.com/favicon.ico">

#3、定义内部样式
<style></style>

#4、引入外部样式文件
<link rel="stylesheet" href="mystyle.css">

#5、定义JavaScript代码或引入JavaScript文件
<script src="hello.js"></script>


\head内 Meta相关标签
Meta标签介绍：
    <meta> 元素可提供有关页面的元信息（mata-information）,针对搜索引擎和更新频度的描述和关键词。
    <meta> 标签位于文档的头部，不包含任何内容。
    <meta> 提供的信息是用户不可见的。
meta标签的组成：meta标签共有两个属性，它们分别是http-equiv属性和name 属性，不同的属性又有不同的参数值，这些不同的参数值就实现了不同的网页功能。 

1.http-equiv属性：相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确地显示网页内容，与之对应的属性值为content，content中的内容其实就是各个参数的变量值。
<!--2秒后跳转到对应的网址，注意引号-->
    <meta http-equiv="refresh" content="2;URL=https://www.oldboyedu.com">
    三秒刷新
    <meta http-equiv="refresh" content="3">
<!--指定文档的编码类型-->
    <meta http-equiv="content-Type" charset=UTF8">
<!--告诉IE以最高级模式渲染文档-->
    <meta http-equiv="x-ua-compatible" content="IE=edge">

2.name属性: 主要用于描述网页，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的。
#关键字：有助于搜索引擎SEC优化，再怎么优化也抵不过竞价排名
    <meta name="Keywords" content="网易，邮箱，游戏，新闻">
    <meta name="description" content="老男孩教育Python学院">

3.页面描述
<meta name="Description" content="具体描述。。。">
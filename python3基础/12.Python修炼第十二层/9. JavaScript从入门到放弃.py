一 JavaScript简介
二 JavaScript引入方式
三 JavaScript语法规范
四 变量
五 数据类型与内置方法
    5.1 数组对象Array
    5.2 Date日期对象
    5.3 Math对象
    5.4 JSON对象
    5.5 RegExp对象
    5.6 JavaScript 允许自定义对象
六 运算符
七 流程控制
八 函数
    8.1 函数的定义与调用（与python类同） 
    8.2 函数中的arguments参数
    8.3 函数的全局变量和局部变量
    8.4 作用域
    8.5 javascript中的变量提升和函数提升
九 BOM与DOM操作: BOM 用于使用JS代码操作浏览器
                DOM 用于使用JS代码操作HTML文档


\一 JavaScript简介
1、JavaScript起源
https://www.cnblogs.com/linhaifeng/articles/9346219.html
总结JavaScript用途：
    #javaScript一般用来编写客户端脚本，来为html页面添加交互行为，是前台语言，而不是后台语言（node.js除外）
    简单地说，ECMAScript 描述了JavaScript语言本身的相关内容。
    JavaScript 是脚本语言
    JavaScript 是一种轻量级的编程语言。
    JavaScript 是可插入 HTML 页面的编程代码。
    JavaScript 插入 HTML 页面后，可由所有的现代浏览器执行。
    JavaScript 很容易学习。
总结JavaScript的特点：
    #1、解释执行（浏览器就是解释器）：事先不编译、逐行执行、无需进行严格的变量声明。
    #2、简单易用：可以使用任何文本编辑工具编写，只需要浏览器就可以执行程序。
    #3、基于对象：内置大量现成对象，编写少量程序可以完成目标 
2、JavaScript组成
    #1、ECMAScript 核心：JavaScript的语法标准。包括变量、表达式、运算符、函数、if语句、for语句等。
    #2、文档对象模型（DOM） Document object model：操作网页上的元素的API。比如让盒子移动、变色、轮播图等。
    #3、浏览器对象模型（BOM） Broswer object model：操作浏览器部分功能的API。比如让浏览器自动滚动。 
Javascript之BOM与DOM讲解: https://www.cnblogs.com/linhaifeng/articles/13696427.html

3、ECMAScript和JavaScript的关系
ECMAScript是一种由Ecma国际（前身为欧洲计算机制造商协会,英文名称是European Computer Manufacturers Association）通过ECMA-262标准化的脚本程序设计语言。这种语言在万维网上应用广泛，它往往被称为JavaScript或JScript，
所以ECMAScript可以理解为是javascript的一个标准,而javascript是ECMA-262标准的实现和扩展。

1996年11月，JavaScript的创造者--Netscape公司，决定将JavaScript提交给国际标准化组织ECMA，希望这门语言能够成为国际标准。次年，ECMA发布262号标准文件（ECMA-262）的第一版，规定了浏览器脚本语言的标准，并将这种语言称为ECMAScript，这个版本就是1.0版。
该标准一开始就是针对JavaScript语言制定的，但是没有称其为JavaScript，有两个方面的原因。一是商标，JavaScript本身已被Netscape注册为商标。而是想体现这门语言的制定者是ECMA，而不是Netscape，这样有利于保证这门语言的开发性和中立性。
因此ECMAScript和JavaScript的关系是，前者是后者的标准，后者是前者的一种实现。

ECMAScript的历史(注：ES6就是指ECMAScript 6)
年份	    名称	        描述
1997	ECMAScript 1	第一个版本
1998	ECMAScript 2	版本变更
1999	ECMAScript 3	添加正则表达式
                        添加try/catch
        ECMAScript 4	没有发布
2009	ECMAScript 5	添加"strict mode"严格模式
                        添加JSON支持
2011	ECMAScript 5.1	版本变更
2015	ECMAScript 6（ES6）	添加类和模块
2016	ECMAScript 7	增加指数运算符（**）
                        增加Array.prototype.includes

\二 HTML中引入JavaScript的方式
# 1、方式一
<script>
  # 在这里写你的JS代码
</script>

# 2、方式二
<script src="xxx.js"></script>

# 示例
    运行 02 HTML引用JS代码.html 文件

\三 JavaScript语法规范
#1、JavaScript对换行、缩进、空格不敏感。
    ps：每一条语句末尾要加上分号，虽然分号不是必须加的，但是为了程序今后要压缩，如果不加分号，压缩之后将不能运行。

#2、所有的符号，都是英语的。比如括号、引号、分号。
#3、JavaScript的注释：
　　单行注释： 
            // 我是注释
   多行注释：
            /*
              多行注释1
              多行注释2
            */
# 4、结束符
JavaScript中的语句要以分号（;）为结束符。    

# 5、日常调试 运行html代码后打开f12 在console中直接写完回车就可以快速调试

\四 JavaScript语言基础
\变量
# 1、声明变量的语法
    1. 先声明后定义
    var name;   # 声明变量时无需指定类型，变量name可以接受任意类型
    name= "egon"; # 全局变量

    var name= "egon"; # 在浏览器f12中练习即可
    name
    输出：egon

    2. 声明立刻定义
        var age = 18;
# 2、变量名命名规范
    #1. 由字母、数字、$ 、下划线、 组成,但是不能数字开头，也不能纯数字
    #2. 严格区分大小写
    #3. 不能包含关键字和保留字（以后升级版本要用的关键字）。
    如：abstract、boolean、byte、char、class、const、debugger、double、enum、export、extends、final、float、goto
    implements、import、int、interface、long、native、package、private、protected、public、short、static、super、synchronized、throws、transient、volatile
    #4. 推荐驼峰命名法：有多个有意义的单词组成名称的时候，第一个单词的首字母小写，其余的单词首字母写
    #5. 匈牙利命名：就是根据数据类型单词的的首字符作为前缀
# 3、ES6中let
    ES6之前js没有块级作用域，ES6新增了let命令，用于声明变量（声明的变量属于块级作用域），流程控制语句的{}就是块级作用域。其用法类似于var，但是所声明的变量只在let命令所在的代码块内有效。例如：for循环的计数器就很适合使用let命令。
    for(let i=1;i<=5;i++){
        console.log(i)
    }
    i # 5

    for(let j=1;j<=5;j++){
        console.log(j)
    }
    j # is not defined

# 4、常量
    ES6新增const用来声明常量。一旦声明，其值就不能改变。
    const PI = 3.1415926;
    PI=3 # TypeError: "PI" is read-only

\五 数据类型与内置方法
js是动态语言：变量里面能够存储数字、字符串等。变量会自动的根据存储内容的类型不同，来决定自己的类型。

# 数据类型
    数值
    字符串
    布尔值
    Null
    Undefined
    Object

# 1、数值（Number）
JavaScript不区分整型和浮点型，就只有一种数字类型，即number
var x = 3;
var y = 3.1;
var z = 13e5;  # 13 * 10的5次方
var m = 13e-5;
var n = NaN;  # NaN也是数值类型 typeof n;是Number类型，其结果表示不是一个数字（Not a Number）
# 常用方法： pasreInt方法是将字符串转换为整形数字
parseInt("123")  # 返回123
parseInt("ABC")  # 返回NaN,NaN属性是代表非数字值的特殊值。该属性用于指示某个值不是数字。
parseFloat("123.456") # 返回123.456

# 四舍五入
var num=1.3456
num.toFixed(2) # "1.35"

# 字符串类型转成数字
    # 字符串转numbber
    parseInt("123")  # 返回123

    # NaN属性是代表非数字值的特殊值。该属性用于指示某个值不是数字。
    parseInt("ABC")  # 返回NaN

    # 带有自动净化的功能；只保留字符串最开头的数字，后面的中文自动消失。例如：
    console.log(parseInt("18林海峰")); # 18

    # 只去末尾的中文，不会去开头的
    console.log(parseInt("林海峰18")); # NaN

    # 字符串中的数字转浮点
    parseInt("123.456")  # 返回123
    parseFloat("123.456")# 返回123.456 

    # 自动带有截断小数的功能：取整，不四舍五入
    var a = parseInt("1.3") + parseInt("2.6");     # a=3
    var a = parseFloat("1.3") + parseFloat("2.6"); # a=3.9

# 数字类型转成字符串
    # 数字转成字符串类型
    var x=10;
    var y='20';
    var z=x+y; # z='1020'
    typeof z;  # String

    # 数字转成字符串类型
    var m=123;
    var n=String(m)

    var a=123;
    var b=a.toString()

# 2、字符串（String）
var a = "Hello"
var b = "world;
var c = a + b; 
console.log(c);  #  得到Helloworld

# 常用方法：
#  方法	                             说明
如: c.length
.length	                            统计长度
.trim()	                            移除空白
.trimLeft()	                        移除左边的空白
.trimRight()	                    移除右边的空白
.charAt(n)	                        返回第n个字符 
.concat(value, ...)	                拼接,拼接字符串通常使用“+”号
.indexOf(substring, start)	        子序列位置
.substring(from, to)	            按索引取值
.slice(start, end)	                切片
.toLowerCase()	                    转为小写
.toUpperCase()	                    转为大写
.split(delimiter, limit)	        分割

string.slice(start, stop)和string.substring(start, stop)：
# slice和substring的区别
两者的相同点：
如果start等于end，返回空字符串
如果stop参数省略，则取到字符串末
如果某个参数超过string的长度，这个参数会被替换为string的长度

substirng()的特点：
如果 start > stop ，start和stop将被交换
如果参数是负数或者不是数字，将会被0替换

silce()的特点：
如果 start > stop 不会交换两者
如果start小于0，则切割从字符串末尾往前数的第abs(start)个的字符开始(包括该位置的字符)
如果stop小于0，则切割在从字符串末尾往前数的第abs(stop)个字符结束(不包含该位置字符)

# 补充：
ES6中引入了模板字符串。模板字符串（template string）是增强版的字符串，用反引号（`）标识，它的用途为:
    #1. 完全可以当做普通字符串使用
    var msg = `my name is egon`

    #2. 也可以用来定义多行字符串
    var info = `
        name:egon
        age:18
        sex:male
    `
    #3. 并且可以在字符串中嵌入变量
    var name = "egon";
    var age = 18;
    var msg = `my name is ${name}, my age is ${age}`;
    注意：如果模板字符串中需要使用反引号，则在其前面要用反斜杠转义。
    pycharm启用ES6语法支持: 方法1、设置 —— Languages —— Javascript
                          方法2、在js文件顶部添加  /* jshint esversion: 6 */

# 3、布尔值（Boolean）
区别于Python，true和false都是小写。
var a = true;
var b = false;
任何数据类型都可以转换为boolean类型：空字符串、0、null、undefined、NaN 都是false。

# 布尔值为假的数据类型
Boolean('')
Boolean(0)
Boolean(null)
Boolean(undefined)
Boolean(NaN)

# 其余数据类型的布尔值均为真，例如
Boolean([])
Boolean(123)

# 4、null和undefined
null表示值是空，一般在需要指定或清空一个变量时才会使用，如 name=null;
undefined表示当声明一个变量但未初始化时，该变量的默认值是undefined。还有就是函数无明确的返回值时，返回的也是undefined。
null表示变量的值是空，undefined则表示只声明了变量，但还没有赋值。 

# 5、常用内置对象
JavaScript 中的所有事物都是对象：字符串、数值、数组、函数...
此外I,JavaScript还提供多个内建对象，比如 Array,Date,Math 等等
对象只是带有属性和方法的特殊数据类型



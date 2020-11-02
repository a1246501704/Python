\六 伪类选择器
#1、作用：针对a标签常用的几种伪类选择器。

#1.1 没有访问过的超链接a标签样式：
a:link {
  color: blue;
}

#1.2 访问过以后的超链接a标签样式：
a:visited {
  color: gray;
}

#1.3 鼠标悬浮在元素上应用样式：
a:hover {
  background-color: #eee; 
}

#1.4 鼠标点击不松手的样式：
a:active {
  color: green;
}

#1.5 input输入框获取焦点时样式：
input:focus {
  outline: none;
  background-color: #eee;
}

#2 注意：
a标签的伪类选择器可以单独出现，也可以一起出现
a标签的伪类选择器如果一起出现，有严格的顺序要求，否则失效
    link，visited，hover，active
hover是所有其他标签都可以使用的
focus只给input标签使用


# 示例
<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>伪类选择器</title>
      <style type="text/css">
          a:link {
              color: #cccccc;
          }
          a:visited {
              color: #55BBBB;
          }
          a:hover {
              color: green;
          }
          a:active {
              color: red;
          }
          input:hover {
              outline: none;
              background-color: #cccccc;
          }
      </style>
  </head>
  <body>
    <a href="https://www.baidu.com/a/b/c/d.html">点击我</a>
    <input type="text">
  </body>
</html>



# 3 过渡模块的基本使用
# 3.1、过渡三要素
  1.1 必须要有属性发生变量，如
          div:hover {
              width: 300px;
          }
  1.2 必须告诉系统哪个属性需要执行过渡效果
          transition-property: width;
  1.3 必须告诉系统过渡效果持续时长
          transition-duration: 5s;


# 3.2、注意：
    当多个属性需要同时执行过渡效果时，用逗号分隔即可
        transition-property:width,background-color;
        transition-duration: 5s,5s;

示范
<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <style>
          * {
              margin: 0;
              padding: 0;
          }
          div {
              width: 100px;
              height: 50px;
              background-color: red;

              /*
              告诉系统哪个系统需要执行过渡效果
              transition-property: width;
              /*告诉系统过渡效果持续的时长
              transition-duration: 5s;

              css是层叠样式表，这么写会跟上面的冲突，所以我们需要修改
              transition-property: background-color;
              transition-duration: 5s;
              */

              transition-property:width,background-color;
              transition-duration: 5s,5s;
          }

          /*
          hover这个伪类选择器除了可以用在a标签上，还可以用在任何其他的标签上
          */
          div:hover {
              width: 300px;
              background-color: green;
          }
      </style>
  </head>
  <body>
    <div></div>
  </body>
</html>


控制过渡的速度transition-timing-function
  值	                      描述
linear	规定以相同速度开始至结束的过渡效果（等于 cubic-bezier(0,0,1,1)）。
ease	  规定慢速开始，然后变快，然后慢速结束的过渡效果（cubic-bezier(0.25,0.1,0.25,1)）。
ease-in	规定以慢速开始的过渡效果（等于 cubic-bezier(0.42,0,1,1)）。
ease-out	规定以慢速结束的过渡效果（等于 cubic-bezier(0,0,0.58,1)）。
ease-in-out	规定以慢速开始和结束的过渡效果（等于 cubic-bezier(0.42,0,0.58,1)）。
cubic-bezier(n,n,n,n)	在 cubic-bezier 函数中定义自己的值。可能的值是 0 至 1 之间的数值。


实例 1
为了更好地理解不同的函数值，请看下面带有五个不同值的五个不同的 div 元素：
<!DOCTYPE html>
<html>
  <head>
    <style> 
      div{
        width:100px;
        height:50px;
        background:red;
        color:white;
        font-weight:bold;
        transition:width 2s;
        -moz-transition:width 2s; /* Firefox 4 */
        -webkit-transition:width 2s; /* Safari and Chrome */
        -o-transition:width 2s; /* Opera */
      }

      #div1 {transition-timing-function: linear;}
      #div2 {transition-timing-function: ease;}
      #div3 {transition-timing-function: ease-in;}
      #div4 {transition-timing-function: ease-out;}
      #div5 {transition-timing-function: ease-in-out;}

      div:hover{
      width:300px;
      }
    </style>
  </head>
  <body>
    <div id="div1" style="top:100px">linear</div>
    <div id="div2" style="top:150px">ease</div>
    <div id="div3" style="top:200px">ease-in</div>
    <div id="div4" style="top:250px">ease-out</div>
    <div id="div5" style="top:300px">ease-in-out</div>
    <p>请把鼠标指针移动到红色的 div 元素上，就可以看到过渡效果。</p>
    <p><b>注释：</b>本例在 Internet Explorer 中无效。</p>
  </body>
</html>

实例 2
与上例相同，但通过 cubic-bezier 来规定速度曲线：
<!DOCTYPE html>
<html>
  <head>
    <style> 
      div {
        width:100px;
        height:50px;
        background:red;
        color:white;
        font-weight:bold;
        transition:width 2s;
        -moz-transition:width 2s; /* Firefox 4 */
        -webkit-transition:width 2s; /* Safari and Chrome */
        -o-transition:width 2s; /* Opera */
      }
      #div1 {transition-timing-function: cubic-bezier(0,0,0.25,1);}
      #div2 {transition-timing-function: cubic-bezier(0.25,0.1,0.25,1);}
      #div3 {transition-timing-function: cubic-bezier(0.42,0,1,1);}
      #div4 {transition-timing-function: cubic-bezier(0,0,0.58,1);}
      #div5 {transition-timing-function: cubic-bezier(0.42,0,0.58,1);}
      
      div:hover {
      width:300px;
      }
    </style>
  </head>
  <body>
    <div id="div1" style="top:100px">linear</div>
    <div id="div2" style="top:150px">ease</div>
    <div id="div3" style="top:200px">ease-in</div>
    <div id="div4" style="top:250px">ease-out</div>
    <div id="div5" style="top:300px">ease-in-out</div>
    <p>请把鼠标指针移动到红色的 div 元素上，就可以看到过渡效果。</p>
    <p><b>注释：</b>本例在 Internet Explorer 中无效。</p>
  </body>
</html>

# 4 过渡模块连写
#1 过渡属性连写
transition: 过渡属性 过渡时长 运动速度 延迟时间;

#2 过渡连写注意点
2.1 和分开写一样，如果想给多个属性添加过渡效果也是用逗号隔开即可
2.2 连写的时间，可以省略后面的两个参数，因为只要编写了前面两个参数
就满足了过渡的三要素

2.3 如果多个属性运动的速度、延迟时间、持续时间都一样，那么可以简写为
transition: all 5s;

示范
<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <style>
          * {
              margin: 0;
              padding: 0;
          }
          div {
              width: 100px;
              height: 50px;
              background-color: red;

              /*transition: width 5s linear 0s;*/
              /*transition: width 5s linear 0s,background-color*/
              /*5s linear 0s;*/

              /*transition: width 5s,background-color 5s;*/
              /*transition: width 5s,background-color,height 5s;*/

              transition: all 5s;

          }

          div:hover {
              width: 500px;
              background-color: blue;

              height: 500px;
          }
      </style>
  </head>
    <body>
    <div></div>
  </body>
</html>

# 5  练习

# 5.1 弹性效果
<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <style>
          * {
              margin: 0;
              padding: 0;
          }

          div {
              height: 100px;
              background-color: grey;
              margin-top: 100px;
              text-align: center;
          }

          span {
              font-size: 50px;
              line-height: 100px;

              transition: all 5s;
          }

          div:hover span {
              margin-left: 50px;
          }
      </style>
  </head>
  <body>
    <div>
        <span>EGON</span>
        <span>是</span>
        <span>讲</span>
        <span>师</span>
        <span>界</span>
        <span>的</span>
        <span>恐</span>
        <span>怖</span>
        <span>分</span>
        <span>子</span>
    </div>
  </body>
</html>

# 5.2 手风琴效果
<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <style>
          * {
              margin: 0;
              padding: 0;
          }

          div {
              width: 1000px;
              height: 300px;
              margin: 0 auto;
          }

          img {
              width: 200px;
              height: 300px;
          }

          ul {
              width: 1000px;
              height: 300px;
              background-color: grey;
              list-style: none;
              margin: 100px auto;

              /*
              最后一张图片超出了，因为每一张图片很大
              但默认情况我们不想看到，所以剪裁掉多余
              */
              overflow: hidden;
          }

          ul li {
              width: 100px;
              height: 300px;
              float: left;

              transition: all 0.3s;
          }

          ul:hover li {
              width: 88px;
          }

          /*谁更具体谁的优先级更高，ul 下的li更具体，而ul可能指定有很多li*/
          ul li:hover {
              width: 200px;
          }
      </style>
  </head>
  <body>
    <div>
        <ul>
            <li><img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180516225724530-539090864.jpg" alt=""></li>
            <li><img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180516225751362-1832630751.jpg" alt=""></li>
            <li><img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180516225809591-1990809146.jpg" alt=""></li>
            <li><img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180516225816920-580320384.jpg" alt=""></li>
            <li><img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180516225828392-1011509025.jpg" alt=""></li>
            <li><img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180516225836490-1526815653.jpg" alt=""></li>
            <li><img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180516225847998-887601490.jpg" alt=""></li>
            <li><img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180516225853390-460353134.jpg" alt=""></li>
            <li><img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180516225859796-1981914722.jpg" alt=""></li>
            <li><img src="https://images2018.cnblogs.com/blog/1036857/201805/1036857-20180516225906468-571800433.jpg" alt=""></li>
        </ul>
    </div>
  </body>
</html>



\nth-child() 与 nth-of-type()的定义与用法
nth-child(n) : 匹配父元素中的第 n 个子元素，元素类型没有限制。
nth-of-type(n) : 匹配同类型中的第n个同级兄弟元素。
n可以是一个数字，一个关键字，或者一个公式，比如：nth-child(odd) 奇数 ,nth-child(even) 偶数。

nth-child和nth-of-type的不同之处就是查找元素的方式不同。前者是查找兄弟元素中某个绝对位置的元素，
后者是查找同类型元素中某个绝对位置的元素。相同之处是，两者都是找到元素之后再与前面的选择符进行匹配，这里的匹配方式是一样的。

举例说明 nth-of-type和nth-child的区别
# 1、给第一个div五个P标签，给第二个div五个H5标签，分别用nth-child(2)与nth-of-type(2),看看结果是不是一样的，都是第二个变色。
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <style>
            p:nth-child(2){color: red;}
            h5:nth-of-type(2){color: blue;}
        </style>
    </head>
    <body>
        <div>
            <p>星期一</p>
            <p>星期二</p>
            <p>星期三</p>
            <p>星期四</p>
            <p>星期五</p>
        </div>
        <div>
            <h5>段落一</h5>
            <h5>段落二</h5>
            <h5>段落三</h5>
            <h5>段落四</h5>
            <h5>段落五</h5>
        </div>
    </body>
</html>

# 2、现在我们对HTML代码做点改动，让他们出现一些不同，CSS样式不变。我们将第一个p元素和第一个h5元素改为h4，代码如下：
# 看看，现在是不是发现nth-of-type(2)结果变了，段落3变色了。h5:nth-of-type(2)要找的是第二个h5类型的元素，也就是段落3。
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <style>
            p:nth-child(2){color: red;}
            h5:nth-of-type(2){color: blue;}
        </style>
    </head>
    <body>
        <div>
            <p>星期一</p>
            <p>星期二</p>
            <p>星期三</p>
            <p>星期四</p>
            <p>星期五</p>
        </div>
        <div>
            <h4>段落一</h4>
            <h5>段落二</h5>
            <h5>段落三</h5>
            <h5>段落四</h5>
            <h5>段落五</h5>
        </div>
    </body>
</html>

# 3、继续改动HTML代码。我们恢复第一个p元素和第一个h5元素，将第二个p元素和第二个h5元素改为h4，样式仍保持不变，结果会怎样呢？
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <style>
            p:nth-child(2){color: red;}
            h5:nth-of-type(2){color: blue;}
        </style>
    </head>
    <body>
        <div>
            <p>星期一</p>
            <h4>星期二</h4>
            <p>星期三</p>
            <p>星期四</p>
            <p>星期五</p>
        </div>
        <div>
            <h5>段落一</h5>
            <h4>段落二</h4>
            <h5>段落三</h5>
            <h5>段落四</h5>
            <h5>段落五</h5>
        </div>
    </body>
</html>

'''
结果可以看到nth-child没有效果，nth-of-type高亮的是段落3。
为什么会这样？
nth-child 是查找一堆兄弟元素里的第二个元素，不管那元素是什么，只要它排行第二就行。这里前一个div找到的是 星期二
后一个div找到的是 段落二。找到之后，再和前面的选择符进行匹配，如果匹配对了，那就应用样式。前面的选择符是p，也就是要求元素是p类型，
但这里都是h4，不匹配，两个元素都不会应用这个样式。

nth-of-type 是在一堆兄弟元素里找到相同HTML标记类型元素中排行第二的元素。在第一个div中 星期三是p类型里排行第二的元素；在后一个div中
段落三 是h5类型里排行第二的元素。找到之后，再和前面的选择符进行匹配，如果匹配对了，那就应用样式。前面的选择符是h5, 那么只有后一个div中
段落三 元素应用了样式，前一个div的 星期二则不会。
'''